from src.enums.FurnitureType import FurnitureType
from src.enums.ActionType import ActionType


class Furniture:
    def __init__(self, furniture_type, name, environment, energy, fun, hunger, social, hygiene, price, size):
        self.furniture_type = furniture_type
        self.name = name
        self.environment = environment
        self.energy = energy
        self.fun = fun
        self.hunger = hunger
        self.social = social
        self.hygiene = hygiene
        self.price = price
        self.size = size

    def get_actions(self):
        if self.furniture_type == FurnitureType.BED:
            return [ActionType.SLEEP, ActionType.HAVE_SEX, ActionType.NAP, ActionType.SIT, ActionType.TALK, ActionType.CUDDLE]
        if self.furniture_type == FurnitureType.SOFA:
            return [ActionType.SLEEP, ActionType.NAP, ActionType.HAVE_SEX, ActionType.SIT, ActionType.ADMIRE, ActionType.CUDDLE]
        if self.furniture_type == FurnitureType.TV:
            return [ActionType.WATCH_TV, ActionType.TALK, ActionType.ADMIRE]
        if self.furniture_type == FurnitureType.COOKER:
            return [ActionType.COOK]
        if self.furniture_type == FurnitureType.FRIDGE:
            return [ActionType.EAT]
        if self.furniture_type == FurnitureType.TOILET:
            return [ActionType.POO, ActionType.WEE]
        if self.furniture_type == FurnitureType.PAINTING:
            return [ActionType.ADMIRE]
