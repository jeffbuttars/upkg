import logging
logger = logging.getLogger('pkgs')

from cmds.base import BaseCmd
from lib import installed_list()


class Cmd(BaseCmd):
    """Docstring for Search """

    name = 'update'
    help_text = ("update all or some pkgs")

    def build(self):
        """todo: Docstring for build
        :return:
        :rtype:
        """

        self._cmd_parser.add_argument(
            'update',
            type=str,
            default=None,
            nargs="*",
            help=(""),
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

        logger.debug("update %s", args.update)
        self.update(args.update) 
    #exec()

    def update(self, repos):
        """

        :param repos: arg description
        :type repos: type description
        :return:
        :rtype:
        """

        pass
        rlist = []
        if not repos:
            # Update them all!
            rlist = installed_list()
        else:
            # make sure the supplied repos are valid, if they are, update them!
            pass
    #update()
# Cmd
