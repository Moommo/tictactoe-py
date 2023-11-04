class TictactoeGame:
    actual_grid = [["", "", ""], ["", "", ""], ["", "", ""]]
    end_game = False
    player1 = None
    player2 = None
    winner = None

    def __init__(self):
        pass

    def define_player_symbol(self, symbol1):
        if symbol1 == "x":
            self.player1 = "x"
            self.player2 = "o"
        else:
            self.player1 = "o"
            self.player2 = "x"

    def make_player_action(self, row, column):
        self.actual_grid[row][column] = self.player1
        return self.player1


    def is_end_game(self):
        matrice = self.actual_grid
        for line in matrice:
            if len(set(line)) == 1 and line[0] != "":
                self.winner = line[0]
                self.end_game = True

        for column in range(3):
            if len(set(matrice[i][column] for i in range(3))) == 1 and matrice[0][column] != "":
                self.winner = matrice[0][column]
                self.end_game = True

        if len(set(matrice[y][y] for y in range(3))) == 1 and matrice[0][0] != "":
            self.winner = matrice[0][0]
            self.end_game = True

        if len(set(matrice[y][2 - y] for y in range(3))) == 1 and matrice[0][2] != "":
            self.winner = matrice[0][2]
            self.end_game = True