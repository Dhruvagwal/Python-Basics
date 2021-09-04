from random import randint

answer = randint(0,10)
input_num = int(input("Enter the number : "))

# if answer == input num than print you won else print you lose
if answer == input_num:
    print("you won")

else:
    print("you lose")
