import tkinter as tk

class Util:

    @staticmethod
    def create_button(gui_instance, parent, width, height, row, column, value):

        def on_click_callback():
            gui_instance.player_action(row, column, button)

        if value == "":
            button = tk.Button(parent, text=value, command=lambda: on_click_callback())
            button.config(width=width, height=height)
        else :
            #create button with image X or O
            button = tk.Button(parent, text=value.upper())
            button.config(width=width, height=height, state="disabled")
        button.grid(row=row, column=column)


    @staticmethod
    def update_button(button, value):
        button.config(text=value, state="disabled")