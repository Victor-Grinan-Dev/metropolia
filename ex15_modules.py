from random import randint, choice
 
# ex 1
def flip_a_coin():
    print("5 coin flips:")
    coin_sides = ["Tails!", "Heads!"]
    for _ in range(5):
        print(coin_sides[randint(0,2)])

def Foot_Nuke_Cockroach():
    choices = [ "Nuke", "Foot", "Cockroach"]
    wins = 0
    tie = 0
    rounds = 0  

    while True:
        player_choice = input("Foot, Nuke or Cockroach? (Quit ends): ")
        if player_choice == "Quit":
            print("You played", rounds ,"rounds, and won", wins ,"rounds, playing tie in", tie ,"rounds.")
            break
        elif player_choice not in choices:
            print("Incorrect selection.")
            continue
        else:
            print("You chose:", player_choice)
            pc_choice = choices[randint(1, 3)]
            print("Computer chose:", pc_choice)
            if pc_choice == player_choice:
                if pc_choice == "nuke":
                    print("Both LOSE!")
                else:
                    print("It is a tie!")
                tie += 1
            elif pc_choice == "Foot" and  player_choice == "Nuke":
                print("You WIN!")
                wins += 1
            elif pc_choice == "Nuke" and  player_choice == "Foot":
                print("You LOSE!")
            elif pc_choice == "Cockroach" and  player_choice == "Nuke":
                print("You LOSE!")
            elif pc_choice == "Nuke" and  player_choice == "Cockroach":
                print("You WIN!")
                wins += 1
            elif pc_choice == "Foot" and  player_choice == "Cockroach":
                print("You LOSE!")
            elif pc_choice == "Cockroach" and  player_choice == "Foot":
                print("You WIN!")
                wins += 1
        rounds += 1

Foot_Nuke_Cockroach()