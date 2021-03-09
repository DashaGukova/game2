class Game:
    table = ''.join([str(i) + '\n' if i % 3 == 0 else str(i) for i in range(1, 10)])

    def __init__(self, player1, player2, log):
        self.board = self.table
        self.sign = 'X'
        self.status = True
        self.player_sign = {'X': player1, 'O': player2}
        self.log = log

    def show(self):
        """
        Show table
        """
        print(self.board)

    def update_table(self, position):
        """
        Placing X or O in the table
        """
        if position in self.board:
            self.board = self.board.replace(position, self.sign)
            self.show()
            self.sign = 'O' if self.sign == 'X' else 'X'
        else:
            position = input('Try once more:')
            self.update_table(position)

    def check(self):
        """
        Checking who is winner
        """
        solutions = [[0, 1, 2], [4, 5, 6], [8, 9, 10],
                     [0, 4, 8], [1, 5, 9], [2, 6, 10],
                     [0, 5, 10], [2, 5, 8]]
        winner = self.player_sign[self.sign]
        if any(j.isdigit() for j in self.board):
            for i in solutions:
                if self.board[i[0]] == self.board[i[1]] == self.board[i[2]]:
                    print(f'{winner} is winner')
                    self.log.open_log(winner)
                    self.status = False

        else:
            print('Draw')
