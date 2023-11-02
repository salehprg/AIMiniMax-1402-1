import ctypes
import typing
from MainGame.Action import Action
from Buildings.AttackTower import AttackTower
from Buildings.Building import Building
from Buildings.DefenseWall import DefenseWall
from Buildings.FarmHouse import FarmHouse


class Player:
    def __init__(self, coin, name, health):
        self.coin = coin
        self.lastAction = ""
        self.name = name
        self.health = health

    def getValidActions(self, board) -> typing.List[Action]:
        available_actions = []

        attacks, defense, farms = board.getPlayerBuildings(self)

        if self.lastAction != "attack" and len(attacks) > 0:
            attack = Action("attack", "", "")
            available_actions.append(attack)
        if self.lastAction != "farm" and len(farms) > 0:
            farm = Action("farm", "", "")
            available_actions.append(farm)

        minY = 0
        maxY = 0
        reverse = False

        if self.name == "Player 1":
            minY = 0
            maxY = board.row // 2

        if self.name == "Player 2":
            minY = board.row // 2
            maxY = board.row
            reverse = True

        yrange = range(minY, maxY)
        if reverse:
            yrange = reversed(yrange)
            
        for y in yrange:
            for x in range(board.col):
                add = True
                for piece in attacks + farms + defense:
                    if piece.location[0] == y and piece.location[1] == x:
                        add = False
                        break

                if add:
                    if self.coin >= DefenseWall.cost:
                        build_d = Action("build", "defense", [y, x])
                        available_actions.append(build_d)
                
                    if self.coin >= AttackTower.cost:
                        build_a = Action("build", "attack", [y, x])
                        available_actions.append(build_a)

                    if self.coin >= FarmHouse.cost:
                        build_f = Action("build", "farm", [y, x])
                        available_actions.append(build_f)

        return available_actions

    def doAttack(self, board, oponent):
        self.lastAction = "attack"

        attackPieces, _, _ = board.getPlayerBuildings(self)

        for attackPiece in attackPieces:
            attackLocation = attackPiece.location

            attacked = False

            targetpiece = None

            if attackLocation[0] < board.row // 2:
                for i in range(board.row // 2, board.row):
                    piece = board.getLocation([i, attackLocation[1]])
                    if piece.building != None:
                        targetpiece = piece
                        break
            else:
                for i in reversed(range(0, board.row // 2)):
                    piece = board.getLocation([i, attackLocation[1]])
                    if piece.building != None:
                        targetpiece = piece
                        break

            if targetpiece != None:
                attackPiece.building.doTask(targetpiece)
                attacked = True

            if not attacked:
                oponent.health -= attackPiece.building.damage

    def doFarm(self, board):
        self.lastAction = "farm"

        _, _, farmPieces = board.getPlayerBuildings(self)

        for farmPiece in farmPieces:
            farmPiece.building.doTask()
            self.coin += farmPiece.building.withdraw()

    def doBuild(self, board, building: Building, location):
        self.lastAction = "build"

        if building.price <= self.coin:
            if board.addBuilding(building, location):
                self.coin -= building.price
                # print(f"{self.name} -{building.price}")
                return True
            else:
                print("Tower already built. Choose again.")
        else:
            print("Not enough coins or invalid building type. Choose again.")

        return False

    def doDefense(self, board):
        self.lastAction = "defense"

        _, defensePieces, _ = board.getPlayerBuildings(self)

        for defensePiece in defensePieces:
            if defensePiece.building.price <= self.coin:
                self.coin -= defensePiece.building.price
                defensePiece.building.doUpgrade()

        return False
