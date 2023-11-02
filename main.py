from MainGame.Board import Board
from MainGame.Player import Player
from AI.PlayerAI import PlayerAI
from gameManager import handleAction

player1 = Player(10000, "Player 1", 300)
player2 = Player(10000, "Player 2", 300)
board = Board(8, 4, player1, player2)

board.display_board()

player1_ai = PlayerAI()
player2_ai = PlayerAI()
depth = 3
isPalyer1 = True

while True:
    if isPalyer1:
        ai_action = player1_ai.choose_action(board, player1, player2, depth)

        handleAction(ai_action, player1, player2, board)

        if ai_action is None:
            print(f"AI {player1.name} doesn't have Action")
        else:
            print(
                f"AI {player1.name} chose to {ai_action.action} {ai_action.type} {ai_action.location}"
            )

    else:
        ai_action = player2_ai.choose_action(board, player2, player1, depth)

        handleAction(ai_action, player2, player1, board)

        if ai_action is None:
            print(f"AI {player2.name} doesn't have Action")
        else:
            print(
                f"AI {player2.name} chose to {ai_action.action} {ai_action.type} {ai_action.location}"
            )

    board.display_board()

    if player1.health <= 0:
        print(f"{player1.name} is out of health. {player2.name} wins!")
        exit()
    if player2.health <= 0:
        print(f"{player2.name} is out of health. {player1.name} wins!")
        exit()

    isPalyer1 = not isPalyer1
    board.nextRound()
