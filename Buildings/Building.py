class Building:
    def __init__(self, name, price , owner , health):
        self.name = name
        self.price = price
        self.owner = owner
        self.health = health
    
    def doTask(self):
        return True
    
    def doUpgrade(self):
        return True

    def takeDamage(self , damage):
        self.health -= damage
