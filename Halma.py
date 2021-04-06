import sys


def main(argv):
    # Process and pass along command line parameters
    if __name__ == "__main__":

        # Catch missing parameters
        if len(sys.argv) < 3:
            # h player is optional for when we start to code the AI
            print("usage: halma <b-size> <t-limit> [<h-player>]")
            sys.exit(-1)

        # Unpack params into variables
        b_size, t_limit = sys.argv[1:3]
        h_player = sys.argv[3] if len(sys.argv) == 4 else None

        # Validate b_size and t_limit
        if b_size not in ["8", "10", "16"]:
            print("error: <b-size> and should be [" + ", ".join(BOARD_SIZES) + "]")
            sys.exit(-1)

        if not b_size.isdigit() or not t_limit.isdigit():
            print("error: <b-size> and <t-limit> should be integers")
            sys.exit(-1)

        b_size = int(b_size)
        t_limit = int(t_limit)

    # todo validate the H-player argument unnecessary right now

    halmaGame = Halma(b_size, t_limit)


# Class that handles game play and launches the GUI

class Halma():
    def __init__(self, b_size, t_limit):
        self.b_size = b_size
        self.t_limit = t_limit

        # Create initial board
        board = [b_size, b_size]
        for row in range(b_size):
            for col in range(b_size):

                if row + col < 4:
                    board[row][col] = (row, col, 2)
                elif row + col > 2 * (b_size - 3):
                    board[row][col] = (row, col, 1)
                else:
                    board[row][col] = (row, col, 0)
