import unittest

from src.objects.Food import Food
from src.player.Player import Player


class TestFood(unittest.TestCase):
    def setUp(self):
        self.bread = Food("Bread", 30, 20)
        self.apple = Food("Apple", 20, 15)
        self.lina = Player("Lina", "Biel", 27, "Critic", "Marchmont")

    def test_if_food_can_decrease_hunger_and_increase_bladder(self):
        self.lina.actions.eat(self.apple)
        self.assertEqual(65, self.lina.hunger)
        self.assertEqual(100, self.lina.bladder)
