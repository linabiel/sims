import unittest

from src.household.Furniture import Furniture
from src.enums.FurnitureType import FurnitureType
from src.enums.ActionType import ActionType


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
        self.assertEqual([ActionType.SLEEP, ActionType.HAVE_SEX, ActionType.NAP, ActionType.SIT, ActionType.TALK, ActionType.CUDDLE],
                         self.bed.get_actions())

    def test_get_furniture_action_list1(self):
        self.assertEqual([ActionType.SLEEP, ActionType.NAP, ActionType.HAVE_SEX, ActionType.SIT, ActionType.ADMIRE, ActionType.CUDDLE],
                         self.sofa.get_actions())

    def test_get_furniture_action_list2(self):
        self.assertEqual([ActionType.WATCH_TV, ActionType.TALK, ActionType.ADMIRE],
                         self.tv.get_actions())

    def test_get_furniture_action_list3(self):
        self.assertEqual([ActionType.COOK],
                         self.cooker.get_actions())

    def test_get_furniture_action_list4(self):
        self.assertEqual([ActionType.EAT],
                         self.fridge.get_actions())

    def test_get_furniture_action_list5(self):
        self.assertEqual([ActionType.POO, ActionType.WEE],
                         self.toilet.get_actions())

    def test_get_furniture_action_list6(self):
        self.assertEqual([ActionType.ADMIRE],
                         self.painting.get_actions())
