# Проверка результата
class Cell:
    win_coord = ((0, 1, 2),
                 (3, 4, 5),
                 (6, 7, 8),
                 (0, 3, 6),
                 (1, 4, 7),
                 (2, 5, 8),
                 (0, 4, 8),
                 (2, 5, 6)
                 )
    def result_game(self, board, name, simbol):
        for result in self.win_coord:
            if board[result[0]] == board[result[1]] == board[result[2]]:
                print('Победил {}'.format(name))
                return True
        return False
# Заполняет игровое поле
class Board:
    board_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    def print_board(self):
        print('-' * 13)
        for i in range(3):
            print('|', self.board_list[0 + i * 3], '|', self.board_list[1 + i * 3], '|', self.board_list[2 + i * 3], '|')
            print('-' * 13)

    # Проверяем свободна клетка или нет, если свободна заполняем ее
    def games(self, simbol, answer):
        valid = False
        while not valid:
            if answer >= 1 and answer <= 9:
                print(self.board_list[answer-1])
                if self.board_list[answer-1] != ('X' or 'O'):
                    self.board_list[answer - 1] = simbol
                    break
                else:
                    answer = int(input('Эта клетка занята. Выберите свободную'))
            else:
                print('Вы вышли за диапазон от 1 до 9')
                break


# Создает игроков
class Player:
    def __init__(self, name, simbol):
        self.name = name
        self.simbol = simbol


# Запускает игру, каждый ход
def main():
    user_1 = Player('Игорь', 'X')
    user_2 = Player('Олеся', 'O')
    field = Board()
    res = Cell()

    field.print_board()
    count = 0
    while count < 9:
        count += 1
        if count % 2 == 0:
            answer = int(input('{} куда ходим: '.format(user_1.name)))
            field.games(user_1.simbol, answer)
            end_game = res.result_game(field.board_list, user_1.name, user_1.simbol)
        else:
            answer = int(input('{} куда ходим: '.format(user_2.name)))
            field.games(user_2.simbol, answer)
            end_game = res.result_game(field.board_list, user_2.name, user_2.simbol)

        field.print_board()
        if end_game:
            break

main()
