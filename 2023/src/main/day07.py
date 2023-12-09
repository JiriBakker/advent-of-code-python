from functools import cmp_to_key

def day07a(input: list[str]) -> int:
    hands = parse_hands(input)
    return calculate_winnings(hands)

def day07b(input: list[str]) -> int:
    hands = parse_hands(list(map(lambda line: line.replace("J", "X"), input)))
    return calculate_winnings(hands)

def match_five_of_a_kind(cards: str) -> bool:
    (jokers, card_counts) = count_cards(cards)
    return count_matches(card_counts, 5 - jokers) >= 1 or jokers >= 4

def match_four_of_a_kind(cards: str) -> bool:
    (jokers, card_counts) = count_cards(cards)
    return count_matches(card_counts, 4 - jokers) >= 1 or jokers == 3

def match_full_house(cards: str) -> bool:
    (jokers, card_counts) = count_cards(cards)
    three_of_a_kind_matches = count_matches(card_counts, 3)
    pair_matches = count_matches(card_counts, 2)
    return (
        (three_of_a_kind_matches == 1 and pair_matches == 1) 
            or (pair_matches == 2 and jokers == 1)
    )

def match_three_of_a_kind(cards: str) -> bool:
    (jokers, card_counts) = count_cards(cards)
    return count_matches(card_counts, 3 - jokers) >= 1 or jokers == 2

def match_two_pair(cards: str) -> bool:
    (_, card_counts) = count_cards(cards)
    return count_matches(card_counts, 2) == 2 # Two pair is not possible with jokers

def match_one_pair(cards: str) -> bool:
    (jokers, card_counts) = count_cards(cards)
    return count_matches(card_counts, 2) == 1 or jokers == 1

class Hand(object):
    def __init__(self, bid: int, cards: str):
        self.bid = bid
        self.cards = cards
        self.strength = self.__compute_strength(cards)

    def __compute_strength(self, cards: str) -> int:
        if match_five_of_a_kind(cards):    return 7
        elif match_four_of_a_kind(cards):  return 6
        elif match_full_house(cards):      return 5
        elif match_three_of_a_kind(cards): return 4
        elif match_two_pair(cards):        return 3
        elif match_one_pair(cards):        return 2
        else:                              return 1
        
    def __str__(self) -> str:
        return f"{self.bid} {self.cards} {self.strength}"
    
    def compare(self, other) -> int:
        if self.strength == other.strength:
            return compare_cards(self.cards, other.cards)
        return self.strength - other.strength
    
card_values = { 'A' : 14, 'K' : 13, 'Q' : 12, 'J' : 11, 'T' : 10, '9' : 9, '8' : 8, '7' : 7, '6' : 6, '5' : 5, '4' : 4, '3' : 3, '2' : 2, 'X': 1 }

def compare_cards(cards1: str, cards2: str) -> int:
    for i in range(0, len(cards1)):
        card1_value = card_values[cards1[i]]
        card2_value = card_values[cards2[i]]
        if card1_value != card2_value:
            return card1_value - card2_value
        
    return 0

def count_cards(cards: str) -> tuple[int, dict[str, int]]:
    counts = {}
    for card in cards:
        counts[card] = counts.get(card, 0) + 1

    jokers = counts.get('X', 0)
    counts_without_jokers = { card: count for (card, count) in counts.items() if card != 'X' }
    return (jokers, counts_without_jokers)

def count_matches(counts: dict[str, int], target: int) -> int:
    return len([card_count for card_count in counts.items() if card_count[1] == target])

def parse_hands(input: list[str]) -> list[Hand]:
    hands = []
    for line in input:
        (cards, bid) = line.split(" ")
        hands.append(Hand(int(bid), cards))
    return hands

def calculate_winnings(hands: list[Hand]) -> int:
    sorted_hands = sorted(hands, key = cmp_to_key(lambda hand1, hand2: hand1.compare(hand2)))
    winnings = 0
    for i in range(0, len(sorted_hands)):
        winnings += sorted_hands[i].bid * (i + 1)
    return winnings