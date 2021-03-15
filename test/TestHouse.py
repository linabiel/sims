import unittest

from src.household.House import House
from src.player.Player import Player


class TestHouse(unittest.TestCase):
    def setUp(self):
        self.lina = Player("Lina", "Biel", 27, "Critic")
        self.rob = Player("Rob", "Hollingworth", 27, "Software Engineer")
        self.bob = Player("Bob", "Hollingworth", 27, "Bum")
        self.house = House(["Living Room"], [self.lina, self.rob], "6, 4")

    def test_can_add_room(self):
        self.house.add_room("Bedroom")
        self.assertEqual(["Living Room", "Bedroom"], self.house.rooms)

    def test_can_remove_room(self):
        self.house.add_room("Bedroom")
        self.assertEqual(["Living Room", "Bedroom"], self.house.rooms)
        self.house.remove_room("Bedroom")
        self.assertEqual(["Living Room"], self.house.rooms)

    def test_can_add_tenant(self):
        self.house.add_tenant(self.lina)
        self.assertEqual([self.lina, self.rob, self.lina], self.house.tenants)

    def test_can_remove_tenant(self):
        self.house.add_tenant(self.bob)
        self.assertEqual([self.lina, self.rob, self.bob], self.house.tenants)
        self.house.remove_tenant(self.bob)
        self.assertEqual([self.lina, self.rob], self.house.tenants)

    def test_can_change_plot_size(self):
        self.house.change_plot_size_size(3, 2)
        self.assertEqual([3, 2], (self.house.plot_size))