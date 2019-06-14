def shorten_to_date(long_date):
    date = long_date.split(",")
    date.pop()
    short_date = "".join(date)
    return short_date