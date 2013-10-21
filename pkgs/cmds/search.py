from cmds.base import BaseCmd


class Cmd(BaseCmd):
    """Docstring for Search """

    name = 'search'

    def build(self):
        """todo: Docstring for build
        :return:
        :rtype:
        """

        self._cmd_parser = self._sub_parser.add_parser(
            'search',
            help=("search for pkgs"),
        )

        # self._cmd_parser.add_argument(
        #     'search',
        #     type=str,
        #     default=None,
        #     # nargs="?",
        #     nargs=1,
        #     help=("Search for a package/repo by name"),
        # )

        return super(Cmd, self).build()
    #build()
# Cmd
