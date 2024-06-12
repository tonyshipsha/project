import random

choices = ["live", "blank", "blank", "blank", "blank", "blank"]
total_ammo = len(choices)
stakes = 500
cancel_game = False



print("6 rounds in the gun, 5 blank, 1 live, begin with a $500 stake, doubled after each survived round.")

while choices: # While there are more rounds than 0, didn't know this one actually. 
    
    if total_ammo == 3:
        print("There aren't that many rounds left, but with a higher risk, comes higher stakes")
    play = input("Do you want to play? (yes/no): ").strip().lower()
    if play != 'yes':
        print("--------------------------------------")
        print("Game over!")
        cancel_game = True
        break    
    
    player_turn = random.choice(choices) 
    choices.remove(player_turn)
    total_ammo -= 1 

    if player_turn == "blank":
        if total_ammo >= 3:
            stakes = stakes*2
        else:
            stakes = stakes*5
        print("--------------------------------------")
        print(player_turn)
        print(str(total_ammo) + " rounds left")
        print("Stake $" + str(stakes))
        print("--------------------------------------")

    if player_turn == "live":
        print("You are Dead")
        print("Game Over")
        break

    if total_ammo == 1:
        print("You broke the bank!")
        break

if cancel_game == True and stakes == 500:
    print("Seems like you dont want to play...")
    print("--------------------------------------")
elif stakes == 500:
    print("Better luck in the next life...")
    print("--------------------------------------")
else:
    print ("You won a total of $" + str(stakes))
    print("--------------------------------------")