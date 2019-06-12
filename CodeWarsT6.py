def areYouPlayingBanjo(name):
    first_letter = name[0]
    if first_letter == "r" or first_letter == "R":
        return name +" plays banjo"
    else:
        return name + " does not play banjo"