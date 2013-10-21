from cmds.base import BaseCmd


class Cmd(BaseCmd):
    """Docstring for Search """

    name = 'install'
    help_text = ("install pkgs")

    def build(self):
        """todo: Docstring for build
        :return:
        :rtype:
        """

        # self._cmd_parser.add_argument(
        #     's',
        #     type=str,
        #     default=None,
        #     # nargs="?",
        #     nargs=1,
        #     help=(""),
        # )

        return super(Cmd, self).build()
    #build()
# Cmd
