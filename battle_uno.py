import random
from copy import deepcopy


class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color

    def __str__(self):
        return f"{self.color} {self.value}"

    @staticmethod
    def build_card(value, color):
        new_card = Card(value, color)
        return new_card


class Hand:
    def __init__(self, hand_size):
        self.hand_size = hand_size

    @staticmethod
    def build_hand(hand_size):
        new_hand = Hand(hand_size)
        return new_hand

    hand_cards = []


class Deck:
    def __init__(self, cards):
        self.cards = cards

    def shuffle_deck(self):
        random.shuffle(self.cards)
        return self.cards

    def deal_cards(self, hand_size, num_hands):
        self.shuffle_deck()
        dealt_hands = []
        counter = 0
        while counter < num_hands:
            card_count = 0
            new_hand = Hand.build_hand(hand_size)
            while card_count < hand_size:
                new_hand.hand_cards.append(self.cards[0])
                self.cards.remove(self.cards[0])
                card_count += 1
            dealt_hands.append(new_hand.hand_cards)
            counter += 1
        print(dealt_hands)


class Player:
    def __init__(self, name, health, weakness, resistance, hand_size, cards):
        self.name = name
        self.health = health
        self.weakness = weakness
        self.resistance = resistance
        self.hand_size = hand_size
        self.cards = cards


red_cards = [
    "red_zero", "red_one_one", "red_two_one", "red_three_one", "red_four_one", "red_five_one", "red_six_one",
    "red_seven_one", "red_eight_one", "red_nine_one", "red_one_two", "red_two_two", "red_three_two", "red_four_two",
    "red_five_two", "red_six_two", "red_seven_two", "red_eight_two", "red_nine_two", "red_skip_one", "red_skip_two",
    "red_reverse_one", "red_reverse_two", "red_draw2_one", "red_draw2_two"
]
blue_cards = [
    "blue_zero", "blue_one_one", "blue_two_one", "blue_three_one", "blue_four_one", "blue_five_one", "blue_six_one",
    "blue_seven_one", "blue_eight_one", "blue_nine_one", "blue_one_two", "blue_two_two", "blue_three_two",
    "blue_four_two", "blue_five_two", "blue_six_two", "blue_seven_two", "blue_eight_two", "blue_nine_two",
    "blue_skip_one", "blue_skip_two", "blue_reverse_one", "blue_reverse_two", "blue_draw2_one", "blue_draw2_two"
]
green_cards = [
    "green_zero", "green_one_one", "green_two_one", "green_three_one", "green_four_one", "green_five_one",
    "green_six_one", "green_seven_one", "green_eight_one", "green_nine_one", "green_one_two", "green_two_two",
    "green_three_two", "green_four_two", "green_five_two", "green_six_two", "green_seven_two", "green_eight_two",
    "green_nine_two", "green_skip_one", "green_skip_two", "green_reverse_one", "green_reverse_two", "green_draw2_one",
    "green_draw2_two"
]
yellow_cards = [
    "yellow_zero", "yellow_one_one", "yellow_two_one", "yellow_three_one", "yellow_four_one", "yellow_five_one",
    "yellow_six_one", "yellow_seven_one", "yellow_eight_one", "yellow_nine_one", "yellow_one_two", "yellow_two_two",
    "yellow_three_two", "yellow_four_two", "yellow_five_two", "yellow_six_two", "yellow_seven_two", "yellow_eight_two",
    "yellow_nine_two", "yellow_skip_one", "yellow_skip_two", "yellow_reverse_one", "yellow_reverse_two",
    "yellow_draw2_one", "yellow_draw2_two"
]
wilds = [
    "wild_one", "wild_two", "wild_three", "wild_four", "wild_draw4_one", "wild_draw4_two", "wild_draw4_three",
    "wild_draw4_four"
]


red_deck = Deck(red_cards)

red_deck.deal_cards(3, 3)