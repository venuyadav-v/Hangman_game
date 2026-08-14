import Hangman_stages
import random
print("Let's play hangman!")
print("You have only 6 lives so try to guess the word within 6 attempts! Good luck!!")
lives=6
list=["chicken","mutton","prowns"]
given=random.choice(list)
word=[]
for i in given:
    word+='_' 
print(word)
game_over=False
while not game_over:
    userinput=input("Guess a letter!")
    for pos in range(len(given)):
        letter=given[pos]
        if letter==userinput:
            word[pos]=userinput   
    print(word)
    if userinput not in given:
        lives-=1
        if lives==0:
            game_over=True
            print("You lost!")
    if '_' not in word:
        game_over=True
        print("You win!")
    print(Hangman_stages.stages[lives])