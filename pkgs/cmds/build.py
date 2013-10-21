def build(sub_parser, cmds):
    """todo: Docstring for build

    :param sub_parser: arg description
    :type sub_parser: type description
    :return:
    :rtype:
    """

    res = {}
    for cmd in cmds:
        res[cmd.name] = cmd(sub_parser)
    # end for cmd in cmds

    return res
#build()
