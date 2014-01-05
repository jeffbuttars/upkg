import logging
logger = logging.getLogger('upkg')

import os
import time
import datetime
import urllib.parse
import tornado.httpclient

from services.base import ServiceBase, ServiceResponse
import services


class GihubResponse(ServiceResponse):

    def __init__(self, service, resp_dict):
        super(GihubResponse, self).__init__(service, resp_dict)
        self.url = self.git_url
    #__init__()

    def __repr__(self):
        """todo: Docstring for __repr__
        :return:
        :rtype:
        """

        return self.__str__()
    #__repr__()
#GihubResponse


@services.upkg_service
class GithubService(ServiceBase):

    name = 'github'
    description = "It's GitHub! https://github.com"

    def __init__(self):
        super(GithubService, self).__init__(api_ver=3, api_base_url='https://api.github.com')

        self._default_headers = {
            'Accept': "application/vnd.github.v{}".format(self._api_ver),
            'User-Agent': 'upkg-package-yourself',
        }

        self._search_ep = {
            'method': 'GET',
            'ep': "/search/repositories"
        }

        self._default_params = {
            'per_page': 100,
        }
    #__init__()

    def add_search_qual(self, term, qname, quals):
        """todo: Docstring for add_search_qual

        :param term: arg description
        :type term: type description
        :param quals: arg description
        :type quals: type description
        :return:
        :rtype:
        """

        logger.debug("term: %s, qname: %s, quals: %s",
                     term, qname, quals)

        if not quals:
            return term

        return "{}+{}:{}".format(term, qname, quals)
    #add_search_qual()

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
               lang=None,
               pop=None,
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
        logger.debug(("github search for '%s' "
                      "sort: %s"
                      "order: %s"
                      "s_in: %s"
                      "size: %s"
                      "forks: %s"
                      "created: %s"
                      "pushed: %s"
                      "user: %s"
                      "repo: %s"
                      "lang: %s"
                      "pop: %s"
                     ),
                     term,
                     sort,
                     order,
                     s_in,
                     size,
                     forks,
                     created,
                     pushed,
                     user,
                     repo,
                     lang,
                     pop,
                    )

        orig_term = term
        term = urllib.parse.quote_plus(term)
        s_order = order or 'desc'
        if s_order not in ('asc', 'desc'):
            s_order = order or 'desc'

        if sort:
            if sort not in ('stars', 'forks', 'updated'):
                sort = ''

        term = self.add_search_qual(term, 's_in', s_in)
        term = self.add_search_qual(term, 'size', size)
        term = self.add_search_qual(term, 'forks', forks)
        term = self.add_search_qual(term, 'created', created)
        term = self.add_search_qual(term, 'pushed', pushed)
        term = self.add_search_qual(term, 'user', user)
        term = self.add_search_qual(term, 'repo', repo)
        term = self.add_search_qual(term, 'language', lang)
        term = self.add_search_qual(term, 'stars', pop)

        ep = os.path.join("search", "repositories")
        params = self._default_params.copy()
        params['q'] = term

        try:
            resp_obj, resp = self.get_json(ep, params=params)

            limit = resp.headers.get('X-RateLimit-Limit', '')
            remaining = resp.headers.get('X-RateLimit-Remaining', '')
            limit_reset = resp.headers.get('X-RateLimit-Reset', '')
            l_res = datetime.datetime.strptime(
                time.ctime(
                    int(limit_reset)), "%a %b %d %H:%M:%S %Y")
            now = datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")

            self.term.pr_info("API Request Limit, {} of {} Remaining, Resets in {} seconds\n",
                              remaining, limit, (l_res - now).seconds)

        except tornado.httpclient.HTTPError as e:
            if e.code == 422:
                self.term.pr_fail("Search for '{}' returned no results", orig_term)

            return []

        return [GihubResponse(self, x) for x in resp_obj['items']]
    #search()
#GithubService


def main():
    import sys
    logger.setLevel(logging.DEBUG)

    this_dir = os.path.realpath(os.path.dirname(__file__))
    p_dir = os.path.dirname(this_dir)
    sys.path.append(p_dir)

    from lib import Term
    term = Term()
    gh = GithubService()
    resp = gh.search("upkg")

    for r in resp:
        print(term.blue(r))
    # end for r in resp

# main()

if __name__ == '__main__':
    main()


# {'items': [{'archive_url': 'https://api.github.com/repos/schwer-q/upkg/{archive_format}{/ref}',
#             'assignees_url': 'https://api.github.com/repos/schwer-q/upkg/assignees{/user}',
#             'blobs_url': 'https://api.github.com/repos/schwer-q/upkg/git/blobs{/sha}',
#             'branches_url': 'https://api.github.com/repos/schwer-q/upkg/branches{/branch}',
#             'clone_url': 'https://github.com/schwer-q/upkg.git',
#             'collaborators_url': 'https://api.github.com/repos/schwer-q/upkg/collaborators{/collaborator}',
#             'comments_url': 'https://api.github.com/repos/schwer-q/upkg/comments{/number}',
#             'commits_url': 'https://api.github.com/repos/schwer-q/upkg/commits{/sha}',
#             'compare_url': 'https://api.github.com/repos/schwer-q/upkg/compare/{base}...{head}',
#             'contents_url': 'https://api.github.com/repos/schwer-q/upkg/contents/{+path}',
#             'contributors_url': 'https://api.github.com/repos/schwer-q/upkg/contributors',
#             'created_at': '2013-12-09T16:40:25Z',
#             'default_branch': 'master',
#             'description': 'Micro Package Manager',
#             'downloads_url': 'https://api.github.com/repos/schwer-q/upkg/downloads',
#             'events_url': 'https://api.github.com/repos/schwer-q/upkg/events',
#             'fork': False,
#             'forks': 0,
#             'forks_count': 0,
#             'forks_url': 'https://api.github.com/repos/schwer-q/upkg/forks',
#             'full_name': 'schwer-q/upkg',
#             'git_commits_url': 'https://api.github.com/repos/schwer-q/upkg/git/commits{/sha}',
#             'git_refs_url': 'https://api.github.com/repos/schwer-q/upkg/git/refs{/sha}',
#             'git_tags_url': 'https://api.github.com/repos/schwer-q/upkg/git/tags{/sha}',
#             'git_url': 'git://github.com/schwer-q/upkg.git',
#             'has_downloads': True,
#             'has_issues': True,
#             'has_wiki': True,
#             'homepage': None,
#             'hooks_url': 'https://api.github.com/repos/schwer-q/upkg/hooks',
#             'html_url': 'https://github.com/schwer-q/upkg',
#             'id': 15052866,
#             'issue_comment_url': 'https://api.github.com/repos/schwer-q/upkg/issues/comments/{number}',
#             'issue_events_url': 'https://api.github.com/repos/schwer-q/upkg/issues/events{/number}',
#             'issues_url': 'https://api.github.com/repos/schwer-q/upkg/issues{/number}',
#             'keys_url': 'https://api.github.com/repos/schwer-q/upkg/keys{/key_id}',
#             'labels_url': 'https://api.github.com/repos/schwer-q/upkg/labels{/name}',
#             'language': 'Shell',
#             'languages_url': 'https://api.github.com/repos/schwer-q/upkg/languages',
#             'master_branch': 'master',
#             'merges_url': 'https://api.github.com/repos/schwer-q/upkg/merges',
#             'milestones_url': 'https://api.github.com/repos/schwer-q/upkg/milestones{/number}',
#             'mirror_url': None,
#             'name': 'upkg',
#             'notifications_url': 'https://api.github.com/repos/schwer-q/upkg/notifications{?since,all,participating}',
#             'open_issues': 0,
#             'open_issues_count': 0,
#             'owner': {'avatar_url': 'https://gravatar.com/avatar/76d607e390feb9df28dbb299f7db5dc4?d=https%3A%2F%2Fidenticons.github.com%2F3793a695ed4da8bb87b97a59d6729395.png&r=x',
#                       'events_url': 'https://api.github.com/users/schwer-q/events{/privacy}',
#                       'followers_url': 'https://api.github.com/users/schwer-q/followers',
#                       'following_url': 'https://api.github.com/users/schwer-q/following{/other_user}',
#                       'gists_url': 'https://api.github.com/users/schwer-q/gists{/gist_id}',
#                       'gravatar_id': '76d607e390feb9df28dbb299f7db5dc4',
#                       'html_url': 'https://github.com/schwer-q',
#                       'id': 4136815,
#                       'login': 'schwer-q',
#                       'organizations_url': 'https://api.github.com/users/schwer-q/orgs',
#                       'received_events_url': 'https://api.github.com/users/schwer-q/received_events',
#                       'repos_url': 'https://api.github.com/users/schwer-q/repos',
#                       'site_admin': False,
#                       'starred_url': 'https://api.github.com/users/schwer-q/starred{/owner}{/repo}',
#                       'subscriptions_url': 'https://api.github.com/users/schwer-q/subscriptions',
#                       'type': 'User',
#                       'url': 'https://api.github.com/users/schwer-q'},
#             'private': False,
#             'pulls_url': 'https://api.github.com/repos/schwer-q/upkg/pulls{/number}',
#             'pushed_at': '2013-12-17T08:45:13Z',
#             'releases_url': 'https://api.github.com/repos/schwer-q/upkg/releases{/id}',
#             'score': 16.724836,
#             'size': 152,
#             'ssh_url': 'git@github.com:schwer-q/upkg.git',
#             'stargazers_count': 0,
#             'stargazers_url': 'https://api.github.com/repos/schwer-q/upkg/stargazers',
#             'statuses_url': 'https://api.github.com/repos/schwer-q/upkg/statuses/{sha}',
#             'subscribers_url': 'https://api.github.com/repos/schwer-q/upkg/subscribers',
#             'subscription_url': 'https://api.github.com/repos/schwer-q/upkg/subscription',
#             'svn_url': 'https://github.com/schwer-q/upkg',
#             'tags_url': 'https://api.github.com/repos/schwer-q/upkg/tags',
#             'teams_url': 'https://api.github.com/repos/schwer-q/upkg/teams',
#             'trees_url': 'https://api.github.com/repos/schwer-q/upkg/git/trees{/sha}',
#             'updated_at': '2013-12-17T08:45:17Z',
#             'url': 'https://api.github.com/repos/schwer-q/upkg',
#             'watchers': 0,
#             'watchers_count': 0},
#            {'archive_url': 'https://api.github.com/repos/jeffbuttars/upkg/{archive_format}{/ref}',
#             'assignees_url': 'https://api.github.com/repos/jeffbuttars/upkg/assignees{/user}',
#             'blobs_url': 'https://api.github.com/repos/jeffbuttars/upkg/git/blobs{/sha}',
#             'branches_url': 'https://api.github.com/repos/jeffbuttars/upkg/branches{/branch}',
#             'clone_url': 'https://github.com/jeffbuttars/upkg.git',
#             'collaborators_url': 'https://api.github.com/repos/jeffbuttars/upkg/collaborators{/collaborator}',
#             'comments_url': 'https://api.github.com/repos/jeffbuttars/upkg/comments{/number}',
#             'commits_url': 'https://api.github.com/repos/jeffbuttars/upkg/commits{/sha}',
#             'compare_url': 'https://api.github.com/repos/jeffbuttars/upkg/compare/{base}...{head}',
#             'contents_url': 'https://api.github.com/repos/jeffbuttars/upkg/contents/{+path}',
#             'contributors_url': 'https://api.github.com/repos/jeffbuttars/upkg/contributors',
#             'created_at': '2013-12-15T01:27:42Z',
#             'default_branch': 'master',
#             'description': "Package Yourself, a tool to help you manage repos of your personal 'scripts' like they're packages.",
#             'downloads_url': 'https://api.github.com/repos/jeffbuttars/upkg/downloads',
#             'events_url': 'https://api.github.com/repos/jeffbuttars/upkg/events',
#             'fork': False,
#             'forks': 0,
#             'forks_count': 0,
#             'forks_url': 'https://api.github.com/repos/jeffbuttars/upkg/forks',
#             'full_name': 'jeffbuttars/upkg',
#             'git_commits_url': 'https://api.github.com/repos/jeffbuttars/upkg/git/commits{/sha}',
#             'git_refs_url': 'https://api.github.com/repos/jeffbuttars/upkg/git/refs{/sha}',
#             'git_tags_url': 'https://api.github.com/repos/jeffbuttars/upkg/git/tags{/sha}',
#             'git_url': 'git://github.com/jeffbuttars/upkg.git',
#             'has_downloads': True,
#             'has_issues': True,
#             'has_wiki': True,
#             'homepage': None,
#             'hooks_url': 'https://api.github.com/repos/jeffbuttars/upkg/hooks',
#             'html_url': 'https://github.com/jeffbuttars/upkg',
#             'id': 15195886,
#             'issue_comment_url': 'https://api.github.com/repos/jeffbuttars/upkg/issues/comments/{number}',
#             'issue_events_url': 'https://api.github.com/repos/jeffbuttars/upkg/issues/events{/number}',
#             'issues_url': 'https://api.github.com/repos/jeffbuttars/upkg/issues{/number}',
#             'keys_url': 'https://api.github.com/repos/jeffbuttars/upkg/keys{/key_id}',
#             'labels_url': 'https://api.github.com/repos/jeffbuttars/upkg/labels{/name}',
#             'language': 'Python',
#             'languages_url': 'https://api.github.com/repos/jeffbuttars/upkg/languages',
#             'master_branch': 'master',
#             'merges_url': 'https://api.github.com/repos/jeffbuttars/upkg/merges',
#             'milestones_url': 'https://api.github.com/repos/jeffbuttars/upkg/milestones{/number}',
#             'mirror_url': None,
#             'name': 'upkg',
#             'notifications_url': 'https://api.github.com/repos/jeffbuttars/upkg/notifications{?since,all,participating}',
#             'open_issues': 0,
#             'open_issues_count': 0,
#             'owner': {'avatar_url': 'https://gravatar.com/avatar/353ea17fb853090ec7fb018a33d14baf?d=https%3A%2F%2Fidenticons.github.com%2F67bdcdefca5c409af0237b7a4bdf4819.png&r=x',
#                       'events_url': 'https://api.github.com/users/jeffbuttars/events{/privacy}',
#                       'followers_url': 'https://api.github.com/users/jeffbuttars/followers',
#                       'following_url': 'https://api.github.com/users/jeffbuttars/following{/other_user}',
#                       'gists_url': 'https://api.github.com/users/jeffbuttars/gists{/gist_id}',
#                       'gravatar_id': '353ea17fb853090ec7fb018a33d14baf',
#                       'html_url': 'https://github.com/jeffbuttars',
#                       'id': 1286887,
#                       'login': 'jeffbuttars',
#                       'organizations_url': 'https://api.github.com/users/jeffbuttars/orgs',
#                       'received_events_url': 'https://api.github.com/users/jeffbuttars/received_events',
#                       'repos_url': 'https://api.github.com/users/jeffbuttars/repos',
#                       'site_admin': False,
#                       'starred_url': 'https://api.github.com/users/jeffbuttars/starred{/owner}{/repo}',
#                       'subscriptions_url': 'https://api.github.com/users/jeffbuttars/subscriptions',
#                       'type': 'User',
#                       'url': 'https://api.github.com/users/jeffbuttars'},
#             'private': False,
#             'pulls_url': 'https://api.github.com/repos/jeffbuttars/upkg/pulls{/number}',
#             'pushed_at': '2014-01-04T01:57:54Z',
#             'releases_url': 'https://api.github.com/repos/jeffbuttars/upkg/releases{/id}',
#             'score': 16.724836,
#             'size': 240,
#             'ssh_url': 'git@github.com:jeffbuttars/upkg.git',
#             'stargazers_count': 0,
#             'stargazers_url': 'https://api.github.com/repos/jeffbuttars/upkg/stargazers',
#             'statuses_url': 'https://api.github.com/repos/jeffbuttars/upkg/statuses/{sha}',
#             'subscribers_url': 'https://api.github.com/repos/jeffbuttars/upkg/subscribers',
#             'subscription_url': 'https://api.github.com/repos/jeffbuttars/upkg/subscription',
#             'svn_url': 'https://github.com/jeffbuttars/upkg',
#             'tags_url': 'https://api.github.com/repos/jeffbuttars/upkg/tags',
#             'teams_url': 'https://api.github.com/repos/jeffbuttars/upkg/teams',
#             'trees_url': 'https://api.github.com/repos/jeffbuttars/upkg/git/trees{/sha}',
#             'updated_at': '2014-01-04T01:57:55Z',
#             'url': 'https://api.github.com/repos/jeffbuttars/upkg',
#             'watchers': 0,
#             'watchers_count': 0}],
#  'total_count': 2}
