import logging
logger = logging.getLogger('upkg')

import os
import urllib.parse

from base import RepoBase


class GithubRepo(RepoBase):

    name = 'github'
    description = "It's GitHub! https://github.com"

    def __init__(self):
        super(GithubRepo, self).__init__(api_ver=3, api_base_url='https://api.github.com')

        self._default_headers = {
            'Accept': "application/vnd.github.v{}".format(self._api_ver),
            'User-Agent': 'upkg-package-yourself',
        }

        self._search_ep = {
            'method': 'GET',
            'ep': "/search/repositories"
        }
    #__init__()

    def search(self, term,
               sort=None,
               order=None,
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
        logger.debug("github search for '%s'", term)

        s_order = order or 'desc'
        if s_order not in ('asc', 'desc'):
            s_order = order or 'desc'

        if sort:
            if sort not in ('stars', 'forks', 'updated'):
                sort = ''

        ep = os.path.join("search", "repositories")
        params = {
            'q': urllib.parse.quote_plus(term),
        }

        return self.get_json(ep, params=params)
    #search()
#GithubRepo


def main():
    import logging
    logger.setLevel(logging.DEBUG)

    from pprint import pformat as pf
    gh = GithubRepo()
    resp = gh.search("upkg")

    print(pf(resp))
# main()

if __name__ == '__main__':
    main()
