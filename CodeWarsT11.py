def make_move(sticks):
    div_mod = sticks % 4
    if div_mod != 0:
        return div_mod
    else:
        return 1