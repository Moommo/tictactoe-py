import tkinter as tk
from tictactoe.util import Util

class TictactoeGui:
    grid_rows = 3
    grid_columns = 3
    window_width = 800
    window_height = 800
    button_width = 20
    button_height = 10
    label_symbol = None
    radio_x = None
    radio_o = None
    button_valider = None

    def __init__(self, game):
        self.game = game
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.geometry(f"{self.window_width}x{self.window_height}")
        message_label = tk.Label(self.window, text="Bienvenue dans mon monde 😀 ", font=("Helvetica", 26))
        message_label.pack(pady=20)
        self.initialize_game()


    def display_grid(self, matrice_grid):
        grid = tk.Frame(self.window, width=100, height=100)
        grid.pack()
        for i in range(3):
            for j in range(3):
                Util.create_button(self, grid, self.button_width, self.button_height, i, j, matrice_grid[i][j])

    def ask_player_symbol(self):
        self.label_symbol = tk.Label(self.window, text="Veuillez choisir un symbole pour commencer la partie:")
        self.label_symbol.pack()

        symbol_var = tk.StringVar()

        self.radio_x = tk.Radiobutton(self.window, text="X", variable=symbol_var, value="x")
        self.radio_o = tk.Radiobutton(self.window, text="O", variable=symbol_var, value="o")
        self.radio_x.pack()
        self.radio_o.pack()
        symbol_var.set("x")

        self.button_valider = tk.Button(self.window, text="Valider", command=lambda : [self.game.define_player_symbol(symbol_var.get()),
                                                                                       self.run()])
        self.button_valider.pack(pady=20)

    def destroy_ask_symbol(self):
        self.label_symbol.destroy()
        self.radio_x.destroy()
        self.radio_o.destroy()
        self.button_valider.destroy()

    def player_action(self, row, column, button):
        value = self.game.make_player_action(row, column)
        Util.update_button(button, value)
        print(self.game.actual_grid)

    def initialize_game(self):
        self.ask_player_symbol()
        self.open_window()

    def run(self):
        self.destroy_ask_symbol(),
        self.display_grid(self.game.actual_grid)

    def open_window(self):
        self.window.mainloop()

    def close_window(self):
        self.window.destroy()

