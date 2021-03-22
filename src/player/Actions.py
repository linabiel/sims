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

    def have_sex(self, player_having_sex_with):
        self.player.increase_social(60)
        player_having_sex_with.increase_social(60)
        self.player.increase_fun(50)
        player_having_sex_with.increase_social(50)

    def nap(self):
        self.player.increase_energy(25)

    def watch_tv(self):
        self.player.increase_fun(30)

    def drink(self, food):
        self.player.increase_bladder(food.increase_bladder)
        self.player.decrease_hunger(food.decrease_hunger)

    def wee(self):
        self.player.decrease_bladder(25)

    def poo(self):
        self.player.bladder = 0

    def sit(self):
        self.player.increase_comfort(25)

    def cuddle(self, player_you_are_cuddling_with):
        self.player.increase_social(25)
        self.player.increase_fun(15)
        player_you_are_cuddling_with.increase_social(25)
        player_you_are_cuddling_with.increase_fun(15)

    def admire(self, player_you_admire):
        self.player.increase_social(15)
        player_you_admire.increase_social(15)
