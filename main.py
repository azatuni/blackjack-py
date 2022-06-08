import random

class GameLogic:
    def __init__(self):
        self.deck = [
            "ace_of_hearts", "king_of_hearts", "queen_of_hearts", "jack_of_hearts", "10_of_hearts",
            "9_of_hearts", "8_of_hearts", "7_of_hearts", "6_of_hearts",
            "5_of_hearts", "4_of_hearts", "3_of_hearts", "2_of_hearts"
           # diamonds
           # spades
           # clubs

        ]

    def get_random_card(self):
        """Select random card"""
        random_card = random.choice(self.deck)
        self.deck.remove(random_card)
        return random_card





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    deck = GameLogic()
    card = deck.get_random_card()
    print(card)

    game_score = {"player": 0, "dealer": 0}





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
