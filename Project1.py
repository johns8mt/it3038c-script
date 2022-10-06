from datetime import date

today = date.today()

from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("The current time is...", current_time)
print("The date today is...", today)


#I tried multiple diifferent ways to get the date to work but found the today=date.today() method from https://www.programiz.com/python-programming/datetime/current-datetime
#To change up the code I added the time as well.
#1. Goal of the script is to display the current date and time using python. 
#2. To run the script simply copy the script and run iin any IDE that allows python. 
#3. The output of the script should be similar to this (will change depending on date and time): 
#The current time is... 22:09:42 The date today is... 2022-10-06
