from MainGame.Board import Board

from Buildings.AttackTower import AttackTower
from Buildings.DefenseWall import DefenseWall
from Buildings.FarmHouse import FarmHouse
from MainGame.Player import Player
from Utility.EvalHelper import EvalHelper


def evaluate(board: Board, player: Player, oponent: Player):
    evalHelper = EvalHelper(board)

    if oponent.health <= 0:
        return 10000000

    attacks_p,defense_p,farms_p = evalHelper.getPlayerBuildings(player)
    score = 0

    score += len(attacks_p) * 1 * (player.coin // AttackTower.cost)
    score += len(defense_p) * 4 * (player.coin // DefenseWall.cost)
    score += len(farms_p) * 2 * (player.coin // FarmHouse.cost)


    return score
