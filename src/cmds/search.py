import logging
logger = logging.getLogger('upkg')

from cmds.base import BaseCmd
import lib
import services


class Cmd(BaseCmd):
    """Docstring for Search """

    name = 'search'
    help_text = ("search repos for a package")
    aliases = ['s', 'se', 'sea', 'sear', 'searc']

    def build(self):
        """todo: Docstring for build
        :return:
        :rtype:
        """

        self._cmd_parser.add_argument(
            'search',
            type=str,
            default=None,
            nargs="+",
            help=("Search for a package/repo by name or by user/reponame"),
        )

        self._cmd_parser.add_argument(
            '-s',
            '--service',
            default=None,
            help=("Limit the search to a particular service ex: github")
        )

        self._cmd_parser.add_argument(
            '-u',
            '--user',
            default=None,
            help=("Limit the search to a username on the service(s) being searched.")
        )

        self._cmd_parser.add_argument(
            '-r',
            '--repo',
            default=None,
            help=("Limit the search to a specific repo.")
        )

        self._cmd_parser.add_argument(
            '-l',
            '--language',
            default=None,
            help=("Limit the search repos containing a specific language")
        )

        self._cmd_parser.add_argument(
            '-p',
            '--popularity',
            default=None,
            help=("Limit the search repos having at least a given popularity rating.")
        )

        self._cmd_parser.add_argument(
            '--created',
            default=None,
            help=("Limit the search repos based on when they were created. "
                  "the format of YYYY-MM-DD--that's year, followed by month, followed by day."
                  "You can"
                  "continue to use < to refer to \"before a date,\" and > as after a date. For"
                  "example:\n\n"
                  "webos created:<2011-01-01\n"
                  "Matches repositories with the word \"webos\" that were created before 2011\n"
                  "css pushed:<2013-02-01"
                  "Matches repositories with the word \"css\" that were pushed to "
                  "before February 2013"
                  "case pushed:>=2013-03-06 fork:only"
                  "Matches repositories with the word \"case\" that were pushed to on or "
                  "after March 6th, 2013, and that are forks"
                  )
        )

        self._cmd_parser.add_argument(
            '--push',
            default=None,
            help=("Limit the search repos based on when they were created. "
                  "the format of YYYY-MM-DD--that's year, followed by month, followed by day."
                  "You can"
                  "continue to use < to refer to \"before a date,\" and > as after a date. For"
                  "example:\n\n"
                  "webos created:<2011-01-01\n"
                  "Matches repositories with the word \"webos\" that were created before 2011\n"
                  "css pushed:<2013-02-01"
                  "Matches repositories with the word \"css\" that were pushed to "
                  "before February 2013"
                  "case pushed:>=2013-03-06 fork:only"
                  "Matches repositories with the word \"case\" that were pushed to on or "
                  "after March 6th, 2013, and that are forks"
                  )
        )

        self._cmd_parser.add_argument(
            '-a',
            '--available',
            default=False, action='store_true',
            help=("List the available services for upkg")
        )

        return super(Cmd, self).build()
    #build()

    def exec(self, args):
        """todo: Docstring for exec

        :param args: arg description
        :type args: type description
        :return:
        :rtype:
        """

        logger.debug("search, %s services available", len(services.get_services()))

        term = lib.Term()

        if args.available:
            term.pr_info("Available services:")
            for serv in services.get_services():
                servi = serv()
                term.pr_ok("\t{}", servi.name)
            return

        kwargs = {
            'user': args.user,
            'repo': args.repo,
            'lang': args.language,
            'pop': args.popularity,
        }

        results = []
        for serv in services.get_services():
            servi = serv()
            if args.service and args.service != servi.name:
                logger.debug("limiting service to %s, skipping service %s",
                             args.service, servi.name)
                continue

            logger.debug("searchin for %s in service %s", args.search, servi)
            results += servi.search(' '.join(args.search), **kwargs)
        # end for serv in lib.services

        padding = len(str(len(results)))
        i = 1
        for r in results:
            term.pr("{}] {} {}",
                    str(i).zfill(padding),
                    term.ok(r.name),
                    term.info(r.url),
                    )
            i += 1
        # end for r in results
    #exec()
# Cmd
