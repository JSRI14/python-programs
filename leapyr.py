yr = int(input("Please Enter any Yr: "))

if (yr%400 == 0):
          print("%d is a Leap Year" %yr)
elif (yr%100 == 0):
          print("%d is Not a  Leap Year" %yr)
elif (yr%4 == 0):
          print("%d is a Leap Year" %yr)
else:
          print("%d is Not a Leap Year" %yr)
