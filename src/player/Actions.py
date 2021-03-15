class Actions:
    def __init__(self, player):
        self.player = player

    def talk(self, player_talking_to):
        self.player.increase_social(15)
        player_talking_to.increase_social(15)

    def eat(self, food):
        self.player.increase_bladder(food.increase_bladder)
        self.player.decrease_hunger(food.decrease_hunger)

    def sleep(self, furniture):
        self.player.increase_energy(furniture.energy)