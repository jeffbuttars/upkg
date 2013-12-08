import logging
logger = logging.getLogger('pkgs')

from blessings import Terminal

from cmds.base import BaseCmd
from lib import Repo


class Cmd(BaseCmd):
    """Docstring for Search """

    name = 'status'
    help_text = ("Get the status of what's installed")

    def build(self):
        """todo: Docstring for build
        :return:
        :rtype:
        """

        self._cmd_parser.add_argument(
            'status',
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

        logger.debug("status %s", args.status)
        self.status(args.status)
    #exec()

    def status(self, repos):
        """

        :param repos: arg description
        :type repos: type description
        :return:
        :rtype:
        """
        logger.debug("repos: %s", repos)

        if repos:
            rlist = [Repo(name=x) for x in repos]
        else:
            # Update them all!
            rlist = Repo.installed()

        logger.debug("repo list: %s", rlist)

        t = Terminal()
        for r in rlist:
            logger.debug("calling statsu on: %s", r)
            r.status()
            w = t.width
            print("\n" + ("*" * w) + "\n")
        # end for r in rlist
    #status()
# Cmd
