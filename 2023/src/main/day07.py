import abc
from functools import cmp_to_key

def day07a(input: list[str]) -> int:
    hands = parse_hands(input)
    sorted_hands = sorted(hands, key = cmp_to_key(compare_hands))
    winnings = 0
    for i in range(0, len(sorted_hands)):
        print(f"{i + 1}: {sorted_hands[i]}")
        winnings += sorted_hands[i].bid * (i + 1)

    return winnings

def day07b(input: list[str]) -> int:
    hands = parse_hands(list(map(lambda line: line.replace("J", "X"), input)))
    sorted_hands = sorted(hands, key = cmp_to_key(compare_hands))
    winnings = 0
    for i in range(0, len(sorted_hands)):
        winnings += sorted_hands[i].bid * (i + 1)

    return winnings

class HandType(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, cards: str):
        self.cards = cards
    
    def compare(self, other) -> int:
        if isinstance(other, type(self)):
            return compare_cards(self.cards, other.cards)
        return hand_values[type(self)] - hand_values[type(other)]

class FiveOfAKind(HandType):
    @staticmethod
    def is_match(cards: str) -> bool:
        card_counts = count_cards(cards)
        jokers = card_counts.get('X', 0)
        card_counts_no_joke = { card: count for (card, count) in card_counts.items() if card != 'X' }
        five_of_a_kind_matches = [card_count for card_count in card_counts_no_joke.items() if card_count[1] == 5 - jokers]
        return len(five_of_a_kind_matches) >= 1 or jokers == 5
    

class FourOfAKind(HandType):
    @staticmethod
    def is_match(cards: str) -> bool:
        card_counts = count_cards(cards)
        jokers = card_counts.get('X', 0)
        card_counts_no_joke = { card: count for (card, count) in card_counts.items() if card != 'X' }
        four_of_a_kind_matches = [card_count for card_count in card_counts_no_joke.items() if card_count[1] == 4 - jokers]
        return len(four_of_a_kind_matches) >= 1 or jokers == 4
    
class FullHouse(HandType):
    @staticmethod
    def is_match(cards: str) -> bool:
        card_counts = count_cards(cards)
        jokers = card_counts.get('X', 0)
        card_counts_no_joke = { card: count for (card, count) in card_counts.items() if card != 'X' }
        three_of_a_kind_matches = [card_count for card_count in card_counts_no_joke.items() if card_count[1] == 3]
        two_of_a_kind_matches = [card_count for card_count in card_counts_no_joke.items() if card_count[1] == 2]
        return (len(three_of_a_kind_matches) == 1 and len(two_of_a_kind_matches) == 1) or (len(two_of_a_kind_matches) == 2 and jokers == 1)
    
class ThreeOfAKind(HandType):
    @staticmethod
    def is_match(cards: str) -> bool:
        card_counts = count_cards(cards)
        jokers = card_counts.get('X', 0)
        card_counts_no_joke = { card: count for (card, count) in card_counts.items() if card != 'X' }
        three_of_a_kind_matches = [card_count for card_count in card_counts_no_joke.items() if card_count[1] == 3 - jokers]
        return len(three_of_a_kind_matches) >= 1 or jokers == 3
    
class TwoPair(HandType):
    @staticmethod
    def is_match(cards: str) -> bool:
        card_counts = count_cards(cards)
        jokers = card_counts.get('X', 0)
        card_counts_no_joke = { card: count for (card, count) in card_counts.items() if card != 'X' }
        pair_matches = [card_count for card_count in card_counts_no_joke.items() if card_count[1] == 2]
        return len(pair_matches) == 2 or (len(pair_matches) == 1 and jokers == 1)
    
class OnePair(HandType):
    @staticmethod
    def is_match(cards: str) -> bool:
        card_counts = count_cards(cards)
        jokers = card_counts.get('X', 0)
        card_counts_no_joke = { card: count for (card, count) in card_counts.items() if card != 'X' }
        two_of_a_kind_matches = [card_count for card_count in card_counts_no_joke.items() if card_count[1] == 2]
        return len(two_of_a_kind_matches) >= 1 or jokers == 1
    

class HighCard(HandType):
    pass

class Hand(object):
    def __init__(self, bid: int, cards: str):
        self.bid = bid
        self.hand_type = self.determine_type(cards)

    def determine_type(self, cards: str) -> HandType:
        if FiveOfAKind.is_match(cards):
            return FiveOfAKind(cards)
        elif FourOfAKind.is_match(cards):
            return FourOfAKind(cards)
        elif FullHouse.is_match(cards):
            return FullHouse(cards)
        elif ThreeOfAKind.is_match(cards):
            return ThreeOfAKind(cards)
        elif TwoPair.is_match(cards):
            return TwoPair(cards)
        elif OnePair.is_match(cards):
            return OnePair(cards)
        else: 
            return HighCard(cards)
    
hand_values: dict[type, int] = { FiveOfAKind : 7, FourOfAKind : 6, FullHouse : 5, ThreeOfAKind : 4, TwoPair : 3, OnePair : 2, HighCard : 1 }
card_values = { 'A' : 14, 'K' : 13, 'Q' : 12, 'J' : 11, 'T' : 10, '9' : 9, '8' : 8, '7' : 7, '6' : 6, '5' : 5, '4' : 4, '3' : 3, '2' : 2, 'X': 1 }

def compare_hands(hand1: Hand, hand2: Hand) -> int:
    comparison = hand1.hand_type.compare(hand2.hand_type)
    return comparison

def compare_cards(cards1: str, cards2: str) -> int:
    for i in range(0, len(cards1)):
        card1_value = card_values[cards1[i]]
        card2_value = card_values[cards2[i]]
        if card1_value != card2_value:
            return card1_value - card2_value
        
    return 0

def count_cards(cards: str) -> dict[str, int]:
    counts = {}
    for card in cards:
        counts[card] = counts.get(card, 0) + 1
    return counts

def parse_hands(input: list[str]) -> list[Hand]:
    hands = []
    for line in input:
        (cards, bid) = line.split(" ")
        hands.append(Hand(int(bid), cards))
        
    return hands
