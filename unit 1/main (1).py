#leap year

"""
year % 4==0 &
year % 100!= /
year % 400==0

"""
def isLeapyear(year):
  if(year % 4==0 and year %100!=0) or year%400==0:
    return True
  else:
    return False

  year=2010

if isLeapyear(2010):
   print("{} is a leapyear.".format(2010))
else:
   print("{} is not a leapyear.".format(2010))


  