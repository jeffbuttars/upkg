#!/usr/bin/env python
# encoding: utf-8
# c816656e1eaf42a58fbc2cc36ea5870e

import logging
# Set up the logger
logger = logging.getLogger('upkg')
cmd_logger = logging.getLogger('command')
# Use a console handler, set it to debug by default
logger_ch = logging.StreamHandler()
logger.setLevel(logging.INFO)
log_formatter = logging.Formatter(('%(asctime)s %(levelname)s:%(process)s'
                                   ' %(lineno)s:%(module)s:%(funcName)s()'
                                   ' %(message)s'))
logger_ch.setFormatter(log_formatter)
logger.addHandler(logger_ch)


def main():

    logger.setLevel(logging.DEBUG)
    logger.debug("test models")

    import models
# main()

if __name__ == '__main__':
    main()
