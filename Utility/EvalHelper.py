from Buildings.AttackTower import AttackTower
from Buildings.DefenseWall import DefenseWall
from Buildings.FarmHouse import FarmHouse
from MainGame.Board import Board


class EvalHelper:
    def __init__(self, board: Board):
        self.board = board

    def getPlayerBuildings(self, player):
        return self.board.getPlayerBuildings(player)

    def getBuildingsInColumns(self, player):
        attacks_p, defense_p, farms_p = self.getPlayerBuildings(player)

        defenses = [
            [0 for i in range(self.board.col)] for j in range(self.board.row // 2)
        ]
        attacks = [
            [0 for i in range(self.board.col)] for j in range(self.board.row // 2)
        ]
        farms = [[0 for i in range(self.board.col)] for j in range(self.board.row // 2)]

        minY = 0

        if player.name == "Player 2":
            minY = self.board.row // 2

        for piece in attacks_p + defense_p + farms_p:
            if isinstance(piece.building, DefenseWall):
                defenses[piece.location[0] - minY][piece.location[1]] = 1
            if isinstance(piece.building, AttackTower):
                attacks[piece.location[0] - minY][piece.location[1]] = 1
            if isinstance(piece.building, FarmHouse):
                farms[piece.location[0] - minY][piece.location[1]] = 1

        return attacks, defenses, farms

    def getColumnsByBuilding(self, player):
        attacks, defenses, farms = self.getPlayerBuildings(player)

        attacksCols = []
        defenseCols = []
        farmsCols = []
        allCols = []
        rawCols = []

        for piece in attacks + defenses + farms:
            if isinstance(piece.building, DefenseWall):
                defenseCols.append(piece.location[1])
            if isinstance(piece.building, AttackTower):
                attacksCols.append(piece.location[1])
            if isinstance(piece.building, FarmHouse):
                farmsCols.append(piece.location[1])

            allCols.append(piece.location[1])

        attacksCols = list(set(attacksCols))
        defenseCols = list(set(defenseCols))
        farmsCols = list(set(farmsCols))
        rawCols = allCols.copy()
        allCols = list(set(allCols))

        return attacksCols, defenseCols, farmsCols, allCols, rawCols

    def pureAttackScore(self, player, oponent):
        _, _, _, buildingsCols_o, _ = self.getColumnsByBuilding(oponent)
        player_attacks, _, _, _, _ = self.getColumnsByBuilding(player)

        attack = 0
        for tower_attack in player_attacks:
            if tower_attack not in buildingsCols_o:
                attack += 1

        return attack

    def defenseOnAttackScore(self, player, oponent):
        oponent_attacks, _, _, _, _ = self.getColumnsByBuilding(oponent)
        _, defenseCols_p, _, _, _ = self.getColumnsByBuilding(player)

        playerDefense = 0

        for oponent_attack in oponent_attacks:
            if oponent_attack in defenseCols_p:
                playerDefense += 1

        return playerDefense
    
    def defenseOnPureAttackScore(self, player, oponent):
        oponent_attacks, _, _, _, _ = self.getColumnsByBuilding(oponent)
        attcks_p, defenseCols_p, farms_p, allBuildding, _ = self.getColumnsByBuilding(player)

        playerPureDefense = 0

        for oponent_attack in oponent_attacks:
            if oponent_attack in defenseCols_p and oponent_attack not in attcks_p and oponent_attack not in farms_p:
                playerPureDefense += 1

        return playerPureDefense

    def destroyBuildingOnAttack(self, player, oponent):
        attacks_o, defense_o, farms_o = self.getPlayerBuildings(oponent)
        attacks_p, defense_p, farms_p = self.getPlayerBuildings(player)

        player_attacks = []
        for attack in attacks_p:
            player_attacks.append(attack.location[1])

        destroyBuilding = 0
        for piece in attacks_o + defense_o + farms_o:
            playerAttackCount = player_attacks.count(piece.location[1])
            if playerAttackCount * AttackTower.damage >= piece.building.health:
                destroyBuilding += 1

        return destroyBuilding
