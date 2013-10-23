import os
import inspect
from argparse import Namespace
from importlib.machinery import SourceFileLoader


# Set config defaults
_config = {
    # Default path to config file.
    "cfg_path": "~/.config/pkgs/pkgs_cfg.py",

    # The install destination directory
    'pkgs_destdir': '~/.pkgs',

    # Require the user to have root access to use pkgs
    'require_root': False,
}

settings = None


def _clean_path(p):
    """todo: Docstring for _clen_path

    :param p: arg description
    :type p: type description
    :return:
    :rtype:
    """

    np = os.path.expanduser(p)
    np = os.path.abspath(np)

    return np
#_clean_path()


def load_settings(cfg_path=None):
    """todo: Docstring for load_settings

    :param cfg_path: arg description
    :type cfg_path: type description
    :return:
    :rtype:
    """

    global settings

    cfg_path = cfg_path or _config['cfg_path']

    cfg_d = _config.copy()

    if os.path.exists(cfg_path):
        sfl = SourceFileLoader('pkgs_cfg', cfg_path)
        cfg_mod = sfl.load_module()

        for m in inspect.getmembers(cfg_mod):
            if m[0][0] != '_':
                cfg_d[m[0]] = m[1]
        # end for m in inspect.getme

    # Make the paths absolute.
    cfg_d["cfg_path"] = _clean_path(cfg_d["cfg_path"])
    cfg_d["pkgs_destdir"] = _clean_path(cfg_d["pkgs_destdir"])

    settings = Namespace(**cfg_d)
#load_settings()
