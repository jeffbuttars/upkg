from repo.base import RepoBase


class GithubRepo(RepoBase):

    def __init__(self):
        super(GithubRepo, self).__init__(api_ver=3, api_base_url='https://api.github.com')

        self._default_headers = {'Accept': "application/vnd.github.v{}".format(self._api_ver)}

        self._search_ep = {
            'method': 'GET',
            'ep': "/search/repositories"
        }
    #__init__()

    def search(self, term,
               s_in=None,
               size=None,
               forks=None,
               created=None,
               pushed=None,
               user=None,
               repo=None,
               language=None,
               stars=None,
               ):
        """todo: Docstring for search
        
        :param term: arg description
        :type term: type description
        :param s_in: arg description
        :type s_in: type description
        :param size: arg description
        :type size: type description
        :param forks: arg description
        :type forks: type description
        :param created: arg description
        :type created: type description
        :param pushed: arg description
        :type pushed: type description
        :param user: arg description
        :type user: type description
        :param repo: arg description
        :type repo: type description
        :param language: arg description
        :type language: type description
        :param stars: arg description
        :type stars: type description
        :param ):: arg description
        :type ):: type description
        :return:
        :rtype:
        """

        pass
    #search()
#GithubRepo
