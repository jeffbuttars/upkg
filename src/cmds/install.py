import logging
logger = logging.getLogger('upkg')

import os

from cmds.base import BaseCmd
from conf import settings
from lib import Repo


class Cmd(BaseCmd):
    """Docstring for Search """

    name = 'install'
    help_text = ("install upkg")
    aliases = ['i', 'in', 'ins', 'inst', 'insta', 'instal']

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
        if not os.path.exists(settings.upkg_destdir):
            os.makedirs(settings.upkg_destdir)

        repo = Repo(url=repo)
        repo.install()

        return repo
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
#repo Cmd
