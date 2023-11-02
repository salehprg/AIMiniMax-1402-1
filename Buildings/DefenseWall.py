from Buildings.Building import Building


class DefenseWall(Building):
    cost = 1000

    def __init__(self, price = cost, owner = None, health = 200):
        super().__init__("Defense Wall", price, owner,health)

    def doUpgrade(self):
        self.health *= 2
        