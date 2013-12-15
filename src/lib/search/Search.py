import logging
logger = logging.getLogger('upkg')

# import dateutil
import dateutil.parser
import dateutil.relativedelta
import datetime
import json
import tornado.httpclient
# from tornado import gen


class Search(object):
    """Docstring for Search """

    def __init__(self, async=False):
        """todo: to be defined """

        self._headers = {
            'User-Agent': "https://github.com/jeffbuttars/upkg",
            'Accept': "application/vnd.github.preview",  # Acknowledge the dev API
        }

        # A list of prefered repos to give greater weight in a search
        # and are searched first.
        self._prefered = None

        self._hc = tornado.httpclient.HTTPClient()
        # # self._ahc = tornado.httpclient.AsyncHTTPClient()

        self._gh_url_base = "https://api.github.com/search/repositories?per_page=100&q="
        self._last_result = None
    #__init__()

    def __call__(self, term, cb=None):
        """todo: Docstring for __call__

        :param term: arg description
        :type term: type description
        :return:
        :rtype:
        """

        logger.debug("term: %s, cb: %s", term, cb)

        if not term:
            return term

        url = self._gh_url_base + str(term)
        future = self._hc.fetch(url, method="GET", headers=self._headers)

        if future.code != 200:
            estr = "Error while search for {}\nerror code: {}, {}\n{}".format(
                term, future.code, future.error, future.body
            )
            raise Exception(estr)

        self._last_result = json.loads(future.body)
        return self._last_result
    #__call__()

    def __str__(self, res=None):
        """todo: Docstring for __str__

        :param res: arg description
        :type res: type description
        :return:
        :rtype:
        """

        res = res or self._last_result
        items = res['items']
        total_count = res['total_count']

        summary = "Showing {} of {} found items:\n".format(len(items), total_count)
        out = summary

        i = 1
        for item in items:
            # 2013-10-10T10:26:32Z
            # lu = datetime.datetime.strptime(item['updated_at'], '%Y-%m-%dT%H:%M:%SZ')
            # lu = datetime.datetime.strptime(item['updated_at'], '%Y-%m-%dT%H:%M:%SZ')

            # Strip the timezone, treat all time as UTC
            # td = self._fmt_tdelta(datetime.datetime.now() - lu)
            td = self._fmt_tdelta(dateutil.parser.parse(item['updated_at'][:-1]))

            fargs = {
                'url': item['url'].replace(
                    'https://api.github.com/repos/', '', 1
                ),
                'private': '\033[92mPublic\033[0m',
                'updated': '\033[93m' + td + '\033[0m',
                'description': item['description'].encode('ascii', 'ignore'),
            }

            if not fargs['private']:
                fargs['private'] = '\033[91mPrivate\033[0m',

            out += ('\033[94m' + str(i) + '\033[0m {url}\n\t'
                    "{description}\n\t"
                    "Last Update {updated}\n\t"
                    "Access: {private}\n\n").format(**fargs)
            i += 1
        # end for item in items

        out += summary
        return out
    #__str__()

    def _fmt_tdelta(self, td):
        """todo: Docstring for _fmt_tdelta

        :param td: arg description
        :type td: type description
        :return:
        :rtype:
        """

        rel = dateutil.relativedelta.relativedelta(datetime.datetime.utcnow(), td)

        if rel.years:
            return "{} Years and {} Months Ago".format(rel.years, rel.months)
        if rel.months:
            return "{} Months Ago".format(rel.months)
        if rel.days:
            return "{} Days Ago".format(rel.days)
        if rel.hours:
            return "{} Hours Ago".format(rel.hours)

        return "{} Minutes Ago".format(rel.minutes)
    #_fmt_tdelta()
#Search

"""
 {
      "archive_url": "https://api.github.com/repos/benfoster/Fabrik.Common/{archive_format}{/ref}", 
      "assignees_url": "https://api.github.com/repos/benfoster/Fabrik.Common/assignees{/user}", 
      "blobs_url": "https://api.github.com/repos/benfoster/Fabrik.Common/git/blobs{/sha}", 
      "branches_url": "https://api.github.com/repos/benfoster/Fabrik.Common/branches{/branch}", 
      "clone_url": "https://github.com/benfoster/Fabrik.Common.git", 
      "collaborators_url": "https://api.github.com/repos/benfoster/Fabrik.Common/collaborators{/collaborator}", 
      "comments_url": "https://api.github.com/repos/benfoster/Fabrik.Common/comments{/number}", 
      "commits_url": "https://api.github.com/repos/benfoster/Fabrik.Common/commits{/sha}", 
      "compare_url": "https://api.github.com/repos/benfoster/Fabrik.Common/compare/{base}...{head}", 
      "contents_url": "https://api.github.com/repos/benfoster/Fabrik.Common/contents/{+path}", 
      "contributors_url": "https://api.github.com/repos/benfoster/Fabrik.Common/contributors", 
      "created_at": "2012-07-05T13:34:05Z", 
      "default_branch": "master", 
      "description": "Useful stuff from fabrik", 
      "downloads_url": "https://api.github.com/repos/benfoster/Fabrik.Common/downloads", 
      "events_url": "https://api.github.com/repos/benfoster/Fabrik.Common/events", 
      "fork": false, 
      "forks": 23, 
      "forks_count": 23, 
      "forks_url": "https://api.github.com/repos/benfoster/Fabrik.Common/forks", 
      "full_name": "benfoster/Fabrik.Common", 
      "git_commits_url": "https://api.github.com/repos/benfoster/Fabrik.Common/git/commits{/sha}", 
      "git_refs_url": "https://api.github.com/repos/benfoster/Fabrik.Common/git/refs{/sha}", 
      "git_tags_url": "https://api.github.com/repos/benfoster/Fabrik.Common/git/tags{/sha}", 
      "git_url": "git://github.com/benfoster/Fabrik.Common.git", 
      "has_downloads": true, 
      "has_issues": true, 
      "has_wiki": true, 
      "homepage": null, 
      "hooks_url": "https://api.github.com/repos/benfoster/Fabrik.Common/hooks", 
      "html_url": "https://github.com/benfoster/Fabrik.Common", 
      "id": 4906940, 
      "issue_comment_url": "https://api.github.com/repos/benfoster/Fabrik.Common/issues/comments/{number}", 
      "issue_events_url": "https://api.github.com/repos/benfoster/Fabrik.Common/issues/events{/number}", 
      "issues_url": "https://api.github.com/repos/benfoster/Fabrik.Common/issues{/number}", 
      "keys_url": "https://api.github.com/repos/benfoster/Fabrik.Common/keys{/key_id}", 
      "labels_url": "https://api.github.com/repos/benfoster/Fabrik.Common/labels{/name}", 
      "language": "C#", 
      "languages_url": "https://api.github.com/repos/benfoster/Fabrik.Common/languages", 
      "master_branch": "master", 
      "merges_url": "https://api.github.com/repos/benfoster/Fabrik.Common/merges", 
      "milestones_url": "https://api.github.com/repos/benfoster/Fabrik.Common/milestones{/number}", 
      "mirror_url": null, 
      "name": "Fabrik.Common", 
      "notifications_url": "https://api.github.com/repos/benfoster/Fabrik.Common/notifications{?since,all,participating}", 
      "open_issues": 9, 
      "open_issues_count": 9, 
      "owner": {
        "avatar_url": "https://2.gravatar.com/avatar/3192eeb39449a86afa994fa9efc83179?d=https%3A%2F%2Fidenticons.github.com%2F061cdd38a3f82458730d861a54852ec7.png", 
        "events_url": "https://api.github.com/users/benfoster/events{/privacy}", 
        "followers_url": "https://api.github.com/users/benfoster/followers", 
        "following_url": "https://api.github.com/users/benfoster/following{/other_user}", 
        "gists_url": "https://api.github.com/users/benfoster/gists{/gist_id}", 
        "gravatar_id": "3192eeb39449a86afa994fa9efc83179", 
        "html_url": "https://github.com/benfoster", 
        "id": 827305, 
        "login": "benfoster", 
        "organizations_url": "https://api.github.com/users/benfoster/orgs", 
        "received_events_url": "https://api.github.com/users/benfoster/received_events", 
        "repos_url": "https://api.github.com/users/benfoster/repos", 
        "site_admin": false, 
        "starred_url": "https://api.github.com/users/benfoster/starred{/owner}{/repo}", 
        "subscriptions_url": "https://api.github.com/users/benfoster/subscriptions", 
        "type": "User", 
        "url": "https://api.github.com/users/benfoster"
      }, 
      "private": false, 
      "pulls_url": "https://api.github.com/repos/benfoster/Fabrik.Common/pulls{/number}", 
      "pushed_at": "2013-07-25T15:36:55Z", 
      "score": 13.695881, 
      "size": 4625, 
      "ssh_url": "git@github.com:benfoster/Fabrik.Common.git", 
      "stargazers_url": "https://api.github.com/repos/benfoster/Fabrik.Common/stargazers", 
      "statuses_url": "https://api.github.com/repos/benfoster/Fabrik.Common/statuses/{sha}", 
      "subscribers_url": "https://api.github.com/repos/benfoster/Fabrik.Common/subscribers", 
      "subscription_url": "https://api.github.com/repos/benfoster/Fabrik.Common/subscription", 
      "svn_url": "https://github.com/benfoster/Fabrik.Common", 
      "tags_url": "https://api.github.com/repos/benfoster/Fabrik.Common/tags", 
      "teams_url": "https://api.github.com/repos/benfoster/Fabrik.Common/teams", 
      "trees_url": "https://api.github.com/repos/benfoster/Fabrik.Common/git/trees{/sha}", 
      "updated_at": "2013-10-15T04:02:40Z", 
      "url": "https://api.github.com/repos/benfoster/Fabrik.Common", 
      "watchers": 57, 
      "watchers_count": 57
    }
"""
