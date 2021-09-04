from flight_function import calculator

print("="*38)
print("Welcome To our Flight Fair Calculator")
print("="*38,"\n")
print("Our Flight Numbers")
print("_"*38)
print("001: Delhi to Mumbai")
print("002: Delhi to Kanyakumari")
print("003: Delhi to Orrisa")
print("004: Delhi to Bihar")
print("_"*38)
# number of childrens
# number of adults
# time duration
# flight number
     
while True:
    print()
    no_of_childrens = int(input("Enter the number of childrens : "))
    no_of_adults = int(input("Enter the number of adults : "))
    time_duration = int(input("How long you want to go : "))
    flight_number = input("What's your flight number : ")

    result = calculator(no_of_childrens, no_of_adults, time_duration, flight_number)
    print("*"*38)
    if result !=None:
        print("Your flight Fair is ",result)
    else:
        print("Sorry, Flight Number is not exsist")
    print("*"*38)

    continue_or_break = input("Do you want to continue or not (Y|N) :")
    if continue_or_break == "N" or continue_or_break == "n":
        break
