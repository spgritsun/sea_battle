import random


# import sys
# sys.setrecursionlimit(5000)


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

    # @classmethod
    # def boom(cls, s):
    #     board[s].z = 'T'
    #     # return board
    #
    # @classmethod
    # def boboom(cls, s):
    #     board[s].z = 'Х'
    #     # return board
    #
    # @classmethod
    # def ship(cls, s):
    #     board[s].z = u"\u25A0"
    #     # return board

    @classmethod
    def draw_board(cls):
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
                st += board[Board.find_n(g, k).n].z + '   '
                # count += 1

            print(g, '   ', st)

    @classmethod
    def create_real_board(cls):
        real_board = []
        for i in range(1, 7):
            for g in range(1, 7):
                real_board.append(Board.find_n(i, g))
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
    def find_n(cls, x, y):
        for i in range(0, 64):
            if board[i].x == x and board[i].y == y:
                return board[i]


class Ship:
    def __init__(self, d):
        self.d = d

    # @classmethod
    # def check_space(cls, m):
    #     lst = []
    #     for i in range(0, 36):
    #         lst.append(m[i].k)
    #     lst2 = []
    #     for i in range(0, 35):
    #         if (lst[i] == 0 and lst[i + 1] == 1) or (lst[i - 1] == 1 and lst[i] == 0):
    #             lst2.append(1)
    #         else:
    #             lst2.append(lst[i])
    #
    #     return lst2

    @classmethod
    def ship_create(cls, d):
        if len(Board.create_real_board_selected()):
            real_board_selected = Board.create_real_board_selected()

            start = random.choice(real_board_selected)
            print('start.n =', start.n, 'start.x =', start.x, 'start.y =', start.y, 'd =', d,
                  'len_real_board_selected =',
                  len(real_board_selected))
            ship = []
            for i in range(0, d):
                if board[start.n + i].k:  # or board[start.n + i - 8].k or board[start.n + i + 8].k:
                    ship.append(1)
            print(ship, len(ship))
        else:
            print("Not everything worked out)). This happens sometimes. Don't worry. Try again")
            return False
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
            return True
        else:
            cls.ship_create(d)


board = Board.create_board()
real_board = Board.create_real_board()
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
Ship.ship_create(3)
Ship.ship_create(2)
# real_board_selected = Board.create_real_board_selected()
Ship.ship_create(2)
real_board_selected = Board.create_real_board_selected()
Ship.ship_create(1)
# real_board_selected = Board.create_real_board_selected()
Ship.ship_create(1)
# real_board_selected = Board.create_real_board_selected()
Ship.ship_create(1)
# real_board_selected = Board.create_real_board_selected()
Ship.ship_create(1)
Board.draw_board()
