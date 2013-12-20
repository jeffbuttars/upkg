import os
import uuid
import inspect
from argparse import Namespace
from importlib.machinery import SourceFileLoader


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


# Set config defaults
_config = {

    "ctx_id": str(uuid.uuid4()),
    "cfg_dir_path": _clean_path("~/.config/upkg"),
    # Default path to config file.
    "cfg_file_path": _clean_path("~/.config/upkg/upkg_cfg.py"),

    # State and history database
    "dbs_path": _clean_path("~/.config/upkg/db"),
    "db_name": "upkg",

    # The install destination directory
    'upkg_destdir': _clean_path('~/.upkg'),

    # Require the user to have root access to use upkg
    'require_root': False,
}


settings = Namespace(**_config)


def load_settings(cfg_file_path=None):
    """todo: Docstring for load_settings

    :param cfg_file_path: arg description
    :type cfg_file_path: type description
    :return:
    :rtype:
    """

    global settings

    cfg_file_path = cfg_file_path or _config['cfg_file_path']

    cfg_d = _config.copy()

    if os.path.exists(cfg_file_path):
        sfl = SourceFileLoader('upkg_cfg', cfg_file_path)
        cfg_mod = sfl.load_module()

        for m in inspect.getmembers(cfg_mod):
            if m[0][0] != '_':
                cfg_d[m[0]] = m[1]
        # end for m in inspect.getme

    # Make the paths absolute.
    cfg_d["cfg_file_path"] = _clean_path(cfg_d["cfg_file_path"])
    cfg_d["upkg_destdir"] = _clean_path(cfg_d["upkg_destdir"])

    settings = Namespace(**cfg_d)

    return settings
#load_settings()
