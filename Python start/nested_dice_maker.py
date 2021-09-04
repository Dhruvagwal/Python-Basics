# we will make a adding dice maker game
import random
def dice():
    return random.randint(1,7)

# loop

score = []
name = []
for times in range(0,3):
    player_name = input("Enter the player one name: ")
    is_player_ready = input("If you are ready then write Y or N")
    if (is_player_ready=="Y"):
        player_num1 = dice()
        player_num2 = dice()

        player_result = player_num1 + player_num2
        
        score.append(player_result)
        name.append(player_name)
        
        print("your sum is", player_result)

max_score = max(score)
player_index = score.index(max_score)
print(name[player_index],"Won")
