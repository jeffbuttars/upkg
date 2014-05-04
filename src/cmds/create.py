import logging
logger = logging.getLogger('upkg')

import os
import stat

from cmds.base import BaseCmd

TMPL_README = """
# {pkg_name}


"""

TMPL_INSTALL = """#!/bin/bash

# This script will be run after a upkg has been checked out.
# Put any custom install shell code here.
#
# Upkg will provide some helper functions and data in the environment.
#
# Variables:
#   $THIS_DIR
#       The current directory of execution. This will be the directory containing
#       this script.
#   $PKGS_PKG_DIR
#       The directory that contains you upkg repos.
#
# helper functions:
#
# The pr_* function print their arguments to the console as colored text.
#   pr_pass()
#       Print a pass, or positive, message to the console
#   pr_fail()
#       Print a fail, or negative, message to the console
#   pr_info()
#       Print an informational message to the console

"""

TMPL_UPDATE = """#!/bin/bash

# This script will be run after a upkg has been updated.
# Put any custom update shell code here.
#
# Upkg will provide some helper functions and data in the environment.
#
# Variables:
#   $THIS_DIR
#       The current directory of execution. This will be the directory containing
#       this script.
#   $PKGS_PKG_DIR
#       The directory that contains you upkg repos.
#
# helper functions:
#
# The pr_* function print their arguments to the console as colored text.
#   pr_pass()
#       Print a pass, or positive, message to the console
#   pr_fail()
#       Print a fail, or negative, message to the console
#   pr_info()
#       Print an informational message to the console

"""

TMPL_REMOVE = """#!/bin/bash

# This script will be run before a upkg is removed.
# Put any custom remove shell code here.
#
# Upkg will provide some helper functions and data in the environment.
#
# Variables:
#   $THIS_DIR
#       The current directory of execution. This will be the directory containing
#       this script.
#   $PKGS_PKG_DIR
#       The directory that contains you upkg repos.
#
# helper functions:
#
# The pr_* function print their arguments to the console as colored text.
#   pr_pass()
#       Print a pass, or positive, message to the console
#   pr_fail()
#       Print a fail, or negative, message to the console
#   pr_info()
#       Print an informational message to the console

"""

TMPLS = [
    {"name": '../README.md', 'tmpl': TMPL_README},
    {"name": 'install',
     'mode': stat.S_IEXEC | stat.S_IREAD | stat.S_IWRITE, 'tmpl': TMPL_INSTALL},
    {"name": 'update',
     'mode': stat.S_IEXEC | stat.S_IREAD | stat.S_IWRITE, 'tmpl': TMPL_UPDATE},
    {"name": 'remove',
     'mode': stat.S_IEXEC | stat.S_IREAD | stat.S_IWRITE, 'tmpl': TMPL_REMOVE},
]


class Cmd(BaseCmd):

    name = 'create'
    help_text = ("Create a skeleton upkg")
    aliases = ['cr']

    def build(self):
        """todo: Docstring for build
        :return:
        :rtype:
        """

        self._cmd_parser.add_argument(
            'create',
            type=str,
            default=None,
            nargs=1,
            help=(""),
        )

        return super(Cmd, self).build()
    # build()

    def exec(self, args):
        """todo: Docstring for exec
        
        :param args: arg description
        :type args: type description
        :return:
        :rtype:
        """
        logger.debug("create %s", args.create[0])

        self.create_repo(args.create[0])
    # exec()

    def safe_mkdir(self, d):
        """If a directory doesn't exist, create it.
        If it does exist, print a warning to the logger.
        If it exists as a file, rais a FileExistsError

        :param d: directory path to create
        :type d: str
        """

        if os.path.isfile(d):
            raise FileExistsError(
                "Cannont create directory %s, a file by that name already exists." % d)

        if os.path.isdir(d):
            logger.warning("%s already exists, using existing directory.", d)
            return

        os.makedirs(d)
    # safe_mkdir()

    def mk_tmpl(self, path, tmpl, ctx, mode=None):
        """Create a file from a template if it doesn't already exist.
        """

        path = os.path.abspath(path)

        if os.path.isfile(path):
            logger.warning("File %s already exists, not creating it.", tmpl)

        with open(path, 'w') as fd:
            fd.write(
                tmpl.format(**ctx)
            )
            if mode:
                os.chmod(path, mode)
    # mk_tmpl()

    def create_repo(self, name):
        """todo: Docstring for create_repo
        
        :param name: arg description
        :type name: type description
        :return:
        :rtype:
        """

        name = os.path.abspath(name)
        logger.debug("create_repo %s", name)

        self.safe_mkdir(name)

        udir = os.path.join(name, '_upkg')
        self.safe_mkdir(udir)

        ctx = {
            'pkg_name': os.path.basename(name),
        }

        for t in TMPLS:
            self.mk_tmpl(
                os.path.join(udir, t['name']),
                t['tmpl'],
                ctx,
                t.get('mode')
            )
        # end for t in TMPLS
    # create_repo()
# Cmd
