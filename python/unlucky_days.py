import datetime
def unlucky_days(year):
    """(int) -> int
    Find the number of Friday 13th in the given year.
    Precondition: 1000 < |year| < 3000
    """
    month = 1
    unlucky = 0
    while month <= 12:
        start = datetime.datetime(year, month, 13)
        if start.weekday() == 4:
            
            unlucky += 1
        month += 1
    return unlucky
