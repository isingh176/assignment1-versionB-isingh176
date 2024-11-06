#!/usr/bin/env python3

'''
OPS445 Assignment 1 
Program: assignment1.py 
The python code in this file is original work written by
"Ishwinder Singh". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.

Author: Ishwinder Singh
Semester: Fall 2024
Description: This script calculates future or past date based on a given date(user input)
'''

import sys

def leap_year(year: int) -> bool:
    "return true if the year is a leap year"
    ...

def mon_max(month:int, year:int) -> int:
    "returns the maximum day for a given month. Includes leap year check"
    ...

def after(date: str) -> str: 
    '''
    after() -> date for next day in YYYY-MM-DD string format

    Return the date for the next day of the given date in YYYY-MM-DD format.
    This function has been tested to work for year after 1582
    '''
    year, mon, day= (int(x) for x in date.split('-'))
    day += 1  # next day

    lyear = year % 4
    if lyear == 0:
        leap_flag = True
    else:
        leap_flag = False  # this is not a leap year

    lyear = year % 100
    if lyear == 0:
        leap_flag = False  # this is not a leap year

    lyear = year % 400
    if lyear == 0:
        leap_flag = True  # this is a leap year
    
    mon_dict= {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
           7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if mon == 2 and leap_flag:
        mon_max = 29
    else:
        mon_max = mon_dict[mon]
    
    if day > mon_max:
        mon += 1
        if mon > 12:
            year += 1
            mon = 1
        day = 1  # if tmp_day > this month's max, reset to 1 
    return f"{year}-{mon:02}-{day:02}"

def before(date: str) -> str:
    """
    before() -> date for previous day in YYYY-MM-DD string format

    Return the date for the previous day of the given date in YYYY-MM-DD format.
    """
    year, mon, day = (int(x) for x in date.split('-'))      # Split the date into year, month, and day components
    
    day -= 1       # Move to the previous day

    if day < 1:     # Check if day goes below 1 (start of the month)
        mon -= 1     # Move to the previous month

        if mon < 1:      # If the month goes below January, reset to December of the previous year
            mon = 12
            year -= 1

        mon_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}   # Determine the maximum days in the previous month (account for leap years in February)
        
        # Check if the new month is February in a leap year
        if mon == 2 and ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
            day = 29
        else:
            day = mon_dict[mon]
    
    # Return the date formatted as YYYY-MM-DD
    return f"{year}-{mon:02}-{day:02}"


def usage():
    "Print a usage message to the user"
    print("Usage: " + str(sys.argv[0]) + " YYYY-MM-DD NN")
    sys.exit()

def valid_date(date: str) -> bool:
    "check validity of date"
    ...

def dbda(start_date: str, step: int) -> str:
    "given a start date and a number of days into the past/future, give date"
    # create a loop
    # call before() or after() as appropriate
    # return the date as a string YYYY-MM-DD
    ...

if __name__ == "__main__":
    # process command line arguments
    # call dbda()
    # output the result
    ...