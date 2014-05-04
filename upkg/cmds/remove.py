import logging
logger = logging.getLogger('upkg')


from upkg.cmds.base import BaseCmd
from upkg.lib import Repo


class Cmd(BaseCmd):
    """Docstring for Search """

    name = 'remove'
    help_text = ("remove installed pkg(s)")

    def build(self):
        """todo: Docstring for build
        :return:
        :rtype:
        """

        self._cmd_parser.add_argument(
            'remove',
            type=str,
            default=None,
            nargs="+",
            help=("Remove an installed pkg"),
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

        logger.debug("remove %s", args.remove)

        for pkg in args.remove:
            logger.debug("removing %s", pkg)
            self.remove_repo(pkg)
        # end for repo in args.remove
    #exec()

    def remove_repo(self, rname):
        """todo: Docstring for remove_repo

        :param repo: arg description
        :type repo: type description
        :return:
        :rtype:
        """
        logger.debug("%s", rname)
        repo = Repo(name=rname)
        repo.remove()

        return repo
    #remove_repo()
# Cmd
