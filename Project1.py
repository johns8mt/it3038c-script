from datetime import date

today = date.today()

from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("The current time is...", current_time)
print("The date today is...", today)


#I tried multiple diifferent ways to get the date to work but found the today=date.today() method from https://www.programiz.com/python-programming/datetime/current-datetime
#To change up the code I added the time as well.
