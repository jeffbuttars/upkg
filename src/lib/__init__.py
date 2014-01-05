import sys
from blessings import Terminal
from lib.repo import Repo


class Term(object):
    def __init__(self):
        self.term = Terminal()
    #__init__()

    def pr(self, fmt, *args, **kwargs):
        """todo: Docstring for pr

        :param arg1: arg description
        :type arg1: type description
        :return:
        :rtype:
        """
        print(str(fmt).format(*args, **kwargs))
    #pr()

    def pr_ok(self, fmt, *args, **kwargs):
        print(self.ok(fmt, *args, **kwargs))
    #pr_ok()

    def pr_info(self, fmt, *args, **kwargs):
        print(self.info(fmt, *args, **kwargs))
    #pr_info()

    def pr_fail(self, fmt, *args, **kwargs):
        print(self.fail(fmt, *args, **kwargs))
    #pr_fail()

    def pr_atten(self, fmt, *args, **kwargs):
        print(self.atten(fmt, *args, **kwargs))
    #pr_atten()

    def ok(self, fmt, *args, **kwargs):
        return self.green(fmt, *args, **kwargs)
    #ok()

    def info(self, fmt, *args, **kwargs):
        return self.blue(fmt, *args, **kwargs)
    #info()

    def fail(self, fmt, *args, **kwargs):
        return self.red(fmt, *args, **kwargs)
    #fail()

    def atten(self, fmt, *args, **kwargs):
        return self.red(fmt, *args, **kwargs)
    #atten()

    def c(self, color, fmt, *args, **kwargs):
        """todo: Docstring for c

        :param color: arg description
        :type color: type description
        :param text: arg description
        :type text: type description
        :return:
        :rtype:
        """

        fmt_s = str(fmt)

        if self.term.number_of_colors:
            fn = getattr(self.term, color)
            # logger.debug("color fun: %s, %s", fn, dir(fn))
            # print("color fun: %s, %s" % (fn, dir(fn)))
            return fn(fmt_s.format(*args, **kwargs))

        return fmt_s.format(*args, **kwargs)
    #c()

    def red(self, fmt, *args, **kwargs):
        """todo: Docstring for red

        :param fmt: arg description
        :type fmt: type description
        :param *args: arg description
        :type *args: type description
        :param **kwargs: arg description
        :type **kwargs: type description
        :return:
        :rtype:
        """
        return self.c('red', fmt, *args, **kwargs)
    #red()

    def green(self, fmt, *args, **kwargs):
        """todo: Docstring for green

        :param fmt: arg description
        :type fmt: type description
        :param *args: arg description
        :type *args: type description
        :param **kwargs: arg description
        :type **kwargs: type description
        :return:
        :rtype:
        """
        return self.c('green', fmt, *args, **kwargs)
    #green()

    def blue(self, fmt, *args, **kwargs):
        """todo: Docstring for blue

        :param fmt: arg description
        :type fmt: type description
        :param *args: arg description
        :type *args: type description
        :param **kwargs: arg description
        :type **kwargs: type description
        :return:
        :rtype:
        """
        return self.c('blue', fmt, *args, **kwargs)
    #blue()

    def _build_writer(self, output, color=None):

        if color:

            def _cwriter(fmt, *args, **kwargs):
                output(self.c(color, fmt.format(*args, **kwargs)))

            return _cwriter

        def _writer(fmt, *args, **kwargs):
            output(fmt.format(*args, **kwargs))

        return _writer
    #_build_writer()

    def c_stdout(self, color=None):
        return self._build_writer(sys.stdout.write, color=color)
    #c_stdout()

    def c_stderr(self, color=None):
        return self._build_writer(sys.stderr.write, color=color)
    #_stderr()
#Term
