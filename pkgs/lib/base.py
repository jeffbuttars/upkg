import logging
logger = logging.getLogger('pkgs')

import os
from conf import settings


ugly_ext = ('.git', '.hg')


def nice_pkg_name(name):
    """todo: Docstring for nice_pkg_name

    :param name: arg description
    :type name: type description
    :return:
    :rtype:
    """
    logger.debug("%s", name)

    root, ext = os.path.splitext(name)

    if ext in ugly_ext:
        return root

    return name
#nice_pkg_name()


def pkg_name_to_path(pkgname):
    """todo: Docstring for pkg_name_to_path

    :param pkgname: arg description
    :type pkgname: type description
    :return:
    :rtype:
    """

    logger.debug("'%s'", pkgname)

    dlist = os.listdir(settings.pkgs_destdir)

    for d in dlist:
        fp = os.path.join(settings.pkgs_destdir, d)
        # logger.debug("checking if %s", fp)
        if not os.path.isdir(fp):
            # logger.debug("moving on")
            continue

        if pkgname == d:
            # logger.debug("match")
            return fp

        if d.startswith(pkgname):
            # logger.debug("startwith")
            root, ext = os.path.splitext(d)
            if pkgname == root:
                return fp
    # end for d in dlist

    return None
#pkg_name_to_path()


def did_u_mean(name):
    """todo: Docstring for did_u_mean

    :param name: arg description
    :type name: type description
    :return:
    :rtype:
    """
    logger.debug("%s", name)

    dlist = os.listdir(settings.pkgs_destdir)
    res = []
    for d in dlist:
        if name in d or d in name:
            res.append(nice_pkg_name(d))
    # end for d in dlist

    if res:
        return "Did you mean '" + " or ".join(res) + "'?"

    return ""
#did_u_mean()
