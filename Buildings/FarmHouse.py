from Buildings.Building import Building


class FarmHouse(Building):
    cost = 800

    stackCoin : int
    
    def __init__(self, price = cost , owner = None, health = 100 , income = 50):
        super().__init__("Farm House", price , owner,health)
        self.income = income
        self.stackCoin = 0

    def doTask(self):
        self.stackCoin += self.income

    def withdraw(self):
        coins = self.stackCoin
        self.stackCoin = 0
        return coins
        
    def doUpgrade(self):
        self.income *= 2 