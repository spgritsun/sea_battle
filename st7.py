import random

ships = [3, 2, 2, 1, 1, 1, 1]  # Сколько и каких кораблей создается на каждом поле
cnt = 0  # Счетчик количества успешно расставленных на игровом поле кораблей
enemy_shot_list = []  # Список координат выстрелов компьютера
my_shot_list = []  # Список координат выстрелов игрока
my_win_list = []  # Список оставшихся клеток кораблей игрока
enemy_win_list = []  # Список оставшихся клеток кораблей компьютера
win_flag = 1  # Флаг продолжаем/победа одного из игроков
move_counter = 0  # Счётчик ходов


class Cell:
    def __init__(self, x, y, z, n, k):
        self.x = x  # Номер строки
        self.y = y  # Номер столбца
        self.z = z  # Отображаемый символ
        self.n = n  # Номер клетки в поле 8х8
        self.k = k  # Ключ невозможности размещения


class Board:

    @classmethod  # Создаем поле 8х8
    def create_board(cls, z='-', k=0):
        line = []
        count = 0
        for l in range(0, 8):
            for r in range(0, 8):
                n = count
                c = Cell(l, r, z, n, k)
                line.append(c)
                count += 1
        return line

    @classmethod  # Создаем поле 6х6
    def create_real_board(cls, board):
        real_board = []
        for i in range(1, 7):
            for g in range(1, 7):
                real_board.append(Board.find_n(i, g, board))
        return real_board

    @classmethod  # Промах
    def boom(cls, s, board):
        board[s].z = 'T'
        return board

    @classmethod  # Попадание
    def boboom(cls, s, board):
        board[s].z = 'X'
        return board

    @classmethod  # Создание списока оставшихся клеток кораблей
    def create_winner_list(cls, belonging, board):
        for i in board:
            if board[i.n].z == u"\u25A0":
                my_win_list.append(1) if belonging else enemy_win_list.append(1)

    @classmethod
    def draw_board(cls, visibility, board):  # Отрисовка игрового поля
        for i in range(1, 7):
            if i == 1:
                print('     ', i, ' ', end=' ')
            else:
                print(i, ' ', end=' ')
        print('\n')
        # count = 0
        for g in range(1, 7):
            st = ''

            for k in range(1, 7):
                if visibility:
                    st += board[Board.find_n(g, k, board).n].z + '   '
                elif board[Board.find_n(g, k, board).n].z == 'X' or board[Board.find_n(g, k, board).n].z == 'T':
                    st += board[Board.find_n(g, k, board).n].z + '   '
                else:
                    # print(board[Board.find_n(g, k, board).n].z)
                    st += '-' + '   '

            print(g, '   ', st)

    @classmethod  # Создание списка доступных клеток
    def create_real_board_selected(cls, board):
        real_board_selected = []
        real_board = []
        for i in range(1, 7):
            for g in range(1, 7):
                real_board.append(Board.find_n(i, g, board))
        for i in real_board:
            if not i.k:
                real_board_selected.append(i)
        return real_board_selected

    @classmethod # определение номера клетки поля 8х8 по координатам (строка, столбец)
    def find_n(cls, x, y, board):
        for i in range(0, 64):
            if board[i].x == x and board[i].y == y:
                return board[i]


class Ship:
    def __init__(self, d):
        self.d = d      # Сколько клеток имеет корабль

    @classmethod        # Создание корабля и размещение его на иговом поле
    def ship_create(cls, d, board):
        try:
            if len(Board.create_real_board_selected(board)):
                real_board_selected = Board.create_real_board_selected(board)

                start = random.choice(real_board_selected)
                # print('start.n =', start.n, 'start.x =', start.x, 'start.y =', start.y, 'd =', d,
                #       'len_real_board_selected =',
                #       len(real_board_selected))
                ship = []  # проверка на возможность размещения
                for i in range(0, d):
                    if board[start.n + i].k:  # or board[start.n + i - 8].k or board[start.n + i + 8].k:
                        ship.append(1)
                # print(ship, len(ship))
            else:
                # print("Not everything worked out)). This happens sometimes. Don't worry. Try again")
                return
            if not len(ship) and start.y <= 7 - d:

                for i in range(0, d):
                    board[start.n + i].z = u"\u25A0"
                    board[start.n + i].k = 1
                    board[start.n + i - 8].k = 1
                    board[start.n + i + 8].k = 1
                board[start.n + d].k = 1
                board[start.n + d + 8].k = 1
                board[start.n + d - 8].k = 1
                board[start.n - 1].k = 1
                board[start.n - 1 + 8].k = 1
                board[start.n - 1 - 8].k = 1
                global cnt
                cnt += 1
                # print('cnt =', cnt)

            else:
                cls.ship_create(d, board)
        except RecursionError:
            print('\n', 'Упс! Возникли небольшие проблемы с расстановкой караблей, но мы их успешно решили)')

    @classmethod  # создание заданного количества кораблей
    def create_ships(cls, ships_d, board):

        for i in ships_d:
            cls.ship_create(i, board)

    @classmethod  # расстановка кораблей на игровом поле и проверка правильности их количеста
    def place_ships(cls, belonging, board):
        global cnt, my_board, enemy_board
        cnt = 0
        Ship.create_ships(ships, board)
        while cnt != 7:
            cnt = 0
            if belonging:
                my_board = Board.create_board()
                Board.create_real_board(my_board)
                Ship.create_ships(ships, my_board)
            else:
                enemy_board = Board.create_board()
                Board.create_real_board(enemy_board)
                Ship.create_ships(ships, enemy_board)

        if cnt == 7 and belonging:
            print('\n', 'Мои корабли расставлены', '\n')

        elif cnt == 7 and not belonging:
            print('\n', 'Корабли противника расставлены', '\n')


my_board = Board.create_board()
real_board = Board.create_real_board(my_board)
Ship.place_ships(1, my_board)
Board.draw_board(1, my_board)

enemy_board = Board.create_board()
real_board = Board.create_real_board(enemy_board)
Ship.place_ships(0, enemy_board)
Board.draw_board(0, enemy_board)

Board.create_winner_list(1, my_board)
Board.create_winner_list(0, enemy_board)

while win_flag:
    print('')
    coordinates = tuple(
        map(int, input(
            'Чтобы сделать ход, введите номер строки и номер столбца через пробел: ' if not move_counter else 'Сделайте ваш ход: ').split()))
    if not coordinates in my_shot_list:
        my_shot_list.append(coordinates)
    else:
        print('Вы уже делали этот ход')
        continue

    x, y = coordinates
    enemy_board = Board.boboom(Board.find_n(x, y, enemy_board).n, enemy_board) if enemy_board[Board.find_n(x, y,
                                                                                                           enemy_board).n].z == u"\u25A0" else Board.boom(
        Board.find_n(x, y, enemy_board).n, enemy_board)

    flag = 0
    while not flag:
        enemy_shot = random.choice(real_board).n
        if not enemy_shot in enemy_shot_list:
            my_board = Board.boboom(enemy_shot, my_board) if my_board[enemy_shot].z == u"\u25A0" else Board.boom(
                enemy_shot,
                my_board)
            enemy_shot_list.append(enemy_shot)
            flag = 1
    move_counter += 1
    print('\n', f'Ход номер {move_counter}', '\n')
    print('Мои корабли')

    Board.draw_board(1, my_board)
    print('\n', 'Корабли противника')
    # print('')

    Board.draw_board(0, enemy_board)

    Board.create_winner_list(1, my_board)
    Board.create_winner_list(0, enemy_board)
    if not len(enemy_win_list):
        print('\n', 'Ура! Вы выиграли!')
        win_flag = 0
    elif not len(my_win_list):
        print('\n', 'Вы проиграли! Увы!')
        win_flag = 0
    else:
        print('\n', 'Отлично! Продолжаем игру')

    my_win_list = []
    enemy_win_list = []
