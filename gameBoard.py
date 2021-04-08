# Python Standard Library imports
import tkinter as tk

class Board(tk.Tk):

    def __init__(self, board, gamemessage):

        # Initialize parent tk class
        tk.Tk.__init__(self)
        self.buttonframe = tk.Frame(self)
        self.buttonframe.grid(row=0, column=0, pady=2, padx=2, sticky="NSEW")
        self.messageframe = tk.Frame(self)
        self.messageframe.grid(row=1, column=0, pady=2, padx=2, sticky="NSEW")


        # title text
        self.wm_title("Halma!!!!")
        self.resizable(False, False)



        for elem in board:
            if board[elem] == 2:
                self.button = tk.Button(self.buttonframe, bg='red', width=4, height=2)
                self.button.grid(row=elem[0], column=elem[1], pady=2, padx=2, sticky="NSEW")

            elif board[elem] == 1:
                self.button = tk.Button(self.buttonframe, bg='green', width=4, height=2)
                self.button.grid(row=elem[0], column=elem[1], pady=2, padx=2, sticky="NSEW")

            else:
                self.button = tk.Button(self.buttonframe, bg='white', width=4, height=2)
                self.button.grid(row=elem[0], column=elem[1], pady=2, padx=2, sticky="NSEW")
        self.displaymessage = tk.Label(self.messageframe, text=gamemessage, anchor="nw")
        self.displaymessage.grid(row=len(board), column=0, pady=2, padx=2, )
