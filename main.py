############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

import os
import random
from art import logo
from typing import List

def cls():  
  """ Cross-platform clear screen """
  os.system('cls' if os.name == 'nt' else 'clear')

def reset_screen():
  cls()
  print(logo)

def check_yn_input(text: str):
  while text not in ['y', 'n']:
    text = input("Invalid input! 'y' or 'n' only! ").lower()
  return text

reset_screen()


start_play = input("You wanna play some blackjack? 'y' or 'n'. ").lower()

start_play = check_yn_input(start_play)

# Should we even play?
keep_playing = start_play == 'y'


ace_name = "A"
card_value = {
  "2": 2,
  "3": 3,
  "4": 4,
  "5": 5,
  "6": 6,
  "7": 7,
  "8": 8,
  "9": 9,
  "10": 10,
  "J": 10,
  "Q": 10,
  "K": 10,
  ace_name: 11,
}
cards = list(card_value)

def calculate_score(hand: List[str]) -> int:
  """Calculate score of given hand"""
  score = 0
  for card in hand:
    score += card_value[card]
  # if there overscore and aces in hand, try to get them to 1
  aces_count = hand.count(ace_name)
  while score > 21 and aces_count > 0:
    score -= 10
    aces_count -= 1
  return score

def deal_card(hand: List[str]) -> str:
  """Add a random card to the hand and return it's name"""
  new_card = random.choice(cards)
  hand.append(new_card)
  return new_card


player_hand = []
dealer_hand = []

player_score = 0
dealer_score = 0

def print_game_info(full: bool = False):
  """Prints current state of the game"""
  dealer_print = dealer_hand if full else dealer_hand[0]
  dealer_start_text = "Dealer's cards" if full else "Dealer's first card"
  dealer_local_score = dealer_score if full else card_value[dealer_hand[0]]
  print(f"\tYour cards: {player_hand} ({player_score})")
  print(f"\t{dealer_start_text}: {dealer_print} ({dealer_local_score})")



def play_again():
  """Asks player if he wants to play again"""
  global keep_playing
  play = input("Do you wish to play again? 'y' or 'n' ").lower()
  play = check_yn_input(play)
  if play == 'n':
    keep_playing = False

while keep_playing:
  reset_screen()
  print("LET US BEGIN!")

  player_hand.clear()
  dealer_hand.clear()
  player_score = 0
  dealer_score = 0

  # start_game: deal 2 cards to player and dealer. Reveal both player cards and 1 dealer

  deal_card(player_hand)
  deal_card(player_hand)
  deal_card(dealer_hand)
  deal_card(dealer_hand)

  player_score = calculate_score(player_hand)
  dealer_score = calculate_score(dealer_hand)

  keep_drawing = True

  # 1st part: player draws cards
  while keep_drawing and player_score <= 21:
    print_game_info()

    wanna_draw = input("Type 'y' to draw a card or 'n' to stop. ").lower()
    while wanna_draw not in ['y', 'n']:
      wanna_draw = check_yn_input(wanna_draw)

    if wanna_draw == 'y':
      new_card = deal_card(player_hand)
      player_score = calculate_score(player_hand)
    else:
      keep_drawing = False

  # 2nd part: check if player is still in the game

  # if player_score > 21:
  #   print_game_info()
  #   print("I'm sorry, but you lose it all. Bye bye")
  #   play_again()
  #   continue
  
  # 3rd part: get dealer cards
  if player_score <= 21:

    while dealer_score < 17 and dealer_score < player_score:
      # print_game_info(full=True)
      new_card = deal_card(dealer_hand)
      # print(f"Dealer got a new card: {new_card}")
      dealer_score = calculate_score(dealer_hand)

  # 4th part: find the winner

  print_game_info(full=True)

  if player_score > 21 or (dealer_score <= 21 and dealer_score > player_score):
    print("Well, you lose. Deal with it.")
  elif player_score == dealer_score:
    print("It's a draw!")
  else:
    print("Hey! You win, who would have guessed!")
    
  play_again()

cls()
print(logo)
print("Ok, buh-bye!")
