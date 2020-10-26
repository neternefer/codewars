def rental_car_cost(d):
    """Every day you rent the car costs $40.
    If you rent the car for 7 or more days, you get $50 off your total.
    Alternatively, if you rent the car for 3 or more days, you get $20 off
    your total.
    Write a code that gives out the total amount for different days(d)."""
    total = d * 40
    if d >= 7:
        total -= 50
    elif d >= 3:
        total -= 20
    return total