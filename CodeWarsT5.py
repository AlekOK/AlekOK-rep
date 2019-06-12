def enough(cap, on, wait):
    free_places = cap - on
    people_who_left = wait - free_places
    if free_places > wait:
        return 0
    else:
        return people_who_left