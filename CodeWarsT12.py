def filter_words(st):
    i= len(st)
    up = st[0].upper()
    low= st[1:i].lower()
    y = " ".join((up+low).split())
    return y