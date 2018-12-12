# Gives the age
from datetime import date
	
def calculate_age(dtob):
            today = date.today()
	    return today.year - dtob.year - ((today.month, today.day) < (dtob.month, dtob.day))
a= int(input("Enter the year of birth : "))
b= int(input("Enter the month of birth : "))
c= int(input("Enter the date of birth : "))

print(calculate_age(date(a,b,c)))
