from Buildings.Building import Building


class BoardPiece():
    building : Building
    def  __init__(self,board,location) -> None:
        self.building = None
        self.board = board
        self.location = location

    def onAttack(self,damage):
        self.building.takeDamage(damage)
        if(self.building.health <= 0):
            self.board.destroyBuilding(self.location)
            return True
        
        return False