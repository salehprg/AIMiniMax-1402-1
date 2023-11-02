from time import sleep
from MainGame.BoardPiece import BoardPiece
from Buildings.AttackTower import AttackTower
from Buildings.Building import Building
from Buildings.DefenseWall import DefenseWall
from Buildings.FarmHouse import FarmHouse


class Board:
    def __init__(self, row, col, player1, player2) -> None:
        self.round = 0
        self.row = row
        self.col = col
        self.board = [[BoardPiece(self, [j, i]) for i in range(self.col)] for j in range(self.row)]
        self.player1 = player1
        self.player2 = player2

    def display_board(self):
        print(f'\n----{self.player1.name} C:{self.player1.coin} H:{self.player1.health}----')
        for i in range(self.row):
            for j in range(self.col):
                if self.board[i][j].building is not None:
                    text = f'{self.board[i][j].building.name[0]} {self.board[i][j].building.health}'
                    print(
                        f"{self.board[i][j].building.name[0]} {self.board[i][j].building.health}" + " " * (6 - len(text)),
                        end="",
                    )
                else:
                    print("_     ", end="")
            if(i == (self.row // 2) - 1):
                print("\n\n" + "-" * 20)
            else:
                print("\n")
        print(f'----{self.player2.name} C:{self.player2.coin} H:{self.player2.health}----\n')
        print("\n" + "#" * 20)
        sleep(1)

    def nextRound(self):
        self.round += 1

    def addBuilding(self, building: Building, location) -> bool:
        piece = self.getLocation(location)
        if piece.building == None:
            piece.building = building
            return True

        return False

    def destroyBuilding(self, location) -> bool:
        piece = self.getLocation(location)
        piece.building = None
        return True

    def getLocation(self, location) -> BoardPiece:
        if (
            location[0] > self.row
            or location[0] < 0
            or location[1] > self.col
            or location[0] < 0
        ):
            return None

        return self.board[location[0]][location[1]]

    def getPlayerBuildings(self, player) -> []:
        attacks = []
        defense = []
        farms = []

        for i in self.board:
            for j in i:
                if j.building != None:
                    if j.building.owner.name == player.name:
                        if isinstance(j.building, AttackTower):
                            attacks.append(j)
                        if isinstance(j.building, FarmHouse):
                            farms.append(j)
                        if isinstance(j.building, DefenseWall):
                            defense.append(j)

        return attacks, defense, farms
