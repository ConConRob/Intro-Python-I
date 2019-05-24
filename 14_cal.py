"""
The Python standard library's 'calendar' module allows you to 
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `calendar.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should 
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that 
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

x = input("Pick a month: ")
date = datetime.now()
if x == '':
    print(date.month)
    print(calendar.monthcalendar(date.year, date.month))
else:
    input = x.split(' ')
    if len(input) == 1:
        print(calendar.monthcalendar(date.year, int(input[0])))
    elif len(input) == 2:
        print(calendar.monthcalendar(int(input[1]), int(input[0])))
    else:
        print('Expects a month and a year as numbers with a space between. For January 2009 input "1 2009"')
