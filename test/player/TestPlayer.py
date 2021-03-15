import unittest

from src.objects.Food import Food
from src.player.Player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.lina = Player("Lina", "Biel", 27, "Critic", 35, 30, 100, 65, 15, 80, 100, 25000)
        self.rob = Player("Rob", "Hollingworth", 25, "Critic", 35, 30, 100, 65, 15, 80, 100, 25000)
        self.food = Food("Bread", 30, 35)

    def test_player_has_name(self):
        self.assertEqual("Lina", self.lina.name)

    def test_player_has_surname(self):
        self.assertEqual("Biel", self.lina.surname)

    def test_player_has_age(self):
        self.assertEqual(27, self.lina.age)

    def test_player_has_job(self):
        self.assertEqual("Critic", self.lina.job)

    def test_player_has_social(self):
        self.assertEqual(35, self.lina.social)

    def test_player_has_hunger(self):
        self.assertEqual(30, self.lina.hunger)

    def test_player_has_bladder(self):
        self.assertEqual(100, self.lina.bladder)

    def test_player_has_energy(self):
        self.assertEqual(65, self.lina.energy)

    def test_player_has_fun(self):
        self.assertEqual(15, self.lina.fun)

    def test_player_has_hygiene(self):
        self.assertEqual(80, self.lina.hygiene)

    def test_player_has_environment(self):
        self.assertEqual(100, self.lina.environment)

    def test_player_had_money(self):
        self.assertEqual(25000, self.lina.money)

    def test_player_can_change_name(self):
        self.assertEqual("Biel", self.lina.surname)
        self.lina.change_surname("Hollingworth")
        self.assertEqual("Hollingworth", self.lina.surname)

    def test_player_can_age(self):
        self.lina.increase_age()
        self.assertEqual(28, self.lina.age)

    def test_player_can_increase_social(self):
        self.lina.increase_social(10)
        self.assertEqual(45, self.lina.social)

    def test_player_can_decrease_social(self):
        self.lina.decrease_social(30)
        self.assertEqual(5, self.lina.social)

    def test_social_cannot_go_above_100(self):
        self.lina.increase_social(90)
        self.assertEqual(100, self.lina.social)

    def test_social_cannot_go_below_0(self):
        self.lina.decrease_social(90)
        self.assertEqual(0, self.lina.social)

    def test_hunger_cannot_go_above_100(self):
        self.lina.increase_hunger(90)
        self.assertEqual(100, self.lina.hunger)

    def test_player_can_decrease_hunger(self):
        self.lina.decrease_hunger(30)
        self.assertEqual(0, self.lina.hunger)

    def test_player_can_talk_to_another_player(self):
        self.lina.actions.talk(self.rob)
        self.assertEqual(50, self.lina.social)
        self.assertEqual(50, self.rob.social)

    def test_player_can_eat(self):
        self.lina.actions.eat(self.food)
        self.assertEqual(100, self.lina.bladder)
        self.assertEqual(0, self.lina.hunger)
