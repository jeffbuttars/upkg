import logging
logger = logging.getLogger('pkgs')

from sh import git
from urlib.parse import urlparse

from cmds.base import BaseCmd
from ..conf import settings



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

        # check if the already exists, if so, don't install
        url = urlparse(repo)

        if url.scheme not in self.supported_schemes:
            raise Exception("Unsupported scheme '{}' for {}".format(url.scheme, repo))

        # 


        # Clone it.
        git.clone("{} {}".format(repo, settings.pkgs_destdir))
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
