

#Ask user to enter a date in format of month/day/year
#                                       mm/dd/yyyy
# Convert given date like following examples
# 03/06/2017      -> March 6, 2017
#      -4-3-2-1
# 07/10/2022      -> July 10, 2022

print("enter a date in format of month/day/year, mm/dd/y ")
#                                       mm/dd/yyyy")

date = input()
# First two charachters of the given date will give you the number of month
month = date[0:2]
day   = date[3:5]    #kantip biz kundu 3 jana 5 dep taptyk. jogoruda 8-liniyada slashdi sanaganda
# 3-jana 5-sifraga tuura kelet
year  = date[-4:]    #8-liniyadagy akyrky 4 charachter jyldy beret

if month == "01":
    print(f"January {day}, {year}")
elif month == "02":
     print(f"February {day}, {year}")
elif month == "03":
     print(f"March {day}, {year}")
elif month == "04":
     print(f"April {day}, {year}")
elif month == "05":
     print(f"May {day}, {year}")
elif month == "06":
     print(f"June {day}, {year}")
elif month == "07":
     print(f"July {day}, {year}")
elif month == "08":
     print(f"August {day}, {year}")
elif month == "09":
     print(f"September {day}, {year}")
elif month == "10":
     print(f"October {day}, {year}")
elif month == "11":
     print(f"November {day}, {year}")
elif month == "12":
     print(f"December {day}, {year}")



















