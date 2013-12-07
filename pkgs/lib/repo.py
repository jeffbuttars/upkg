import logging
logger = logging.getLogger('pkgs')

import os
import sys
import shutil
from urllib.parse import urlparse
from pprint import pformat as pf
from sh import git

from conf import settings
from lib.base import InvalidRepo, pkg_name_to_path, did_u_mean


def nice_pkg_name(name):
    """todo: Docstring for nice_pkg_name

    :param name: arg description
    :type name: type description
    :return:
    :rtype:
    """
    logger.debug("%s", name)

    root, ext = os.path.splitext(name)

    if ext in ugly_ext:
        return root

    return name
#nice_pkg_name()


def pkg_name_to_path(pkgname):
    """todo: Docstring for pkg_name_to_path

    :param pkgname: arg description
    :type pkgname: type description
    :return:
    :rtype:
    """

    logger.debug("'%s'", pkgname)

    dlist = Repo.installed()

    for d in dlist:
        fp = os.path.join(settings.pkgs_destdir, d)
        # logger.debug("checking if %s", fp)
        if not os.path.isdir(fp):
            # logger.debug("moving on")
            continue

        if pkgname == d:
            # logger.debug("match")
            return fp

        if d.startswith(pkgname):
            # logger.debug("startwith")
            root, ext = os.path.splitext(d)
            if pkgname == root:
                return fp
    # end for d in dlist

    return None
#pkg_name_to_path()


class Repo(object):
    """
        Repo object. Perform git operations on a given repo.
    """

    def __init__(self, repo_dir=None, name=None, url=None):
        """todo: to be defined

        :param repo_dir: arg description
        :type repo_dir: type description
        :param name: arg description
        :type name: type description
        :param url: arg description
        :type url: type description
        """

        if not repo_dir or name or url:
            estr = "You must supply at least one of: repo_dir, name, or url."
            logger.error(estr)
            raise InvalidRepo(estr)

        self._repo_dir = repo_dir
        self._name = name
        self._url = url
        self._basename = None

    #__init__()

    def __repr__(self):
        """todo: Docstring for __repr__
        :return:
        :rtype:
        """

        return pf(self.info())
    #__repr__()

    def _sh_stdout(self, line):
        print(line)
    #_sh_stdout()

    def _sh_stderr(self, line):
        sys.stderr.write("{}\n".format(line))
    #_sh_stderr()

    def __str__(self):
        """todo: Docstring for __str__
        :return:
        :rtype:
        """

        return pf(self.info())
    #__str__()

    @property
    def name(self):
        if not self._name:
            self._name = nice_pkg_name(self._basename)

        return self._name

    @property
    def repo_dir(self):
        if not self._repo_dir:
            self._repo_dir = pkg_name_to_path(self.basename)
                
        return self._repo_dir

    @property
    def url(self):
        if not self._url:
            # Get it from the git info
            rd = self.repo_dir

                
        return self.url

    @property
    def basename(self):

        if self._repo_dir:
            self._basename = os.path.basename(self._repo_dir)
        elif self._url:
            url = urlparse(self.url)
            self._basename = sys.path.basename(url.path)
        else:
            self._basename = sys.path.basename(pkg_name_to_path(self._name))

        return self._basename

    @classmethod
    def installed(cls, self):
        """todo: Docstring for list
        :return:
        :rtype:
        """

        res = []
        for x in os.listdir(settings.pkgs_destdir):
            d = os.path.join(settings.pkgs_destdir, x)
            try:
                res.append(Repo(repo_dir=d))
            except InvalidRepo:
                logger.warning("Invalid repo '%s' in the installation directory.", d)

        return res
    #installed()

    def install(self):
        """todo: Docstring for install
        :return:
        :rtype:
        """

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

        # Clone it.
        dest = os.path.join(settings.pkgs_destdir, path_end)
        logger.debug("cloning %s into %s .", self.url, dest)
        p = git.clone('--progress', self.url, dest,
                      _out=self._sh_stdout, _err=self._sh_stderr,
                      _out_bufsize=0, _in_bufsize=0)
        p.wait()
    #install()

    def update(self):
        """todo: Docstring for update
        :return:
        :rtype:
        """

        pass
    #update()

    def remove(self):
        """todo: Docstring for remove
        :return:
        :rtype:
        """

        pkg = pkg_name_to_path(self.name)

        logger.debug("pkg path %s", pkg)
        if not pkg:
            print(
                "unable to find pkg '%s'. %s" % (self.name, did_u_mean(self.name))
            )

        # Does the repo have any uncommitted changes?
        # Is the repo out of sync(needs a push?)

        # Are you sure?
        resp = input("Are you sure you want to remove the '%s' pkg? [y|N] " % self.name)

        if resp == 'y' or resp == 'yes':
            print('removing %s...' % self.name)
            shutil.rmtree(pkg)

    #remove()

    def info(self):
        """todo: Docstring for info
        :return:
        :rtype:
        """

        pass
    #info()
#Repo
