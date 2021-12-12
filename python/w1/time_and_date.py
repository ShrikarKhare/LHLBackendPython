from datetime import datetime
from datetime import date
from datetime import timedelta
import calendar
#Print out the following:
# Current date and time
now = datetime.now()
today = date.today()
print(now)
# Current year
print(today.year)
# Month of year
print(today.month)
# Week number of the year
print(today.weekday())
# Weekday of the week
print(calendar.day_name[today.weekday()])
# Day of year
print(now.timetuple().tm_yday)
# Day of the month
print(now.strftime("%d"))
# Day of week
print(now.today().weekday())
# Convert a string to datetime
stringdate = "12/12/2021"
print(datetime.strptime(stringdate, "%d/%m/%Y"))

# print the current time
print(now.time())
# subtract five days from current date
fivedaysago = timedelta(days=5)
print(now-fivedaysago)
# convert unix timestamp string to readable date unix = 1284105682
print(date.fromtimestamp(1284105682))
# convert today's date to Day of Year
print(now.timetuple().tm_yday)
# get week number from today's date
print(today.weekday())
# get the number of days between the following two dates
date_a = date(2020,2,2)
date_b = date(2020,1,1)
delta = date_a-date_b
print(delta)
#get the number of days given month and year
month = 10
year = 2016
print(calendar.monthrange(year,month)[1])
#get a list of dates between the two dates
start_dt = date(2015, 12, 20)
end_dt = date(2016, 1, 11)
delta = end_dt-start_dt
listofdates =[]
for i in range(delta.days+1):
    day = start_dt + timedelta(days=i)
    print(day)
