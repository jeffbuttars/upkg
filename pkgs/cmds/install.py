import logging
logger = logging.getLogger('pkgs')

import os

from sh import git
from urllib.parse import urlparse

from cmds.base import BaseCmd
from conf import settings


def out_she_goes(line):
    print(line)
#out_she_goes()


class Cmd(BaseCmd):
    """Docstring for Search """

    name = 'install'
    help_text = ("install pkgs")
    supported_schemes = ('https', 'http', 'file', '')

    def build(self):
        """todo: Docstring for build
        :return:
        :rtype:
        """

        self._cmd_parser.add_argument(
            'install',
            type=str,
            default=None,
            nargs="+",
            help=(""),
        )

        return super(Cmd, self).build()
    #build()

    def install_repo(self, repo):
        """todo: Docstring for install_repo
        :param repo: arg description
        :type repo: type description
        :return:
        :rtype:
        """

        # make sure the destination dir exists.
        if not os.path.exists(settings.pkgs_destdir):
            os.makedirs(settings.pkgs_destdir)

        # check if the already exists, if so, don't install, update it?
        url = urlparse(repo)
        url_path = url[2]
        path_end = url_path.split('/')
        path_end = path_end[len(path_end) - 1]

        if url.scheme not in self.supported_schemes:
            raise Exception("Unsupported scheme '{}' for {}".format(url.scheme, repo))

        # Clone it.
        dest = os.path.join(settings.pkgs_destdir, path_end)
        logger.debug("cloning %s into %s .", repo, dest)
        p = git.clone('--progress', repo, dest,
                      _out=out_she_goes, _err=out_she_goes,
                      _out_bufsize=0, _in_bufsize=0)
        p.wait()
    #install_repo()

    def exec(self, args):
        """todo: Docstring for exec

        :param args: arg description
        :type args: type description
        :return:
        :rtype:
        """

        logger.debug("install %s", args.install)

        for repo in args.install:
            self.install_repo(repo)
        # end for repo in args.install
    #exec()
# Cmd
