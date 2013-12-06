import logging
logger = logging.getLogger('pkgs')

import shutil

from lib import pkg_name_to_path, did_u_mean
from cmds.base import BaseCmd


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
            self.remove_repo(pkg)
        # end for repo in args.remove
    #exec()

    def remove_repo(self, repo):
        """todo: Docstring for remove_repo

        :param repo: arg description
        :type repo: type description
        :return:
        :rtype:
        """
        logger.debug("%s", repo)

        pkg = pkg_name_to_path(repo)

        logger.debug("pkg path %s", pkg)
        if not pkg:
            print(
                "unable to find pkg '%s'. %s" % (repo, did_u_mean(repo))
            )

        # Does the repo have any uncommitted changes?
        # Is the repo out of sync(needs a push?)

        # Are you sure?
        resp = input("Are you sure you want to remove the '%s' pkg? [y|N] " % repo).lower()

        if resp == 'y' or resp == 'yes':
            print('removing %s...' % repo)
            shutil.rmtree(pkg)

    #remove_repo()
# Cmd
