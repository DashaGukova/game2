from datetime import datetime


class Log:

    @staticmethod
    def open_log(player):
        """
        Filling the file with information
        """
        with open('test.txt', 'a+') as file:
            log_time = datetime.now().strftime('%d-%m-%Y %H:%M')
            file.write(f'{log_time}, {player} - winner\n')

    @staticmethod
    def delete_log():
        """
        Removing information from the log
        """
        with open('test.txt', 'w') as file:
            file.write('')

    @staticmethod
    def show_log():
        """
        Show log
        """
        with open('test.txt', 'r') as file:
            print(file.read())
