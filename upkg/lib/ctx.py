import logging
logger = logging.getLogger('upkg')

_CTX = None


class UpkgCtx(object):

    def __init__(self):
        """todo: to be defined """
        self._deps = {}
        self._installed = {}
    #__init__()

    def add_dep(self, name, dep):
        """todo: Docstring for add_dep

        :param name: arg description
        :type name: type description
        :param dep: arg description
        :type dep: type description
        :return:
        :rtype:
        """
        logger.debug("name: %s, dep: %s", name, dep)

        if dep not in self._deps:
            self._deps[name] = dep
    #add_dep()

    @property
    def deps(self):
        return self._deps

    @property
    def deps_needed(self):
        needed = []
        for k in self._deps:
            try:
                if k not in self._installed:
                    needed.append(self._deps[k])
            except KeyError:
                pass
        return needed

    def dep(self, name):
        return self._deps[name]

    def installed(self, name):
        """todo: Docstring for installed

        :param name: arg description
        :type name: type description
        :return:
        :rtype:
        """
        logger.debug("name: %s", name)

        self._installed[name] = True
        return name
    #installed()
#UpkgCtx


def get_ctx():
    """todo: Docstring for get_ctx
    :return:
    :rtype:
    """
    return _CTX or UpkgCtx()
#get_ctx()
