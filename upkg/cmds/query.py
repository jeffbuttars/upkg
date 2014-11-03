import logging
logger = logging.getLogger('upkg')

from upkg.cmds.base import BaseCmd
from upkg.lib import Repo


class Cmd(BaseCmd):
    """Docstring for Search """

    name = 'query'
    help_text = ("Advanced quering")
    aliases = ['q']

    def build(self):
        """todo: Docstring for build
        :return:
        :rtype:
        """

        self._cmd_parser.add_argument(
            'query',
            type=str,
            default=None,
            nargs="*",
            # nargs=1,
            help=("Get information about installed 'upkg'"),
        )

        return super(Cmd, self).build()
    #build()

    def exec(self, args):
        """todo: Docstring for exec

        :param args: arg description
        :type args: type description
        :return:
        :rtype:
        """

        logger.debug("query %s", args.query)

        pl = Repo.installed_list()
        if not pl:
            print("No packages installed, use 'upkg install'")

        idx = 1
        for p in pl:
            print("[%s] %s" % (idx, p))
            idx += 1
    #exec()
# Cmd
