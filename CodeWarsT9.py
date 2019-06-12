def correct_tail(body, tail):
    p=len(body)
    e=p-1
    if body[e] == tail:         
        return True
    else:
        return False