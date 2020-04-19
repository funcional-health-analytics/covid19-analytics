def aux_enforce_max_addition(Q, delta):
    if Q - delta <= 0:
        return Q

    else:
        return delta


def aux_enforce_max_removal(Q, delta):
    if Q + delta <= 0:
        return -Q
    else:
        return delta


def param_at(param_var, t):
    if isinstance(param_var, dict):
        return param_var[t]
    else:
        return param_var


def dynamic_parameter(regimens, min_length):
    i = 0
    params = {}
    last_value = None
    min_length = int(min_length)
    for value, length in regimens:
        length = int(length)
        param = {t: value for t in range(i, i + length)}
        params.update(param)
        i += length
        last_value = value

    # if we do not have enough data, fill in the remaining entries with the last specified value
    if i < min_length:
        param = {t: last_value for t in range(i, i + min_length)}
        params.update(param)

    return params
