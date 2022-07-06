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
                user_answer = int(input(">>> "))
                answer = simple_selection[user_answer - 1]
            except:
                print("Please select one from above...")
                answer = None
        if answer == "No":
            print("Exiting the game")
            sys.exit(1)

    @staticmethod
    def make_bet(holdings) -> int:
        """
        If no bet returns 0
        """
        print("Please select bet amount")
        bet_selection = [50, 100, 200, 500]
        for bet_amount in bet_selection:
            if holdings < bet_amount:
                bet_selection.remove(bet_amount)
        bet_selection_len = len(bet_selection) + 1
        user_answer = 10
        while user_answer > bet_selection_len:
            amount_index = 0
            for amount in bet_selection:
                amount_index = amount_index + 1
                print(f"{amount_index}) {amount}$")
            next_index = amount_index + 1
            print(f"{next_index}) Quit")
            user_answer = int(input(">>> "))
        try:
            return bet_selection[user_answer - 1]
        except IndexError:
            return 0
#            print("You choose quit")
#            sys.exit(1)

    @staticmethod
    def result(result):
        print(f'{result.upper()}!')

    @staticmethod
    def stand_or_hit() -> str:
        stand_or_hit_select = {1: "stand", 2: "hit"}
        answer = None

        while answer not in stand_or_hit_select.keys():
            for key, value in stand_or_hit_select.items():
                print(f"{key}) {value}")
            answer = int(input(">>> "))
            #print(f"1) {stand_or_hit_select[0]}\n2) {stand_or_hit_select[1]}")
            return stand_or_hit_select[answer]

    @staticmethod
    def quit_game():
        print("You choose quit game")
        sys.exit(0)

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
        self.data = {"player": {"score": 0, "money": 1000,
                                "cards": [], "win": False,
                                "loose": False, "hide_second_card": False},
                     "dealer": {"score": 0, "money": 0,
                                "cards": [], "win": False,
                                "loose": False, "hide_second_card": True},
                     "round": {"number": 0, "bet": 0, "next_round": True}}

    def get_random_card(self):
        """Select random card"""
        random_card = random.choice(self.deck)
        self.deck.remove(random_card)
        return random_card

    def get_card(self, for_whom):
        card = self.get_random_card()
        self.data[for_whom]["cards"].append(card)
        return card

    def calculate_score(self, for_whom):
        score = 0
        for card in self.data[for_whom]["cards"]:
            card_data = card.split("_")
            card_name = card_data[0]
            try:
                int_card = int(card_name)
                score = score + int_card
            except ValueError:
                if card_name == "ace":
                    score = score + 11
                    if score > 21:
                        score = score - 10
                else:
                    score = score + 10
        self.data[for_whom]["score"] = score

    def increase_round(self):
        previous_round = self.data["round"]["number"]
        self.data["round"]["number"] = previous_round + 1

    def bet(self, bet):
        previous_player_money = self.data["player"]["money"]
        self.data["player"]["money"] = previous_player_money - bet
        self.data["round"]["bet"] = bet

    def reset_round(self):
        print(f"Reset round here")
        self.data["player"]["score"] = 0
        self.data["dealer"]["score"] = 0
        self.data["round"]["bet"] = 0
        self.data["player"]["cards"] = []
        self.data["dealer"]["cards"] = []
        self.data["player"]["win"] = False
        self.data["dealer"]["win"] = False



    def check_blackjack(self, for_whom) -> bool:
        if self.data[for_whom]["score"] == 21:
            self.data[for_whom]["win"] = True
            return True
        return False

    def check_loose(self, for_whom) -> bool:
        if self.data[for_whom]["score"] > 21:
            self.data[for_whom]["win"] = False
            return True
        return False


if __name__ == '__main__':
    game = GameLogic()
    ui = UserInterface
    #ui.simple_yes_no()
    #game.deal()
    def round(game):
        bet = ui.make_bet(game.data["player"]["money"])
        if bet == 0:
            ui.quit_game()
        game.bet(bet)
        game.increase_round()
        game.get_card("player")
        game.calculate_score("player")
        game.get_card("player")
        game.calculate_score("player")
        game.get_card("dealer")
        game.calculate_score("dealer")
        game.get_card("dealer")
        #game.calculate_score("dealer")

    def is_blackjack(game) -> bool:
        if game.check_blackjack("player") and game.check_blackjack("dealer"):
            ui.result("draw")
            game.reset_round()
            return True
        elif game.check_blackjack("player"):
            ui.result("win")
            game.reset_round()
            return True
        elif game.check_blackjack("dealer"):
            ui.result("loose")
            game.reset_round()
            return True
        return False

    def is_loose(game, for_whom):
        if game.check_loose(for_whom):
            ui.result("loose")
            game.reset_round()
            return True
        return False

    round(game)
    print(game.data)
    is_blackjack(game)



    #ui.stand_or_hit()
    action = "hit"
    while action == "hit":
        action = ui.stand_or_hit()
        if action == "hit":
            new_card = game.get_card("player")
            print(f"You got a {new_card}")
            game.calculate_score("player")
            print(game.data)
            if is_blackjack(game):
                break
                action = "stand"

            if is_loose(game, "player"):
                break
                action = "stand"
            print(game.data)
            print(action)

        #if game.check_loose("player")

    print(game.data)
