import logging
logger = logging.getLogger('upkg')

from cmds.base import BaseCmd


class Cmd(BaseCmd):
    """Docstring for Search """

    name = 'search'
    help_text = ("search repos for a package")
    aliases = ['s', 'se', 'sea', 'sear', 'searc']

    def build(self):
        """todo: Docstring for build
        :return:
        :rtype:
        """

        self._cmd_parser.add_argument(
            'search',
            type=str,
            default=None,
            nargs="+",
            help=("Search for a package/repo by name or by user/reponame"),
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

        logger.debug("search %s", args.search)
    #exec()
# Cmd
