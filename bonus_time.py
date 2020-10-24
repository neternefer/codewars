def bonus_time(salary, bonus):
    """If bonus is true, the salary should be multiplied by 10.
    If bonus is false, the fatcat did not make enough money and must
    receive only his stated salary.
    Return the total figure the individual will receive as a string
    prefixed with "$"
    """
    return "$" + str(salary * 10) if bonus else "$" + str(salary)