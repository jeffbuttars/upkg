

class Install(object):
    """Docstring for Install """

    # def __init__(self):
    #     """todo: to be defined """
    #     pass    
    # #__init__()

    def __call__(self, *args):
        """todo: Docstring for __call__

        :param *args: arg description
        :type *args: type description
        :return:
        :rtype:
        """

        for pkg in args:
            self.install(pkg)
        # end for pkg in args
    #__call__()

    def install(self, pkg_url):
        """todo: Docstring for install

        :param pkg_url: arg description
        :type pkg_url: type description
        :return:
        :rtype:
        """

        pass
    #install()
#Install
