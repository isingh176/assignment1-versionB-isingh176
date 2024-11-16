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

    """Return true if the year is a leap year, otherwise False"""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) #Check if the year is divisble by 4 and not by 100, or if it is divisble by 100


def mon_max(month:int, year:int) -> int:

    """Returns the maximum day for a given month. Includes leap year check."""
    if month == 2:  #Check if the month is February
        return 29 if leap_year(year) else 28 #return 29 if it is a lepa year otherwise 28
    elif month in {4, 6, 9, 11}:  # April, June, September, November (if the month has 30 days)
        return 30
    return 31  # All other months have 31 days


def after(date: str) -> str: 
    """
    after() -> date for next day in YYYY-MM-DD string format

    Return the date for the next day of the given date in YYYY-MM-DD format.
    This function has been tested to work for year after 1582
    """
    year, mon, day= (int(x) for x in date.split('-'))   # Split the date string by '-' and convert each part to be an integer
    day += 1  # increasing the day by 1 for the next day

    lyear = year % 4   # Calculting the remainder by diving the year by 4
    if lyear == 0:   # Check if the year is divisble by 4
        leap_flag = True   # If divisble by 4 then it is a leap year
    else:
        leap_flag = False  # If not, then it is not a leap year

    lyear = year % 100   # Calculate the remainder by dividing the year by 100
    if lyear == 0:   # Check if it is divisble by 100
        leap_flag = False  # If yes, then it is not a leap year

    lyear = year % 400   # Calculate the remainder by dividing the year by 400
    if lyear == 0:   # Check if it is divisble by 400
        leap_flag = True  # Then it is a leap year
    
    mon_dict= {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
           7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}   # Dictionary mapping month numbers to the number of days in each of it
    if mon == 2 and leap_flag:   # Check if the month is february and it is a leap year
        mon_max = 29   # If february in a leap year, set the number of days to 29
    else:
        mon_max = mon_dict[mon]   # Otherwise get the maximum days from the dictionary
    
    if day > mon_max:   # Check if the increase in days exceed the maximum number of days in a month
        mon += 1   # Then increase the month by 1
        if mon > 12:   # Check if month number exceeds 12
            year += 1   # Then increase the year by 1
            mon = 1   # and Month=1 for when the year gets incremented by 1
        day = 1  # if the number of days gets exceeded for a month then reset it to 1
    return f"{year}-{mon:02}-{day:02}"

def before(date: str) -> str:
    """
    before() -> date for previous day in YYYY-MM-DD string format

    Return the date for the previous day of the given date in YYYY-MM-DD format.
    """
    year, mon, day = (int(x) for x in date.split('-'))    # Split the date into year, month, and day components
    
    day -= 1    # Move to the previous day

    if day < 1:    # Check if day goes below 1 (start of the month)
        mon -= 1    # Move to the previous month

        if mon < 1:    # If the month goes below January, reset to December of the previous year
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


def usage():   # Defined a function named usage
    '''Print a usage message to the user'''   # Docstring for the function
    print("Usage: " + str(sys.argv[0]) + " YYYY-MM-DD NN")   # Print a usage message including the script name and excepted date format
    sys.exit()   # Exit the program

def valid_date(date: str) -> bool:
    """Check if the date is valid in YYYY-MM-DD format."""   # Docstring for the function
    try:
        year, mon, day = (int(x) for x in date.split('-'))   #Split the date string by '-' and convert each part to integers for year, month, and day
        
        if not (1000 <= year <= 9999):   #Ensure year is a 4-digit number, month is between 1 and 12, and day is valid for the month
            return False   # If not a 4 digit number then return false
        
        max_day = mon_max(mon, year)   #Get the maximum day for the month and year
        
        print(f"Debug: Year={year}, Month={mon}, Day={day}, Max Day for Month={max_day}")   #Debugging statements to observe values
        
        is_valid = 1 <= mon <= 12 and 1 <= day <= max_day   #Check if the month and day are within valid ranges
        print(f"Debug: Valid Date Check={is_valid}")
        return is_valid   # If Valid 
    except ValueError:   # For error handling
        return False   #If an error occurs like wrong format, return False

def dbda(start_date: str, step: int) -> str:
    # create a loop
    # call before() or after() as appropriate
    # return the date as a string YYYY-MM-DD
    """Given a start date and a number of days, return the calculated date."""   # Docstring for the function
    date = start_date   #initialize the date variable with the start date
    for _ in range(abs(step)):
        date = after(date) if step > 0 else before(date)    #update the date by moving forward or backward 
    return date       #return the final calculated date


if __name__ == "__main__":
    ''' This will process command line arguments to calculate and print past and future dates based on a given start date '''
    # process command line arguments
    # call dbda()
    # output the result
    if len(sys.argv) != 3:   # Check if the number of command line arguments is not equal to 3
        usage()   # Print the usage message and exit 

    start_date = sys.argv[1]   # Get the start date from the command line argument
    try:
        divisor = int(sys.argv[2])   # Attempt to convert the divisor from a string to nn integer
        if divisor == 0:   # If the divsor is 0, print error
            print("Error: Divisor cannot be zero.")
            usage()   # Then print the usage message
    except ValueError:   # If there is an error while converting the divisor, then print the usage message and exit
        usage()

    # Validate start date format
    if not valid_date(start_date):
        print("Error: Invalid date format.")
        usage()   # Print the usage message and exit

    # Calculate the number of days to add/subtract
    days = round(365 / divisor)

    # Get the dates
    past_date = dbda(start_date, -days)   # by subtracting the calculated number of days from the start date
    future_date = dbda(start_date, days)   # by adding the the calculated number of days from the start date

    # Output the results
    print(f"A year divided by {divisor} is {days} days.")
    print(f"The date {days} days ago was {past_date}.")
    print(f"The date {days} from now will be {future_date}.")

