# inputs
 # number of childrens
 # number of adults
 # time duration
 # flight number

 # return the fair of the flight

def calculator(no_of_child, no_of_adults, time_dur, flight_num):
    # to calculate flight fair : formula:
        # [(child*fair_for_child) + (adults*fair_for_adult)]*
    if flight_num == "001":
        child_fair = 2000

    elif flight_num == "002":
        child_fair = 2500

    elif flight_num == "003":
        child_fair = 1500

    elif flight_num == "004":
        child_fair = 1000

    else:
        return None

    return ((no_of_child*child_fair) + (no_of_adults*(child_fair+500)))*time_dur
        
