class Household:
    def __init__(self, players, relation, money, house, furniture):
        self.players = players
        self.relation = relation
        self.combined_money = 0
        self.household_money = money
        self.house = house
        self.furniture = furniture
        self.add_all_household_members_money()

    def change_relation(self, relation):
        self.relation = relation

    def add_all_household_members_money(self):
        self.combined_money = self.household_money
        for player in self.players:
            self.combined_money += player.money

    def remove_players_money_from_household(self, money):
        self.combined_money -= money

    def add_player(self, player):
        self.players.append(player)
        self.add_all_household_members_money()

    def remove_player(self, player):
        self.players.remove(player)

    def change_house(self, house):
        self.house = house
