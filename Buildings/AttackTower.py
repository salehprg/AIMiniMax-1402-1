from Buildings.Building import Building


class AttackTower(Building):
    cost = 700
    damage = 50

    def __init__(self, price = cost , owner = None  , health = 100, damage = damage):
        super().__init__("Attack Tower", price,  owner , health)
        self.damage = damage

    def doTask(self , piece ):
        if(piece.building == None):
            return False
        
        if piece.onAttack(self.damage):
            self.owner.coin += 20
            
        return True
    
    def doUpgrade(self):
        self.damage *= 2
        