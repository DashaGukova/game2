from game import Game
from log import Log


def main():
    log = Log()
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
