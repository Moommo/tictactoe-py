import tkinter as tk
from tictactoe.util import Util

class TictactoeGui:
    grid_rows = 3
    grid_columns = 3
    window_width = 800
    window_height = 800
    button_width = 20
    button_height = 10

    def __init__(self, game):
        self.game = game
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.geometry(f"{self.window_width}x{self.window_height}")


    def display_grid(self, matrice_grid):
        grid = tk.Frame(self.window, width=100, height=100)
        grid.pack()
        for i in range(3):
            for j in range(3):
                Util.create_button(self, grid, self.button_width, self.button_height, i, j, matrice_grid[i][j])


    def player_action(self, row, column, button):
        value = self.game.make_player_action(row, column)
        Util.update_button(button, value)
        print(self.game.actual_grid)

    def run(self):
        self.display_grid(self.game.actual_grid)
        self.open_window()

    def open_window(self):
        self.window.mainloop()

    def close_window(self):
        self.window.destroy()

