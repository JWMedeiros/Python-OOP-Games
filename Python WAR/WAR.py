import random

#Suits, ranks and values variables to be used for creating cards and assigning ranks to the respective cards.
suits=('Hearts','Diamonds','Spades','Clubs')
ranks=('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values={'Two':2, 'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,
        'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}

#Classes
class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
        
    def __str__(self):
        return self.rank + " of "+self.suit

class Deck:
    def __init__(self):
        self.all_cards=[]
        for suit in suits:
            for rank in ranks:
                created_card=Card(suit,rank)
                self.all_cards.append(created_card)
    
    def shuffle(self):
        print("Deck Shuffled.")
        random.shuffle(self.all_cards)
    
    def deal_one(self):
        return self.all_cards.pop()

class Player:
    
    def __init__(self,name):
        self.name=name
        self.all_cards=[]
        
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        if type(new_cards)==type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'

#Game Setup, create players, create deck, shuffle deck and deal to both players.
player_one=Player("One")
player_two=Player("Two")

new_deck=Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())


game_on=True
round_num=0

#While Game ON, count round num, check if there is a winner, if no winner start new round.
while game_on:
    round_num+=1
    print(f"Round {round_num}")
    
    if len(player_one.all_cards)==0:
        print("Player One is out of cards and Player Two has won.")
        game_on=False
        break
    
    elif len(player_two.all_cards)==0:
        print("Player Two is out of cards and Player One has won.")
        game_on=False
        break
        
    #Start A new Round, remove cards from players and determine round winner or war
    player_one_cards=[]
    player_one_cards.append(player_one.remove_one())
    
    player_two_cards=[]
    player_two_cards.append(player_two.remove_one())
    
    

    #While At War, take 5 cards from both players, then determine war winner or if a second war is taking place.
    #Whoever wins will have cards added to their hand.
    at_war=True
    while at_war:
        if player_one_cards[-1].value>player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war=False
        elif player_two_cards[-1].value>player_one_cards[-1].value:
            player_two.add_cards(player_two_cards)
            player_two.add_cards(player_one_cards)
            at_war=False
        else:
            print('WAR!')
            if len(player_one.all_cards)<5:
                print("Player One unable to Declare War")
                print("Player Two Wins!")
                game_on=False
                break
            elif len(player_one.all_cards)<5:
                print("Player Two unable to Declare War")
                print("Player One Wins!")
                game_on=False
                break
            else:
                for num in range (5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
            