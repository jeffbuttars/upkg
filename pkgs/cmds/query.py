import logging
logger = logging.getLogger('pkgs')

import os

from cmds.base import BaseCmd
from conf import settings
from lib import nice_pkg_name


class Cmd(BaseCmd):
    """Docstring for Search """

    name = 'query'
    help_text = ("Advanced quering")

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
            help=("Get information about installed 'pkgs'"),
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

        pl = self.list_pkgs()
        if not pl:
            print("No packages installed, use 'pkgs install'")    

        for p in pl:
            print(p)
        # end for p in self.lis
    #exec()

    def list_pkgs(self):
        """todo: Docstring for self.list_pkgs
        :return:
        :rtype:
        """

        dlist = os.listdir(settings.pkgs_destdir)
        res = []
        for d in dlist:
            dp = os.path.join(settings.pkgs_destdir, d)
            if os.path.isdir(dp):
                res.append(nice_pkg_name(d))
        # end for d in dlist

        return res
    #list_pkgs()
# Cmd
