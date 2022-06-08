import random
import sys


class UserInterface:
    @staticmethod
    def start():
        print("Do you want to play?")

    @staticmethod
    def simple_yes_no():
        simple_selection = ["Yes", "No"]
        print("Please select Yes or No")
        answer = None
        while answer not in simple_selection:
            print(f"1) Yes\n2) No\n")
            try:
                user_answer = int(input(">>>"))
                answer = simple_selection[user_answer - 1]
            except:
                print("Please select one from above...")
                answer = None
        if answer == "No":
            print("Exiting the game")
            sys.exit(1)


class GameLogic:
    def __init__(self):
        self.deck = [
            "ace_of_hearts", "king_of_hearts", "queen_of_hearts",
            "jack_of_hearts", "10_of_hearts", "9_of_hearts", "8_of_hearts",
            "7_of_hearts", "6_of_hearts", "5_of_hearts", "4_of_hearts",
            "3_of_hearts", "2_of_hearts",
            "ace_of_diamonds", "king_of_diamonds", "queen_of_diamonds",
            "jack_of_diamonds", "10_of_diamonds", "9_of_diamonds",
            "8_of_diamonds", "7_of_diamonds", "6_of_diamonds", "5_of_diamonds",
            "4_of_diamonds", "3_of_diamonds", "2_of_diamonds",
            "ace_of_spades", "king_of_spades",
            "queen_of_spades", "jack_of_spades", "10_of_spades", "9_of_spades",
            "8_of_spades", "7_of_spades", "6_of_spades", "5_of_spades",
            "4_of_spades", "3_of_spades", "2_of_spades",
            "ace_of_clubs", "king_of_clubs", "queen_of_clubs", "jack_of_clubs",
            "10_of_clubs", "9_of_clubs", "8_of_clubs", "7_of_clubs",
            "6_of_clubs", "5_of_clubs", "4_of_clubs", "3_of_clubs",
            "2_of_clubs"
        ]
        self.game_data = {"player": {"score": 0, "money": 1000,
                                     "cards": []},
                          "dealer": {"score": 0, "money": 0,
                                     "cards": []}}

    def get_random_card(self):
        """Select random card"""
        random_card = random.choice(self.deck)
        self.deck.remove(random_card)
        return random_card

    def get_user_card(self):
        user_card = self.get_random_card()
        self.game_data["player"]["cards"].append(user_card)
        print(self.game_data)
        return user_card

    def get_dealer_card(self):
        dealer_card = self.get_random_card()
        self.game_data["dealer"]["cards"].append(dealer_card)
        print(self.game_data)
        return dealer_card

    def calculate_score(self, for_whom):
        score = 0
        for card in self.game_data[for_whom]["cards"]:
            card_data = card.split("_")
            card_name = card[0]
            try:
                if card_name.is_integer():
                    score = score + card_name
            except AttributeError:
                if card_name == "ace" and score < 21:
                    score = score + 11
                elif card_name == "ace" and score > 21:
                    score = score + 1
                else:
                    score = score + 10
        self.game_data[for_whom]["score"] = score
        print(f"after calc {self.game_data}")


if __name__ == '__main__':
    game = GameLogic()
    ui = UserInterface
    ui.simple_yes_no()
    game.get_user_card()
    game.calculate_score("player")
    game.get_user_card()
    game.calculate_score("player")
    game.get_dealer_card()
    game.calculate_score("dealer")
    game.get_dealer_card()
    game.calculate_score("dealer")
