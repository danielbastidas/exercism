from datetime import timedelta
def add(moment):
    giga_second = 1_000_000_000
    return moment + timedelta(seconds=giga_second)
