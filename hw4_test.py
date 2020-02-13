#########################################
##### Name: Erin Murray             #####
##### Uniqname: erinvm              #####
#########################################

import unittest
import hw4_cards as cards

# SI 507 Winter 2020
# Homework 4 - Code

## You can write any additional debugging/trying stuff out code here...
## OK to add debugging print statements, but do NOT change functionality of existing code.
## Also OK to add comments!

class TestCard(unittest.TestCase):
    # this is a "test"
    def test_0_create(self):
        card = cards.Card()
        self.assertEqual(card.suit_name, "Diamonds")
        self.assertEqual(card.rank, 2)

    # Add methods below to test main assignments. 
    def test_1_queen(self):
        card_queen = cards.Card(0, 12)

        self.assertEqual(card_queen.rank_name, "Queen")


    def test_2_clubs(self):
        card_clubs = cards.Card(1, 1)

        self.assertEqual(card_clubs.suit_name, "Clubs")


    def test_3_king_of_spades(self):
        king_card = cards.Card(3, 13)

        self.assertEqual(cards.Card.__str__(king_card), "King of Spades")


    def test_4_deck_total(self):
        deck4 = cards.Deck()

        self.assertEqual(len(deck4.cards), 52)


    def test_5_deal_card_return(self):
        deck5 = cards.Deck()
        deck5.shuffle()
        card5 = deck5.deal_card()

        self.assertIsInstance(card5.suit, int)
        self.assertIsInstance(card5.suit_name, str)
        self.assertIsInstance(card5.rank, int)
        self.assertIsInstance(card5.rank_name, str)


    def test_6_deal_card_less(self):
        deck6 = cards.Deck()
        deck6_comp = cards.Deck()
        deck6.deal_card()

        self.assertEqual(len(deck6.cards), len(deck6_comp.cards)-1)


    def test_7_replace_card(self):
        deck7 = cards.Deck()
        deck7.shuffle()
        card7 = deck7.deal_card()

        self.assertNotEqual(card7, deck7.cards[-1])

        deck7.replace_card(card7)

        self.assertEqual(len(deck7.cards), 52)
        self.assertEqual(card7, deck7.cards[-1])


    def test_8_wignore_replace(self):
        deck8 = cards.Deck()
        deck8.shuffle()
        card8 = deck8.deal_card()
        deck8.replace_card(card8)

        self.assertEqual(card8, deck8.cards[-1])

        deck8.replace_card(card8)

        self.assertEqual(len(deck8.cards), 52)
        self.assertEqual(card8, deck8.cards[-1])
        self.assertNotEqual(card8, deck8.cards[-2])


############
### The following is a line to run all of the tests you include:
if __name__ == "__main__":
    unittest.main()
