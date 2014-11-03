import logging
logger = logging.getLogger('upkg')

import os
import sys
import subprocess

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

from blessings import Terminal

import shutil
from urllib.parse import urlparse
from pprint import pformat as pf
import sh
from sh import git

from conf import settings
from . import ctx as upkg_ctx

sh.logging_enabled = True

ugly_ext = ('.git', '.hg')


class InvalidRepo(Exception):
    """Docstring for InvalidRepo """
    pass
#InvalidRepo


def repo_dirlist():
    """List out the directories in the install location(s)
    :return:
    :rtype:
    """

    for d in os.listdir(settings.upkg_destdir):
        dp = os.path.join(settings.upkg_destdir, d)
        # logger.debug("%s", dp)
        if os.path.isdir(dp) and d[0] != '.':
            # logger.debug("adding %s", dp)
            yield {'base': d, 'root': settings.upkg_destdir,
                   'path': dp}
#repo_dirlist()


def did_u_mean(name):
    """todo: Docstring for did_u_mean

    :param name: arg description
    :type name: type description
    :return:
    :rtype:
    """
    logger.debug("%s", name)

    dlist = Repo.installed_list()
    res = []
    for d in dlist:
        if name in d.name or d.name in name:
            res.append(nice_pkg_name(d.name))
    # end for d in dlist

    if res:
        return "Did you mean '" + " or ".join(res) + "'?"

    return ""
#did_u_mean()


def pkg_name_to_path(pkgname):
    """todo: Docstring for pkg_name_to_path

    :param pkgname: arg description
    :type pkgname: type description
    :return:
    :rtype:
    """

    logger.debug("'%s'", pkgname)

    fp = os.path.join(settings.upkg_destdir, pkgname)
    if os.path.isdir(fp):
        logger.debug("found %s", fp)
        return fp

    # Try to find the repo dir if just needs an extension
    for d in repo_dirlist():
        logger.debug("trying %s", d)
        if d['base'].startswith(pkgname):
            # logger.debug("startwith")
            root, ext = os.path.splitext(d['base'])
            if pkgname == root:
                logger.debug("found %s", d)
                return d['path']
    # end for d in dlist

    logger.debug("found nothing")
    return ""
#pkg_name_to_path()


def nice_pkg_name(name):
    """todo: Docstring for nice_pkg_name

    :param name: arg description
    :type name: type description
    :return:
    :rtype:
    """
    logger.debug("%s", name)

    root, ext = os.path.splitext(name)
    logger.debug("root :'%s', ext: '%s'", root, ext)

    if ext in ugly_ext:
        logger.debug("remove ext %s to get %s", ext, root)
        return root

    logger.debug("no change %s", name)
    return name
#nice_pkg_name()


class Repo(object):
    """
        Repo object. Perform git operations on a given repo.
    """

    def __init__(self, repo_dir="", name="", url=""):
        """todo: to be defined

        :param repo_dir: arg description
        :type repo_dir: type description
        :param name: arg description
        :type name: type description
        :param url: arg description
        :type url: type description
        """
        logger.debug("repo_dir: %s, name: %s, url: %s", repo_dir, name, url)

        if not (repo_dir or name or url):
            estr = "You must supply at least one of: repo_dir, name, or url."
            logger.error(estr)
            raise InvalidRepo(estr)

        self._repo_dir = repo_dir
        self._name = nice_pkg_name(name)
        self._url = url
        self._basename = ""

        self.supported_schemes = ('git', 'https', 'http', 'file', '')


        self._ctx = upkg_ctx.get_ctx()
        self.term = Terminal()
    #__init__()

    def __repr__(self):
        """todo: Docstring for __repr__
        :return:
        :rtype:
        """

        return "{} URL:{} LOCATION: {}".format(
            self._name,
            self._url,
            self._repo_dir
        )
    #__repr__()

    def _build_writer(self, output, color=None, prefix=""):
        if color:

            def _cwriter(line):
                go = getattr(self.term, color)
                output(go(self.name + ": " + prefix + line))

            return _cwriter

        def _writer(line):
            output(self.name + ": " + prefix + line)

        return _writer
    #_build_writer()

    def _sh_stdout(self, *args, **kwargs):
        return self._build_writer(sys.stdout.write, *args, **kwargs)
    #_sh_stdout()

    def _sh_stderr(self, *args, **kwargs):
        return self._build_writer(sys.stderr.write, *args, **kwargs)
    #_sh_stderr()

    def __str__(self):
        """todo: Docstring for __str__
        :return:
        :rtype:
        """

        return "{} : {}".format(self.name, self.url)
    #__str__()

    @property
    def name(self):
        logger.debug("name: %s", self._name)

        if not self._name:
            self._name = nice_pkg_name(self.basename)

        return self._name

    @property
    def repo_dir(self):
        logger.debug("repo_dir: %s", self._repo_dir)

        if not self._repo_dir:
            bn = self.basename
            if bn:
                self._repo_dir = os.path.join(settings.upkg_destdir, bn)

        return self._repo_dir

    @property
    def url(self):
        logger.debug("url: %s", self._url)

        if not self._url:
            rd = self.repo_dir
            out = StringIO()
            cwd = os.getcwd()
            os.chdir(rd)

            p = git('ls-remote', '--get-url',
                        _out=out, _err=self._sh_stderr('red'))
            p.wait()
            os.chdir(cwd)
            self._url = out.getvalue().strip()
            logger.debug("URL? %s", self._url)
            out.close()

        return self._url

    @property
    def basename(self):
        logger.debug("basename: %s, repo_dir: %s", self._basename, self._repo_dir)

        if self._repo_dir:
            self._basename = os.path.basename(self._repo_dir)
        elif self._url:
            url = urlparse(self._url)
            self._basename = os.path.basename(url.path)
        else:
            self._basename = os.path.basename(pkg_name_to_path(self._name))

        return self._basename

    @property
    def installed(self):
        rd = self.repo_dir
        if rd:
            return os.path.exists(rd)

        return rd
    #installed()

    @classmethod
    def installed_list(cls):
        """todo: Docstring for list
        :return:
        :rtype:
        """
        logger.debug("")

        res = []
        for x in repo_dirlist():
            d = x['path']
            try:
                res.append(Repo(repo_dir=d, name=x['base']))
            except InvalidRepo:
                logger.warning("Invalid repo '%s' in the installation directory.", d)

        return res
    #installed_list()

    def pr_pass(self, fmt, *args, **kwargs):
        print(self.term.green(fmt.format(*args, **kwargs)))
    #pr_pass()

    def pr_info(self, fmt, *args, **kwargs):
        print(self.term.blue(fmt.format(*args, **kwargs)))
    #pr_info()

    def pr_fail(self, fmt, *args, **kwargs):
        print(self.term.red(fmt.format(*args, **kwargs)))
    #pr_fail()

    def pr_atten(self, fmt, *args, **kwargs):
        print(self.term.red(fmt.format(*args, **kwargs)))
    #pr_atten()

    def clone(self):
        """todo: Docstring for clone
        :return:
        :rtype:
        """
        logger.debug("")
    
        if not self.url:
            estr = "Cannot install this repos without a URL. %s" % self.info()
            logger.warning(estr)
            raise ValueError(estr)

        # check if the already exists, if so, don't install, update it?
        url = urlparse(self.url)
        url_path = url[2]
        path_end = url_path.split('/')
        path_end = path_end[len(path_end) - 1]

        if url.scheme not in self.supported_schemes:
            raise ValueError("Unsupported scheme '{}' for {}".format(url.scheme, self.url))

        assert self.repo_dir, "Invalid repo directory."

        # Clone it.
        logger.debug("cloning %s into %s .", self.url, self.repo_dir)
        self.pr_pass("\nInstalling %s ... " % self.url)

        p = git.clone('--progress', self.url, self.repo_dir,
                      _out=self._sh_stdout('blue'), _err=self._sh_stderr('blue'))
        p.wait()
    #clone()

    def install_update_deps(self):
        """todo: Docstring for install_update_deps
        :return:
        :rtype:
        """
        logger.debug("")
        self._ctx.installed(self.name)

        # are there any dependencies?
        depfile = os.path.join(self.repo_dir, '_upkg', 'depends')
        logger.debug("depfile? %s", depfile)
        if os.path.exists(depfile):
            logger.debug("Found depends file at %s", depfile)
            deps = open(depfile, 'r')
            dep = deps.readline()
            while dep:
                dep = dep.strip()
                logger.debug("depends: %s", dep)
                self._ctx.add_dep(nice_pkg_name(os.path.basename(dep)), dep)
                dep = deps.readline()
            deps.close()

        for rep in self._ctx.deps_needed:
            repo = Repo(url=rep)
            if repo.installed:
                repo.update()
            else:
                repo.install()
    #install_update_deps()

    def install(self):
        """todo: Docstring for install
        :return:
        :rtype:
        """
        logger.debug("")

        # If we're already installed, don't do anything.
        if self.installed:
            self.pr_info("pkg {} is already installed. Perhaps you want to update it?",
                    self.name)
            return

        self.clone()
        self.install_update_deps()

        logger.debug("Checking for install script")

        inst = os.path.join(self.repo_dir, '_upkg', 'install')
        if os.path.exists(inst):
            cwd = os.getcwd()
            logger.debug("chdir to %s", os.path.join(self.repo_dir, '_upkg'))
            logger.debug("install script is %s", inst)
            self.pr_info("Running install script at {}", inst)
            logger.debug("runnin script %s", inst)
            # We use subprocess instead of the sh module due to problems with
            # runing shell scripts with sh
            os.chdir(os.path.join(self.repo_dir, '_upkg'))
            subprocess.check_call(inst, shell=True)
            os.chdir(cwd)
            self.pr_pass("install script finished")
    #install()

    def remove(self):
        """todo: Docstring for remove
        :return:
        :rtype:
        """
        logger.debug("")

        rd = self.repo_dir

        logger.debug("pkg path %s", rd)
        if not rd:
            print(
                "unable to find pkg '%s'. %s" % (self.name, did_u_mean(self.name))
            )
            return

        # Does the repo have any uncommitted changes?
        # Is the repo out of sync(needs a push?)

        # Are you sure?
        resp = input(self.term.red("Are you sure you want to remove the '%s' pkg? [y|N] " %
                                   self.name))

        if resp == 'y' or resp == 'yes':
            self.pr_atten('removing {}...', self.name)
            shutil.rmtree(rd)

    #remove()

    def update(self):
        """todo: Docstring for update
        :return:
        :rtype:
        """
        logger.debug("")

        rd = self.repo_dir

        logger.debug("pkg path %s", rd)
        if not rd:
            print(
                "unable to find pkg '%s'. %s" % (self.name, did_u_mean(self.name))
            )

        cwd = os.getcwd()
        os.chdir(self.repo_dir)
        logger.debug("cwd: %s, updating %s ", cwd, self.repo_dir)
        try:
            p = git.pull('--rebase', '--progress',
                         _out=self._sh_stdout('blue'),
                         _err=self._sh_stderr('red'))
            p.wait()
        except Exception as e:
            pass
            # logger.warn(e)

        os.chdir(cwd)

        # Update or install any dependancies before running the
        # update script.
        self.install_update_deps()

        up = os.path.join(self.repo_dir, '_upkg', 'update')
        if os.path.exists(up):
            # We use subprocess instead of the sh module due to problems with
            # runing shell scripts with sh
            cwd = os.getcwd()
            os.chdir(os.path.join(self.repo_dir, '_upkg'))
            self.pr_info("Running update script for {} @ {}", self.name, up)
            subprocess.check_call(up, shell=True)
            os.chdir(cwd)
    #update()

    def push(self):
        """todo: Docstring for push
        :return:
        :rtype:
        """

        pass
    #push()

    def status(self):
        """Get status on the repo.
        :return:
        :rtype:
        """

        rd = self.repo_dir

        logger.debug("pkg path %s", rd)
        if not rd:
            print(
                "unable to find pkg '%s'. %s" % (self.name, did_u_mean(self.name))
            )

        cwd = os.getcwd()
        os.chdir(self.repo_dir)
        logger.debug("cwd: %s, getting status %s ", cwd, self.repo_dir)
        try:
            p = git.status(_out=self._sh_stdout('blue'),
                           _err=self._sh_stderr('red'))
            p.wait()
        except Exception:
            pass
            # logger.warn(e)
        os.chdir(cwd)

    #status()

#Repo
