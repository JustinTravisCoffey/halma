# Python Standard Library imports
import tkinter as tk


class Board(tk.Tk):

    def __init__(self, b_size, gamemessage):

        # Initialize parent tk class
        tk.Tk.__init__(self)
        self.buttonframe = tk.Frame(self)
        self.buttonframe.grid(row=0, column=0, pady=2, padx=2, sticky="NSEW")
        self.messageframe = tk.Frame(self)
        self.messageframe.grid(row=1, column=0, pady=2, padx=2, sticky="NSEW")


        # title text
        self.wm_title("Halma!!!!")
        self.resizable(False, False)

        for row in range(b_size):
            for col in range(b_size):

                if row + col < 4:
                    self.button = tk.Button(self.buttonframe, bg='red', width=4, height=2)
                    self.button.grid(row=int(row), column=int(col), pady=2, padx=2, sticky="NSEW")


                elif row + col > 2 * (b_size - 3):
                    self.button = tk.Button(self.buttonframe, bg='green', width=4, height=2)
                    self.button.grid(row=int(row), column=int(col), pady=2, padx=2, sticky="NSEW")

                else:
                    self.button = tk.Button(self.buttonframe, bg='white', width=4, height=2)
                    self.button.grid(row=int(row), column=int(col), pady=2, padx=2, sticky="NSEW")
            self.displaymessage = tk.Label(self.messageframe, text=gamemessage, anchor="nw")
            self.displaymessage.grid(row=b_size+1, column=0, pady=2, padx=2, )
