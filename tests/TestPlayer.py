import unittest

from src.holdhold.Furniture import Furniture
from src.objects.Food import Food
from src.player.Player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.lina = Player("Lina", "Biel", 27, "Critic", "Marchmont", )
        self.rob = Player("Rob", "Hollingworth", 25, "Critic", "Meadows")
        self.food = Food("Bread", 30, 35)
        self.food_drink = Food("Milk", 30, 30)
        self.furniture = Furniture(1, "Bed", 15, 65, 35, 0, 65, 0, 650, "2 x 3")

    def test_player_has_name(self):
        self.assertEqual("Lina", self.lina.name)

    def test_player_has_surname(self):
        self.assertEqual("Biel", self.lina.surname)

    def test_player_has_age(self):
        self.assertEqual(27, self.lina.age)

    def test_player_has_job(self):
        self.assertEqual("Critic", self.lina.job)

    def test_player_has_social(self):
        self.assertEqual(80, self.lina.social)

    def test_player_has_hunger(self):
        self.assertEqual(80, self.lina.hunger)

    def test_player_has_bladder(self):
        self.assertEqual(80, self.lina.bladder)

    def test_player_has_energy(self):
        self.assertEqual(80, self.lina.energy)

    def test_player_has_fun(self):
        self.assertEqual(80, self.lina.fun)

    def test_player_has_hygiene(self):
        self.assertEqual(80, self.lina.hygiene)

    def test_player_has_environment(self):
        self.assertEqual(80, self.lina.environment)

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
        self.assertEqual(90, self.lina.social)

    def test_player_can_decrease_social(self):
        self.lina.decrease_social(30)
        self.assertEqual(50, self.lina.social)

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
        self.assertEqual(50, self.lina.hunger)

    def test_player_can_decrease_comfort(self):
        self.lina.decrease_comfort(30)
        self.assertEqual(50, self.lina.comfort)

    def test_player_can_increase_comfort(self):
        self.lina.increase_comfort(30)
        self.assertEqual(100, self.lina.comfort)

    def test_player_can_eat(self):
        self.lina.actions.eat(self.food)
        self.assertEqual(100, self.lina.bladder)
        self.assertEqual(45, self.lina.hunger)

    def test_player_can_talk_to_another_player(self):
        self.lina.actions.talk(self.rob)
        self.assertEqual(95, self.lina.social)
        self.assertEqual(95, self.rob.social)

    def test_player_can_sleep(self):
        self.lina.actions.sleep(self.furniture)
        self.assertEqual(100, self.lina.energy)

    def test_player_can_have_sex(self):
        self.lina.actions.have_sex(self.rob)
        self.lina.actions.have_sex(self.rob)
        self.rob.actions.have_sex(self.lina)
        self.rob.actions.have_sex(self.lina)
        self.assertEqual(100, self.lina.social)
        self.assertEqual(100, self.lina.fun)
        self.assertEqual(100, self.rob.social)
        self.assertEqual(100, self.rob.fun)

    def test_player_can_nap(self):
        self.lina.actions.nap()
        self.assertEqual(100, self.lina.energy)

    def test_player_can_watch_tv(self):
        self.rob.actions.watch_tv()
        self.assertEqual(100, self.rob.fun)

    def test_player_can_drink(self):
        self.rob.actions.drink(self.food_drink)
        self.assertEqual(50, self.rob.hunger)
        self.assertEqual(100, self.rob.bladder)

    def test_player_can_wee(self):
        self.lina.actions.wee()
        self.assertEqual(55, self.lina.bladder)

    def test_player_can_poo(self):
        self.lina.actions.poo()
        self.assertEqual(0, self.lina.bladder)

    def test_player_can_sit(self):
        self.lina.actions.sit()
        self.assertEqual(100, self.lina.comfort)

    def test_player_can_cuddle(self):
        self.lina.actions.cuddle(self.rob)
        self.assertEqual(100, self.lina.social)
        self.assertEqual(95, self.lina.fun)
        self.assertEqual(100, self.rob.social)
        self.assertEqual(95, self.rob.fun)

    def test_player_can_admire(self):
        self.lina.actions.admire(self.rob)
        self.assertEqual(95, self.lina.social)