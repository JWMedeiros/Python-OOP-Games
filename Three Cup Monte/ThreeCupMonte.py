#Three Cup Monte Game:
from random import shuffle

def shuffle_list(mylist):
    shuffle (mylist)
    return mylist

def player_guess():
    guess=''
    while guess not in ['0','1','2']:
        guess=input("Pick a number: 0, 1 or 2: ")
    return int(guess)

def check_guess(mylist,guess):
    if mylist[guess]=='O':
        print("WINNER!")
    else:
        print("Please Try Again.")
        print(mylist)
        
mylist=[' ','O',' ']
shuffled_list=shuffle_list(mylist)
guess=player_guess()
check_guess(shuffled_list,guess)