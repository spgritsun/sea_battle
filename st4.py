import random

# import sys
#
# sys.setrecursionlimit(1000)
ships = [3, 2, 2, 1, 1, 1, 1]
my_board = []
enemy_board = []

cnt = 0
enemy_shot_list = []
my_shot_list = []
my_win_list = []
enemy_win_list = []
win_flag = 1
move_counter = 0


class Cell:
    def __init__(self, x, y, z, n, k):
        self.x = x
        self.y = y
        self.z = z
        self.n = n
        self.k = k


class Board:

    @classmethod
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

    @classmethod
    def boom(cls, s, board):
        board[s].z = 'T'
        return board

    @classmethod
    def boboom(cls, s, board):
        board[s].z = 'X'
        return board

    @classmethod
    def create_winner_list(cls, belonging, board):
        for i in board:
            if board[i.n].z == u"\u25A0":
               my_win_list.append(1) if belonging else enemy_win_list.append(1)

    @classmethod
    def draw_board(cls, visibility, board):
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

    @classmethod
    def create_real_board(cls, board):
        real_board = []
        for i in range(1, 7):
            for g in range(1, 7):
                real_board.append(Board.find_n(i, g, board))
        return real_board

    @classmethod
    def create_real_board_selected(cls):
        real_board_selected = []
        for i in real_board:
            if not i.k:
                real_board_selected.append(i)
        # print('длинна выборки', len(real_board_selected))
        return real_board_selected

    @classmethod
    def find_n(cls, x, y, board):
        for i in range(0, 64):
            if board[i].x == x and board[i].y == y:
                return board[i]


class Ship:
    def __init__(self, d):
        self.d = d


    @classmethod
    def ship_create(cls, d, board):

        if len(Board.create_real_board_selected()):
            real_board_selected = Board.create_real_board_selected()

            start = random.choice(real_board_selected)
            print('start.n =', start.n, 'start.x =', start.x, 'start.y =', start.y, 'd =', d,
                  'len_real_board_selected =',
                  len(real_board_selected))
            ship = [] # проверка на возможность размещения
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
            print('cnt =', cnt)

        else:
            cls.ship_create(d, board)

    @classmethod
    def create_ships(cls, ships_d, board):

        for i in ships_d:
            cls.ship_create(i, board)

    @classmethod
    def place_ships(cls, belonging, board):
        global cnt, real_board
        Ship.create_ships(ships, board)
        while cnt != 7:
            print('Пробуем ещё раз')
            cnt = 0
            board = Board.create_board()
            real_board = Board.create_real_board(board)
            Ship.create_ships(ships, board)

        if cnt == 7 and belonging:
            print('')
            print('Мои корабли расставлены', 'n = ', cnt)
            print('')
        elif cnt == 7 and not belonging:
            print('')
            print('Корабли противника расставлены', 'n = ', cnt)
            print('')


my_board = Board.create_board()
real_board = Board.create_real_board(my_board)
# real_board_selected = Board.create_real_board_selected()
# print(board[1].z)
# Board.boom(7)
# Board.ship(2)
# Board.ship(3)
# Board.boboom(4)
# Board.ship(5)
# Board.boom(12)
# Board.boom(22)
# Board.draw_board()
# print(Ship.ship_create().__dict__)
# Ship.ship_create(3)
# Ship.ship_create(3)
# Ship.ship_create(2)
# Ship.ship_create(2)
# Ship.ship_create(1)
# Ship.ship_create(1)
# Ship.ship_create(1)
# Ship.ship_create(1)
Ship.place_ships(1, my_board)

# Ship.create_ships(ships)
#
# while cnt != 7:
#     print('Пробуем ещё раз')
#     cnt = 0
#     board = Board.create_board()
#     real_board = Board.create_real_board()
#     Ship.create_ships(ships)
#
# if cnt == 7:
#     print('Всё получилось. Корабли расставлены!')
# my_board = board
Board.draw_board(1, my_board)

# print('')
# print('Корабли противника')
# print('')
enemy_board = Board.create_board()
real_board = Board.create_real_board(enemy_board)
Ship.place_ships(0, enemy_board)
Board.draw_board(1, enemy_board)

while win_flag:
    print('')
    coordinates = tuple(
        map(int, input('Чтобы сделать ход, введите номер строки и номер столбца через пробел: ' if not move_counter else 'Сделайте ваш ход: ').split()))
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
    print('')
    print(f'Ход номер {move_counter}', '\n')
    print('Мои корабли')
    # print('')
    Board.draw_board(1, my_board)
    print('')
    print('Корабли противника')
    #print('')



    Board.draw_board(0, enemy_board)

    Board.create_winner_list(1, my_board)
    Board.create_winner_list(0, enemy_board)
    if not len(enemy_win_list):
        print('\n', 'Ура! Вы выиграли!')
        win_flag = 0
    elif not len(my_win_list):
        print('\n', 'Вы проиграли! Увы!')
        win_flag = 0
    else: print('\n','Отлично! Продолжаем игру')




    my_win_list = []
    enemy_win_list = []
