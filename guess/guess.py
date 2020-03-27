import random as r
print("NUMBER GUESSING GAME")
num = r.randint(1, 10)
chance = 0
while chance <= 5:
    guess_num = int(input("Guess the number: "))
    if guess_num == num:
        print("CONGRATULATION YOU WON!!\nYou have guessed the number correctly")
        break
    elif guess_num < num:
        print("The number",guess_num,"is smaller than what you have guessed\nTRY AGAIN")
    else:
        print("The number",guess_num ,"is greater than what you have guessed\nTRY AGAIN")
    chance += 1
if not chance <= 5:
        print("You have lost the game!!!\nThe number is: ", num)






