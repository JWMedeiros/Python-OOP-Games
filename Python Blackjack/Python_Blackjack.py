#Blackjack version 1.0 created by John Medeiros as a bigger small project for learning OOP in Python.
#Some help from Pierian-Data from their course on Udemy titled: 2021 Complete Python Bootcamp From Zero to Hero in Python
import random

#Setup
suits=('Hearts','Diamonds','Spades','Clubs')
ranks=('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values={'Two':2, 'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,
        'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}

#Begin Classes:
class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
        
    def __str__(self):
        return self.rank + " of "+self.suit

#Deck class creates a deck of all cards with their suits and respective values for blackjack, and can be shuffled and dealt to players.
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


#BlackJackPlayer is an extension of Player, having access to Deposit, Bet and a bankroll to make bets.
class BlackJackPlayer (Player):
   
   def __init__(self,name,bankroll):
        Player.__init__(self,name)
        self.bankroll=bankroll
   
   def Deposit (self,amt):
        self.bankroll=self.bankroll + amt
    
   def Bet (self,amt):
        if self.bankroll >= amt:
            self.bankroll=self.bankroll-amt
            print(f"You have successfully placed a bet, your current bankroll is {self.bankroll}")
            return True
        else :
            print ("You have insufficient funds.")
            return False

   def __str__(self):
       return f'Player {self.name} has a bankroll of {self.bankroll}'

#Checks if a given player has busted, if they have busted but have an ace, their sum is reduced by 10, returns either True if bust or the sum if not bust
def checkBust(Player):
    sum=0
    num_Aces=0
    for card in Player.all_cards:
        sum+=values[card.rank]
    for card in Player.all_cards:
        if card.rank=='Ace':
            num_Aces+=1
    while num_Aces!=0 and sum>21:
        sum-=10
        num_Aces-=1
    if sum>21:
        return True
    else:
        return sum

def showHand(Player):
    print(f'{Player.name} has a hand of: ')
    print(*Player.all_cards,sep=',')
    print('')

#Game Logic
#Ask for name, ask for starting bank roll. Value of aces starts at 11, determined to be 1 in game logic. All face cards have value 10
while True:
        try:
            player = BlackJackPlayer(input("Please Enter your name: "),int(input("Please enter your desired bankroll: ")))
        except:
            print("An error occurred, please enter your name and a number for your desired bankroll.")
        else:
            break    
dealer = Player("Dealer")

#Set up preliminary bets for rounds, if the player does not have enough money and if they do not want to add more funds the game will end.
playing=True
while playing:
    print(player)
    bet=0
    while bet<1:
        try:
            bet=int(input("Please place a bet for the next round. \nIf the bet is larger than your bankroll you will be given the chance to add funds: "))
        except:
            print('You have entered an invalid bet, or a number less than one. Please try again.')
   
    if player.Bet(bet)==True:
        game_on=True
    else:
        choice = input("Would you like to deposit additional funds to your bankroll? y/n ")
        while choice.lower()!='y'and choice.lower()!='n':
            print("You have made an incorrect choice, please choose y or n.")
            choice = input("Would you like to deposit additional funds to your bankroll? y/n" )
        if choice=='y':
            while True:
                try:
                    bet = int(input("Please add funds: "))
                except:
                    print('You have entered an invalid amount, please try again!')
                else:
                    player.Deposit(bet)
                    game_on=False
                    break;
        else:
            playing=False
            game_on=False

    #While Game ON, show player cards, show dealer card, ask for input. After the round it will ask if the player wishes to keep playing
    while game_on:
        bust=False
        #Shuffle deck and deal hands, show cards
        deck=Deck()
        deck.shuffle()
        player.all_cards=[]
        dealer.all_cards=[]
        for x in range(2):
           player.add_cards(deck.deal_one())
           dealer.add_cards(deck.deal_one())
        print('')
    
        while bust!=True:
            showHand(player)
            print(f'{dealer.name} has {dealer.all_cards[0]} visible to you.')

            choice =input("Would you like to hit or stay? (Type hit or stay): ")
            while choice.lower()!= 'hit' and choice.lower()!='stay':
                print('Invalid input!')
                choice =input("Would you like to hit or stay? (Type hit or stay): ")
    
            #Winner Deciding Logic, if you hit, add card, perform bust calculation and ace exception. If you stay then the dealer must hit until bust or win.
            if choice=='hit':
                dealt_card=deck.deal_one()
                print(f'You have been dealt {dealt_card}')
                player.add_cards(dealt_card)
                if checkBust(player)==True:
                    print('You have busted! \n')
                    game_on=False
                    bust=True
            elif choice =='stay':
                player_sum=checkBust(player)
                dealer_sum=checkBust(dealer)
                while dealer_sum<=player_sum:
                    showHand(dealer)
                    print(f"{dealer.name} has hit.")
                    dealt_card=deck.deal_one()
                    print(f'The {dealer.name} has been dealt {dealt_card}')
                    dealer.add_cards(dealt_card)
                    if checkBust(dealer)==True:
                        print(f'The {dealer.name} has busted! {player.name} has won!')
                        player.Deposit(bet*2)
                        game_on=False
                        break
                    else:
                        dealer_sum=checkBust(dealer)
                        if dealer_sum>player_sum:
                            showHand(dealer)
                            print(f'{dealer.name} has won.')
                else:
                    showHand(dealer)
                    print(f'{dealer.name} has won.')
                choice = input("Would you like to keep playing? y/n ")
                while choice!='y' and choice !='n':
                    print("Invalid input, please try again.")
                    choice = input("Would you like to keep playing? y/n ")
                if choice=='n':
                    playing=False
                    game_on=False
                    break
                elif choice=='y':
                    game_on=False
                    break