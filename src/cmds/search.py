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

        results = []
        for serv in services.get_services():
            servi = serv()
            logger.debug("searchin for %s in service %s", args.search, servi)
            results += servi.search(' '.join(args.search))
        # end for serv in lib.services

        term = lib.Term()
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
