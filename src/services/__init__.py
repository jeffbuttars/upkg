import os
import importlib
import glob


_services = set()


def get_services():
    """todo: Docstring for get_services
    :return:
    :rtype:
    """

    return _services
#get_services()


def upkg_service(cl):
    """todo: Docstring for register_service

    :param cl: arg description
    :type cl: type description
    :return:
    :rtype:
    """

    _services.add(cl)
    return cl
#upkg_service()


def register_services():
    _this_dir = os.path.realpath(os.path.dirname(__file__))
    _this_mod = os.path.basename(_this_dir)

    service_mods = {}
    imlist = glob.glob(os.path.join("services", "*.py"))
    imlist.remove(os.path.join("services", "__init__.py"))
    # imlist.remove(os.path.join("services", "base.py"))
    # print(imlist)

    imlist = [os.path.basename(x) for x in imlist]
    imlist = [os.path.splitext(x)[0] for x in imlist]

    # s = importlib.import_module('cmds.search')
    # print(s.Cmd.name)

    for im in imlist:
        # print(im)
        importlib.import_module(_this_mod + '.' + im)
        # mod = importlib.import_module(_this_mod + '.' + im)
        # if hasattr(mod, 'Cmd'):
        #     # print("Found Command: ", mod.Cmd.name)
        #     cmd_objs[mod.Cmd.name] = mod.Cmd(sub_parser)
        #     cmd_objs[mod.Cmd.name].build()
    # end for im in imlist
    # print(cmd_objs)

    return service_mods
#register_services()
