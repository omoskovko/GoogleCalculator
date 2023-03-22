def recursive_compare(d1, d2, level="root"):
    res_list = []
    if isinstance(d1, dict) and isinstance(d2, dict):
        if d1.keys() != d2.keys():
            s1 = set(d1.keys())
            s2 = set(d2.keys())
            res_list.append("{0} + {1} - {2}".format(level, s1 - s2, s2 - s1))
            common_keys = s1 & s2
        else:
            common_keys = set(d1.keys())

        for k in common_keys:
            res_list += recursive_compare(
                d1[k], d2[k], level="{0}.{1}".format(level, k)
            )

    elif isinstance(d1, list) and isinstance(d2, list):
        if len(d1) > len(d2):
            res_list.append("{0} len1={1}; len2={2}".format(level, len(d1), len(d2)))
        common_len = min(len(d1), len(d2))

        for i in range(common_len):
            res_list += recursive_compare(
                d1[i], d2[i], level="{0}[{1}]".format(level, i)
            )

    else:
        if not isinstance(d2, type(d1)):
            res_list.append("{0} {1} != {2}".format(level, type(d1), type(d2)))
        elif d2 != d1:
            res_list.append("{0} {1} != {2}".format(level, d1, d2))

    return res_list
