import logging
logger = logging.getLogger('pkgs')

from cmds.base import BaseCmd
from lib import Repo


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

        if not repos:
            # Update them all!
            rlist = [Repo(name=x) for x in repos]
        else:
            rlist = Repo.installed()

        for r in rlist:
            r.update()
        # end for r in rlist
    #update()
# Cmd
