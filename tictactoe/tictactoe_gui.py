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
    label_round = None
    grid = None

    def __init__(self, game):
        self.game = game
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.geometry(f"{self.window_width}x{self.window_height}")
        message_label = tk.Label(self.window, text="Bienvenue dans mon monde 😀 ", font=("Helvetica", 26))
        message_label.pack(pady=20)
        self.initialize_game()


    def display_grid(self, matrice_grid):
        self.grid = tk.Frame(self.window, width=100, height=100)
        self.grid.pack()
        for i in range(3):
            for j in range(3):
                Util.create_button(self, self.grid, self.button_width, self.button_height, i, j, matrice_grid[i][j])

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
        self.destroy_round()
        self.continued_computer()

    def computer_action(self):
        available_row, available_column = Util.get_possible_position(self.game.actual_grid)
        self.round_computer()
        button_choose = Util.recover_button(self.grid, available_row, available_column)
        value = self.game.make_computer_action(available_row, available_column)
        self.window.after(1000, self.end_action_computer, button_choose, value)

    def end_action_computer(self, button_choose, value):
        Util.update_button(button_choose, value)
        self.destroy_round()
        self.continued_player()

    def initialize_game(self):
        self.ask_player_symbol()
        self.open_window()

    def round_player(self):
        self.label_round = tk.Label(self.window, text="C'est à toi de jouer clique sur une case vide !!",
                                    font=("Helvetica", 20, "bold"), fg="red")
        self.label_round.pack()

    def round_computer(self):
        self.label_round = tk.Label(self.window, text="C'est le tour de l'ordinateur de jouer, attend ton tour !! ",
                                    font=("Helvetica", 20, "bold"), fg="cyan")
        self.label_round.pack()

    def destroy_round(self):
        self.label_round.destroy()

    def continued_computer(self):
        if not self.game.end_game:
            self.computer_action()
        else:
            self.end()

    def continued_player(self):
        if not self.game.end_game:
            self.round_player()
        else:
            self.end()

    def run(self):
        self.destroy_ask_symbol(),
        self.display_grid(self.game.actual_grid)
        self.continued_player()

    def end(self):
        if self.game.player_is_winner():
            text = "Félicitation tu es le gagnant, bravo"
        else:
            text = "Dommage tu as perdu, retente la chance la prochaine fois"

        self.label_round = tk.Label(self.window, text=text,
                                    font=("Helvetica", 20, "bold"), fg="blue")
        self.label_round.pack()
        self.display_end_buttons()

    def open_window(self):
        self.window.mainloop()

    def close_window(self):
        self.window.destroy()

    def display_end_buttons(self):
        button_close = Util.create_button_with_color(self.window, "Quitter", self.close_window, "red")
