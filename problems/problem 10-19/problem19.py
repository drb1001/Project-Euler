
###
#  Problem 19 - Project Euler
#  https://projecteuler.net/problem=19
#  
#  
#  You are given the following information, but you may prefer to do some research for yourself.
#  
#  1 Jan 1900 was a Monday.
#  Thirty days has September,
#  April, June and November.
#  All the rest have thirty-one,
#  Saving February alone,
#  Which has twenty-eight, rain or shine.
#  And on leap years, twenty-nine.
#  A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#  
#  How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
#  
###

# Project Euler
# problem 19

def dayfromdate(d,m,yyyy):

    yeardays=(yyyy-1901)*365
    leapyears=(yyyy-1901)/4.0
    leapyears=int(leapyears)

    monthcount=monthdict[m-1]

    if yyyy%4==0 and m>2:
        isleapyear=1
    else:
        isleapyear=0

    dayscount = yeardays + leapyears + monthcount + isleapyear + d

    dayscount = dayscount%7

    return weekdaydict[dayscount]



monthdict = {
    0:0,
    1:31, #31
    2:59, #28
    3:90, #31
    4:120, #30
    5:151, #31
    6:181, #30
    7:212, #31
    8:243, #31
    9:273, #30
    10:304, #31
    11:334, #30
    12:365 #31
}

weekdaydict = {
    0:'M',
    1:'Tu',
    2:'W',
    3:'Th',
    4:'F',
    5:'Sa',
    6:'Su'
    }


print dayfromdate(19,2,1989)
print dayfromdate(2,8,1985)

count=0
for year in range(1901,2001):
    for month in range(1,13):
        if dayfromdate(1,month,year)=='Su':
            count+=1

print count
