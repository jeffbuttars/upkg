import logging
logger = logging.getLogger('upkg')

import os

from upkg.cmds.base import BaseCmd
from upkg.conf import settings
from upkg.lib import Repo


class Cmd(BaseCmd):
    """Docstring for Search """

    name = 'install'
    help_text = ("install upkg")
    aliases = ['in', 'ins', 'inst', 'insta', 'instal']

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

        self._cmd_parser.add_argument(
            '-l',
            '--location',
            default=None,
            help=("Specify the installation location. ")
        )

        return super(Cmd, self).build()

    def install_repo(self, repo, location=''):
        """todo: Docstring for install_repo
        :param repo: arg description
        :type repo: type description
        :return:
        :rtype:
        """

        dst = location or settings.upkg_destdir

        # make sure the destination dir exists.
        if not os.path.exists(dst):
            os.makedirs(dst)

        # repo = Repo(url=repo, repo_dir=dst)
        repo = Repo(url=repo)
        repo.install()

        return repo

    def exec(self, args):
        """todo: Docstring for exec

        :param args: arg description
        :type args: type description
        :return:
        :rtype:
        """

        logger.debug("install %s, location %s", args.install, args.location)
        location = args.location and os.path.abspath(args.location)

        if location and len(args) > 1:
            raise Exception(("You cannot specify multiple install packages when "
                             "using the --location option."
                            ))

        for repo in args.install:
            self.install_repo(repo, location)
