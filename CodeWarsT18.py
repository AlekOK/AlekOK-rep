def list_animals(animals):
    a_mount = len(animals)
    list = ''
    for i in range(a_mount):
        list += str(i + 1) + '. ' + animals[i] + '\n'
    return list