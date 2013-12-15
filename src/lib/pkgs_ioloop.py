import logging
logger = logging.getLogger('upkg')
# mailogger = logging.getLogger('upkg-maillogger')

import sys
# import smtplib
# from tornado.platform.epoll import EPollIOLoop
from tornado.ioloop import IOLoop


# class UpkgIOLoop(EPollIOLoop, object):
class UpkgIOLoop(IOLoop):
    """UpkgIOLoop
    """

   #  def initialize(self, **kwargs):
   #      """todo: Docstring for initialize

   #      :param **kwargs: arg description
   #      :type **kwargs: type description
   #      :return:
   #      :rtype:
   #      """
   #      super(UpkgIOLoop, self).initialize(**kwargs)
   # #initialize()

    def handle_callback_exception(self, callback):
        # We setup a Pokemon handler
        # to e-mail us when something
        # funky happens

        import traceback
        import socket
        import platform

        t, v, tr = sys.exc_info()
        estr = "IOLoop Excption\n"
        estr += "hostname: %s\n" % socket.gethostname()
        estr += "uname: %s\n" % ' '.join(platform.uname())
        estr += "Type: %s\n" % t
        estr += "Value: %s\n" % v
        estr += "Traceback: %s\n" % traceback.print_tb(tr)

        logger.error(estr, exc_info=True)
        # try:
        #     mailogger.exception(estr)
        # except smtplib.SMTPServerDisconnected:
        #     logger.error("Unable to mail exception")

        # for srv in self._services:
        #     srv.reset_timeout()
        # # end for srv in self._services

        # sys.exit(1)

        super(UpkgIOLoop, self).handle_callback_exception(callback)
    #handle_callback_exception()

    # def start(self):
    #     super(UpkgIOLoop, self).start()
    # #start()
#UpkgIOLoop
