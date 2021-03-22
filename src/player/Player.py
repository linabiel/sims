from src.player.Actions import Actions


class Player:
    def __init__(self, name, surname, age, job, house, social=80, hunger=80, bladder=80,
                 energy=80, fun=80, hygiene=80, environment=80, money=25000, relationships=0, comfort=80):
        self.name = name
        self.surname = surname
        self.age = age
        self.job = job
        self.house = house
        self.social = social
        self.hunger = hunger
        self.bladder = bladder
        self.energy = energy
        self.fun = fun
        self.hygiene = hygiene
        self.environment = environment
        self.money = money
        self.actions = Actions(self)
        self.relationships = relationships
        self.comfort = comfort

    def change_surname(self, surname):
        self.surname = surname

    def increase_age(self):
        self.age += 1

    def change_job(self, job):
        self.job = job

    def increase_social(self, amount):
        if self.social + amount >= 100:
            self.social = 100
        else:
            self.social += amount

    def decrease_social(self, amount):
        if self.social - amount <= 0:
            self.social = 0
        else:
            self.social -= amount

    def increase_hunger(self, amount):
        if self.hunger + amount >= 100:
            self.hunger = 100
        else:
            self.hunger += amount

    def decrease_hunger(self, amount):
        if self.hunger - amount <= 0:
            self.hunger = 0
        else:
            self.hunger -= amount

    def increase_bladder(self, amount):
        if self.bladder + amount >= 100:
            self.bladder = 100
        else:
            self.bladder += amount

    def decrease_bladder(self, amount):
        if self.bladder - amount <= 0:
            self.bladder = 0
        else:
            self.bladder -= amount

    def increase_energy(self, amount):
        if self.energy + amount >= 100:
            self.energy = 100
        else:
            self.energy += amount

    def decrease_energy(self, amount):
        if self.energy - amount <= 0:
            self.energy = 0
        else:
            self.energy -= amount

    def increase_fun(self, amount):
        if self.fun + amount >= 100:
            self.fun = 100
        else:
            self.fun += amount

    def decrease_fun(self, amount):
        if self.fun - amount >= 0:
            self.fun = 0
        else:
            self.fun -= amount

    def increase_hygiene(self, amount):
        if self.hygiene + amount <= 100:
            self.hygiene = 100
        else:
            self.hygiene += amount

    def decrease_hygiene(self, amount):
        if self.hygiene - amount <= 0:
            self.hygiene = 0
        else:
            self.hygiene -= amount

    def increase_environment(self, amount):
        if self.environment + amount >= 100:
            self.environment = 100
        else:
            self.environment += amount

    def decrease_environment(self, amount):
        if self.environment - amount <= 0:
            self.environment = 0
        else:
            self.environment -= amount

    def increase_money(self, amount):
        self.money += amount

    def decrease_money(self, amount):
        self.money -= amount

    def decrease_comfort(self, amount):
        if self.comfort - amount <= 0:
            self.comfort = 0
        else:
            self.comfort -= amount

    def increase_comfort(self, amount):
        if self.comfort + amount >= 100:
            self.comfort = 100
        else:
            self.comfort += amount
