import tkinter as tk
import random

class Util:

    @staticmethod
    def create_button(gui_instance, parent, width, height, row, column, value):

        def on_click_callback():
            gui_instance.player_action(row, column, button)

        if value is None:
            button = tk.Button(parent, text="", command=lambda: on_click_callback())
            button.config(width=width, height=height)
        else :
            #create button with image X or O
            button = tk.Button(parent, text=value.upper())
            button.config(width=width, height=height, state="disabled")
        button.grid(row=row, column=column)


    @staticmethod
    def update_button(button, value):
        button.config(text=value, state="disabled")

    @staticmethod
    def recover_button(parent, row, column):
        button = parent.grid_slaves(row=row, column=column)[0]
        return button

    @staticmethod
    def get_possible_position(matrix):
        while True:
            random_row = random.randint(0,2)
            random_column = random.randint(0,2)

            random_value = matrix[random_row][random_column]
            if random_value is None:
                return random_row, random_column

    @staticmethod
    def create_button_with_color(parent, value, action, color):
        button = tk.Button(parent, text=value, command=action, bg=color)
        button.pack()