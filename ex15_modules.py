from random import randint, choice
 
# ex 1
def flip_a_coin():
    print("5 coin flips:")
    coin_sides = ["Tails!", "Heads!"]
    for i in range(5):
        print(coin_sides[randint(0,2)])