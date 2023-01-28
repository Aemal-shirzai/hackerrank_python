"""
Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. 
It is only necessary to complete the is_leap function.

In the Gregorian calendar, three conditions are used to identify leap years:

    The year can be evenly divided by 4, is a leap year, unless:
        The year can be evenly divided by 100, it is NOT a leap year, unless:
            The year is also evenly divisible by 400. Then it is a leap year.

This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, 
while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.
"""
def is_leap(year):
    leap = False
    
    if (year % 100 != 0 and year % 4 == 0 or year % 400 == 0):
        leap = True
    
    return leap

year = int(input())