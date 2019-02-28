import random

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.TotalScore = 0
        self.current_player = None
        self.current_turn = false

















if __name__ == "__main__":
    p1 = ComputerPlayer()
    p2 = HumanPlayer()

    game = Game(p1, p2)
    game.run_game()