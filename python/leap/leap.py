def leap_year(year):
    return True if year % 400 == 0 else bool(year % 4 ==0 and year % 100 != 0)