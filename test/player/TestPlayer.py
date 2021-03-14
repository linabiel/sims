import unittest
from src.player.Player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("Lina", "Biel", 27, "Critic", 35, 30, 100, 65, 15, 80, 100, 25000)

    def test_player_has_name(self):
        self.assertEqual("Lina", self.player.name)

    def test_player_has_surname(self):
        self.assertEqual("Biel", self.player.surname)

    def test_player_has_age(self):
        self.assertEqual(27, self.player.age)

    def test_player_has_job(self):
        self.assertEqual("Critic", self.player.job)

    def test_player_has_social(self):
        self.assertEqual(35, self.player.social)

    def test_player_has_hunger(self):
        self.assertEqual(30, self.player.hunger)

    def test_player_has_bladder(self):
        self.assertEqual(100, self.player.bladder)

    def test_player_has_energy(self):
        self.assertEqual(65, self.player.energy)

    def test_player_has_fun(self):
        self.assertEqual(15, self.player.fun)

    def test_player_has_hygiene(self):
        self.assertEqual(80, self.player.hygiene)

    def test_player_has_environment(self):
        self.assertEqual(100, self.player.environment)

    def test_player_had_money(self):
        self.assertEqual(25000, self.player.money)

    def test_player_can_change_name(self):
        self.assertEqual("Biel", self.player.surname)
        self.player.change_surname("Hollingworth")
        self.assertEqual("Hollingworth", self.player.surname)

    def test_player_can_age(self):
        self.player.increase_age()
        self.assertEqual(28, self.player.age)

    def test_player_can_increase_social(self):
        self.player.increase_social(10)
        self.assertEqual(45, self.player.social)

    def test_player_can_decrease_social(self):
        self.player.decrease_social(30)
        self.assertEqual(5, self.player.social)

    def test_social_cannot_go_above_100(self):
        self.player.increase_social(90)
        self.assertEqual(100, self.player.social)

    def test_social_cannot_go_below_0(self):
        self.player.decrease_social(90)
        self.assertEqual(0, self.player.social)

    def test_hunger_cannot_go_above_100(self):
        self.player.increase_hunger(90)
        self.assertEqual(100, self.player.hunger)

    def test_player_can_decrease_hunger(self):
        self.player.decrease_hunger(30)
        self.assertEqual(0, self.player.hunger)

