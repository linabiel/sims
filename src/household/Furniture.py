from src.household.FurnitureType import FurnitureType
from src.player.ActionType import Action


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
            return [Action.SLEEP, Action.HAVE_SEX, Action.NAP, Action.SIT, Action.TALK, Action.CUDDLE]
        if self.furniture_type == FurnitureType.SOFA:
            return [Action.SLEEP, Action.NAP, Action.HAVE_SEX, Action.SIT, Action.ADMIRE, Action.CUDDLE]
        if self.furniture_type == FurnitureType.TV:
            return [Action.WATCH_TV, Action.TALK, Action.ADMIRE]
        if self.furniture_type == FurnitureType.COOKER:
            return [Action.COOK]
        if self.furniture_type == FurnitureType.FRIDGE:
            return [Action.EAT]
        if self.furniture_type == FurnitureType.TOILET:
            return [Action.POO, Action.WEE]
        if self.furniture_type == FurnitureType.PAINTING:
            return [Action.ADMIRE]

