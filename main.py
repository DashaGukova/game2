from datetime import datetime


class Log:
    """
    Filling the file with information
    """
    @staticmethod
    def open_log(player):
        with open('test.txt', 'a+') as file:
            log_time = datetime.now().strftime('%d-%m-%Y %H:%M')
            file.write(f'{log_time}, {player} - winner\n')
    """
    Removing information from the log
    """
    @staticmethod
    def delete_log():
        with open('test.txt', 'w') as file:
            file.write('')

    """
    Show log
    """
    @staticmethod
    def show_log():
        with open('test.txt', 'r') as file:
            print(file.read())


class Game:
    table = ''.join([str(i) + '\n' if i % 3 == 0 else str(i) for i in range(1, 10)])

    def __init__(self, player1, player2, log):
        self.board = self.table
        self.sign = 'X'
        self.status = True
        self.player_sign = {'X': player1, 'O': player2}
        self.log = log

    """
    Show table
    """
    def show(self):
        print(self.board)

    """
    Placing X or O in the table
    """
    def update_table(self, position):
        if position in self.board:
            self.board = self.board.replace(position, self.sign)
            self.show()
            self.sign = 'O' if self.sign == 'X' else 'X'
        else:
            position = input('Try once more:')
            self.update_table(position)

    """
    Checking who is winner
    """
    def check(self):
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


def main():
    log = Log()
    """
    Creating each option of menu
    """
    print('1 - play\n'
          '2 - log\n'
          '3 - delete log\n'
          '4 - exit')
    option = input('Choose one of the options:')
    # option 'play'
    if option == '1':
        player1 = input('Write your name player1:')
        player2 = input('Write your name player2:')
        game = Game(player1, player2, log)
        game.show()
        while True:
            while game.status:

                position = input('Choose free cell')
                game.update_table(position)
                game.check()
            print('1 - play again\n'
                  '2 - exit')
            choose = input('What do you want:')
            if choose == '1':
                game.status = True
                game.board = game.table
                game.show()
            elif choose == '2':
                exit()
    # option 'log view'
    elif option == '2':
        log.show_log()
        main()
    # option 'delete log'
    elif option == '3':
        log.delete_log()
    # option 'exit'
    elif option == '4':
        exit()
    else:
        print('Choose one more time:')
        main()


if __name__ == '__main__':
    main()
