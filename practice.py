import random

OUTPUT_FILE = "result.txt"

coin_faces = ["heads", "tails"]

def toss_coin():
   return random.choice(coin_faces)

die_faces = range(1, 7)

def roll_dice():
    return random.choice(die_faces)

class Card:
    def __init__(self, suite_p, value_p):
        self.suite = suite_p
        self.value = value_p

    def __str__(self):
        return "Suite = " + self.suite + ", Value = " + self.value

    def __eq__(self, other):
        return self.suite == other.suite and self.value == other.value

def build_deck():
    deck = []
    suites = ["diamond", "spade", "club", "heart"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    for suite in suites:
        for value in values:
            deck.append(Card(suite, value))

    return deck

deck = build_deck()

def shuffle_deck():
    return random.choice(deck)
 
def play(output_f):
    toss_result = toss_coin()
    dice_result = roll_dice()
    card_drawn = shuffle_deck()

    output_f.write(toss_result + "\n")
    output_f.write(str(dice_result)+ "\n")
    output_f.write(str(card_drawn) + "\n")

    return (toss_result, dice_result, card_drawn)

f_out = open(OUTPUT_FILE, "w")

coin_wins = ["heads"]
dice_wins = [6]
card_wins = [Card("spade", "J"), Card("diamond", "A")]

while(True):
    (toss_result, dice_result, card_drawn) = play(f_out)    
    if toss_result in coin_wins and dice_result in dice_wins and card_drawn in card_wins :
        f_out.write("\n YOU WON! \n")
        f_out.close()
        break
    else:
        continue




    

