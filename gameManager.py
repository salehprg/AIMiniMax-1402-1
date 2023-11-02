from MainGame.Action import Action
from Buildings.AttackTower import AttackTower
from Buildings.DefenseWall import DefenseWall
from Buildings.FarmHouse import FarmHouse
from MainGame.Player import Player

def handleAction(action: Action, player: Player, oponent: Player, board):
    if(action is not None):
        if action.action == "attack":
            player.doAttack(board, oponent)
        elif action.action == "farm":
            player.doFarm(board)
        elif action.action == "build":
            row, col = action.location
            if action.type == "attack":
                target_building = AttackTower(owner=player)
            elif action.type == "defense":
                target_building = DefenseWall(owner=player)
            elif action.type == "farm":
                target_building = FarmHouse(owner=player)
            player.doBuild(board, target_building, [row, col])
    else:
        player.lastAction = ''

    player.coin += 25
    oponent.coin += 25

    board.round += 1