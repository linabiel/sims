import unittest

from src.household.Furniture import Furniture
from src.household.FurnitureType import FurnitureType
from src.player.ActionType import Action


class TestFurniture(unittest.TestCase):
    def setUp(self):
        self.bed = Furniture(FurnitureType.BED, "Bed", 6, 7, 5, 0, 5, 0, 565, [2, 4])
        self.sofa = Furniture(FurnitureType.SOFA, "Sofa", 6, 7, 5, 0, 5, 0, 565, [2, 4])
        self.toilet = Furniture(FurnitureType.TOILET, "Toilet", 6, 7, 5, 0, 5, 0, 565, [2, 4])
        self.painting = Furniture(FurnitureType.PAINTING, "Painting", 6, 7, 5, 0, 5, 0, 565, [2, 4])
        self.cooker = Furniture(FurnitureType.COOKER, "Cooker", 6, 7, 5, 0, 5, 0, 565, [2, 4])
        self.fridge = Furniture(FurnitureType.FRIDGE, "Fridge", 6, 7, 5, 0, 5, 0, 565, [2, 4])
        self.tv = Furniture(FurnitureType.TV, "Tv", 6, 7, 5, 0, 5, 0, 565, [2, 4])

    def test_get_furniture_action_list(self):
        self.assertEqual([Action.SLEEP, Action.HAVE_SEX, Action.NAP, Action.SIT, Action.TALK, Action.CUDDLE],
                         self.bed.get_actions())

    def test_get_furniture_action_list1(self):
        self.assertEqual([Action.SLEEP, Action.NAP, Action.HAVE_SEX, Action.SIT, Action.ADMIRE, Action.CUDDLE],
                         self.sofa.get_actions())

    def test_get_furniture_action_list2(self):
        self.assertEqual([Action.WATCH_TV, Action.TALK, Action.ADMIRE],
                         self.tv.get_actions())

    def test_get_furniture_action_list3(self):
        self.assertEqual([Action.COOK],
                         self.cooker.get_actions())

    def test_get_furniture_action_list4(self):
        self.assertEqual([Action.EAT],
                         self.fridge.get_actions())

    def test_get_furniture_action_list5(self):
        self.assertEqual([Action.POO, Action.WEE],
                         self.toilet.get_actions())

    def test_get_furniture_action_list6(self):
        self.assertEqual([Action.ADMIRE],
                         self.painting.get_actions())
