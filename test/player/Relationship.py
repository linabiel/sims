class Relationship:
    def __init__(self, player, relationship_type, relationship_strength):
        self.player = player
        self.relationship_type = relationship_type
        self.relationship_strength = relationship_strength

    def increase_relationship_strength(self, amount):
        if self.relationship_strength + amount >= 100:
            self.relationship_strength = 100
        else:
            self.relationship_strength += amount

    def decrease_relationship_strength(self, amount):
        if self.relationship_strength - amount <= 0:
            self.relationship_strength = 0
        else:
            self.relationship_strength -= amount

