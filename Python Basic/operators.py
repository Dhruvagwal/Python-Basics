# type function is functio that return the type of any class or variable
# we can use type function and any in python by just calling it as func()

# what is function

# let's define a function that takes two input and return sum value


# f(a,b) = a + b
# a and b are the parameters

# basic operators
    # * - multiplication
    # - - minus
    # + - plus
    # / - divide
    # % - modules
    # // - quotient


def sum(a,b):
    return a+b

def multiply(a,b):
    return a*b

def power(a,b):
    return a**b

# Till now what we have learned:
    # what is operators
    # how we can define function
    # how we print statements
    # whate is math operators


# python operators
    # == - equality
    # >,< - greater than previous one
    # >=,<= - whether it's greter or equal
    
# if, elif, else

def hotel_room_price_calculator(number_of_rooms, time_range,room_class):
    # the classes is differentiated in 3 parts first class, second class, third class
        # first class - Rs.7000
        # second class - Rs. 3000
        # third class - Rs.700
        
        # if it's first class than it's Rs.3000
        
        x = number_of_rooms * time_range

        if room_class == 1:
            price = 7000
        
        elif room_class == 2:
            price = 3000

        elif room_class == 2:
            price = 700
        
        else:
            return "You have entered wrong class"

        return x * price


result = hotel_room_price_calculator(2,5,4)
print(result)
        



            
