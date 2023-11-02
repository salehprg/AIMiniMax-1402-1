import copy
from AI.Evaluate import evaluate
from MainGame.Board import Board
from MainGame.Player import Player
from gameManager import handleAction


class PlayerAI:
    def choose_action(self, board, player, oponent, max_depth):
        best_action, _ = self.minimax(
            copy.deepcopy(board),
            copy.copy(player),
            copy.copy(oponent),
            max_depth,
            True,
        )

        return best_action

    def deepCopy(self, player, oponent, board) -> tuple[Player, Player, Board]:
        player_copy = copy.deepcopy(player)
        oponent_copy = copy.deepcopy(oponent)
        next_board = copy.deepcopy(board)
        next_board.player1 = player_copy
        next_board.player2 = oponent_copy

        return player_copy, oponent_copy, next_board

    def succusors(self, board: Board, player: Player, oponent: Player, reverse = False):
        if(reverse):
            actions = oponent.getValidActions(board)
        else:
            actions = player.getValidActions(board)

        result = []
        for action in actions:
            player_copy, oponent_copy, next_board = self.deepCopy(player, oponent, board)

            if(reverse):
                handleAction(action, oponent_copy, player_copy, next_board)
            else:
                handleAction(action, player_copy, oponent_copy, next_board)
                
            result.append({'board' : next_board , 'player' : player_copy , 'oponent' : oponent_copy, 'action' : action})

        return result



    def minimax(self, board: Board, player: Player, oponent: Player, depth, maximizing_player):
        states = self.succusors(board,player,oponent)
        return states[0]['action'], 0