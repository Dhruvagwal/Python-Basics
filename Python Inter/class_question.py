# Write a program that takes a birthday as input and prints the user’s age and the
# number of days, hours, minutes and seconds until their next birthday.


# Step-1: input - DD/MM/YYYY
# Step-2 : split input:string - Date by "/"
# calculate age and calculate time left

from datetime import date

class BirthdayCalculator:
    def age_diff(self, date1,date2):
        
        # print("d1 =", date_today,month_today, year_today)
        
        year1, month1, date1 = self.get_date(date1)
        year2, month2, date2 = self.get_date(date2)

        year_left = abs(year1 - year2)
        month_left = abs(month1 - month2)
        date_left = abs(date1 - date2)

        return year_left, month_left, date_left

    def get_date(self, date):
        date = date.split('/')
        
        year =  int(date[2])
        month = int(date[1])
        date= int(date[0])
        
        return year, month, date

print("*"*30)
print("Let's Play with Age")
print("*"*30)

print()

print("1. Calculate Your Age")
print("2. ... days left in your birthday")

print()

while True:
    choice = int(input("Enter your Choice : "))

    dd_mm_yyyy = input("Enter your birthday date in dd/mm/yyyy format : ")
    cal = BirthdayCalculator()

    today = date.today()
    today = today.strftime("%d/%m/%Y")

    if choice == 1:

        year, month, date1 = cal.age_diff(today, dd_mm_yyyy)
        print(f"you are {year}.{month}.{date1} old")

    else:        

        year, month, date1 = cal.get_date(dd_mm_yyyy)
        next_bday = f"{date1}/{month}/{int(today.split('/')[2])+1}"

        year, month, days = cal.age_diff(next_bday,today)
        print(f"{days} days {month} month {year} year left")
    

    cont = input("Do you Wanna continue (Y|N) :")
    if cont == "N" or cont== "n":
        break
        
