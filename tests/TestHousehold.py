import unittest
from src.player.Player import Player
from src.holdhold.Household import Household


class TestHousehold(unittest.TestCase):
    def setUp(self):
        self.player = Player("Lina", "Biel", 27, "Critic", 35, 30, 100, 65, 15, 80, 100, 25000)
        self.player1 = Player("Rob", "Hollingworth", 27, "Critic", 35, 30, 100, 65, 15, 80, 100, 25000)
        self.household = Household([self.player, self.player1], "partner", 20000, "Meadows", "bed")

    def test_check_total_money(self):
        self.assertEqual(70000, self.household.combined_money)

    def test_can_remove_player(self):
        self.household.remove_player(self.player)
        self.assertEqual([self.player1], self.household.players)

    def test_can_add_player(self):
        self.household.add_player(self.player)
        self.assertEqual([self.player, self.player1, self.player], self.household.players)

    def test_can_change_house(self):
        self.assertEqual("Meadows", self.household.house)
        self.household.change_house("Brunsfield")
        self.assertEqual("Brunsfield", self.household.house)
        print(self.household.house)
