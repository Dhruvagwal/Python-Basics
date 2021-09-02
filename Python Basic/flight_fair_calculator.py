print()
print("="*47)
print("Welcome To our Flight Fair Calculator Software")
print("="*47)
print()

print("Our Flights")
print("1. Delhi to Tamilnadu")
print("2. Meghlaya to Kanpur")
print("3. Orrisa to Goa")

# num_of_adults, num_of_children, fligt_number, time_range

def flight_fair(num_of_children=0, num_of_adults=0, flight_number=1, time_range=0):
    flight_price = 0

    if flight_number == 1:
        print("You are going to Tamil nadu from Delhi")
        flight_price = 2500

    elif  flight_number == 2:
        print("You are going to Kanpur from Meghlaya")
        flight_price = 5000

    elif flight_number == 3:
        print("You are going to Goa from Orrisa")
        flight_price = 3000

    else:
        print("You entered wrong flight number")
    
    return (num_of_adults+num_of_children)*flight_price*time_range
    

continue_operator = True

while continue_operator:
    # Taking parmaters from user
    print()
    print("_"*47)
    num_of_children = int(input("Enter the num of children :"))
    num_of_adults = int(input("Enter the num of adult :"))
    flight_number = int(input("Enter the num of flight number :"))
    time_range = int(input("Enter the num of time range :"))
    print("_"*47)
    print()


    result = flight_fair(num_of_children, num_of_adults, flight_number, time_range)

    print()
    print("_"*47)
    print("Your Bill is Rs.", result)
    print("_"*47)
    print()

    do_you_continue = input("Enter y for yes or n for no :")
    if (do_you_continue=="n"):
        continue_operator=False
    
