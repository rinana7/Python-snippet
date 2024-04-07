class Tictactoe:
    def __init__(self, user):
        self.user = user
        self.board = []

    def board1(self):
        self.board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

    def show_board(self):
        for board in self.board:
            s = ""
            for element in board:
                s += element + " "
            print(s)

    def is_board_filled(self):
        for i in self.board:
            for e in i:
                if e == "-":
                    return False
        return True

    def if_3_in_a_row(self):
        # checking by row:
        for row in self.board:
            won = True
            for each_item in row:
                if each_item != self.user:
                    won = False
                    break
            if won:
                return won
        # checking by column:
        for columnI in range(len(self.board)):
            won = True
            for rowI in range(len(self.board)):
                if self.board[rowI][columnI] != self.user:
                    won = False
                    break
            if won:
                return won

        # checking by diagonal:
        won = True
        for i in range(0, len(self.board)):
            if self.board[i][i] != self.user:
                won = False
        if won:
            return won

        won = True
        for a in range(0, len(self.board)):
            for f in reversed(range(0, len(self.board))):
                if self.board[a][f] != self.user:
                    won = False
        if won:
            return won
        else:
            return False

    def place_piece(self, row, columns):
        self.board[row][columns] = self.user

    def switch_players(self):
        if self.user == "x":
            self.user = "o"
        else:
            self.user = "x"

    def start_game(self):
        self.board1()
        while not self.is_board_filled():
            print("It's " + self.user + "'s turn now.")
            self.show_board()
            row = input("Please type in the index of the row.")
            row = int(row)
            print(row)
            column = input("Please type in the index of the column.")
            column = int(column)
            print(column)
            self.place_piece(row, column)
            if self.if_3_in_a_row():
                print(self.user + " won!")
                break
            self.switch_players()
            if self.is_board_filled():
                print("It's a tie!")
                break
        self.show_board()


if __name__ == '__main__':
    game = Tictactoe("x")
    game.start_game()
