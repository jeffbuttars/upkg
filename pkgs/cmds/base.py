
class BaseCmd(object):
    """Docstring for Search """

    name = 'search'

    def __init__(self, sub_parser):
        """todo: to be defined

        :param sub_parser: arg description
        :type sub_parser: type description
        """
        self._sub_parser = sub_parser
        self._cmd_parser = None
    #__init__()

    def build(self):
        self._cmd_parser.set_defaults(func=self.exec)
        return self._cmd_parser
    #build()

    def exec(self, args):
        print(args)
    #exec()
# BaseCmd
