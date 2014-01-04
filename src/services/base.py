
class RepoBase(object):

    api_ver = '1'
    api_base_url = 'https://example.com/api/v' + api_ver

    def __init__(self, api_ver=None, api_base_url=None):
        """todo: to be defined

        :param api_ver: arg description
        :type api_ver: type description
        :param api_base_url: arg description
        :type api_base_url: type description
        """
        self._api_ver = api_ver or ''
        self._api_base_url = api_base_url or ''
    #__init__()

    def search(self, term):
        """todo: Docstring for search

        :param term: arg description
        :type term: type description
        :return:
        :rtype:
        """

        pass
    #search()
#RepoBase
