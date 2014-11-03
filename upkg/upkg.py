#!/usr/bin/env python
# encoding: utf-8

import logging

# Set up the logger
logger = logging.getLogger('upkg')
cmd_logger = logging.getLogger('command')
# Use a console handler, set it to debug by default
logger_ch = logging.StreamHandler()
logger.setLevel(logging.INFO)
log_formatter = logging.Formatter(
    ('%(asctime)s %(levelname)s:%(process)s'
                                   ' %(lineno)s:%(module)s:%(funcName)s()'
                                   ' %(message)s')
)
logger_ch.setFormatter(log_formatter)
logger.addHandler(logger_ch)

import sys
import os

if __name__ == '__main__':
    this_dir = os.path.realpath(os.path.dirname(__file__))
    sys.path.insert(0, os.path.abspath(os.path.join(this_dir, "../")))
#     sys.path.insert(0, os.path.abspath(this_dir))

import argparse
import cmds

parser = argparse.ArgumentParser(
    "upkg",
    description=("Package Yourself")
)

# parser.add_argument('-t', '--test',
#                     default='default_value',
#                     help=("Some nice help for this option")
#                     )

parser.add_argument('-d',
                    '--debug',
                    default=False, action='store_true',
                    help=("Enable debug output and debug run mode")
                    )

parser.add_argument('-c',
                    '--config',
                    default=None,
                    help=("Specify a config file location.")
                    )

def main():
    print(sys.path)
    # Sub parsers.
    sub_parser = parser.add_subparsers(help=("upkg commands"))
    cmds.build_cmds(sub_parser)

    args = parser.parse_args()
    if args.debug:
        logger.setLevel(logging.DEBUG)
        cmd_logger.setLevel(logging.DEBUG)

    logger.debug("args: %s", args)

    import conf
    conf.load_settings(args.config)

    logger.debug("settings: %s", conf.settings)

    if hasattr(args, 'func'):
        return args.func(args)
    parser.print_help()
# main()

if __name__ == '__main__':
    main()
