import random


class Cell:
    def __init__(self, x, y, z, n):
        self.x = x
        self.y = y
        self.z = z
        self.n = n


class Board:

    @classmethod
    def create_board(cls, z='-'):
        line = []
        count = 0
        for l in range(1, 7):
            for r in range(1, 7):
                n = count
                c = Cell(l, r, z, n)
                line.append(c)
                count += 1
        return line

    @classmethod
    def boom(cls, s):
        board[s].z = 'T'
        # return board

    @classmethod
    def boboom(cls, s):
        board[s].z = 'Х'
        # return board

    @classmethod
    def ship(cls, s):
        board[s].z = u"\u25A0"
        # return board

    @classmethod
    def draw_board(cls):
        for i in range(1, 7):
            if i == 1:
                print('     ', i, ' ', end=' ')
            else:
                print(i, ' ', end=' ')
        print('\n')
        count = 0
        for g in range(1, 7):
            st = ''

            for k in range(1, 7):
                st += board[count].z + '   '
                count += 1

            print(g, '   ', st)


class Ship:
    def __init__(self, d):
        self.d = d

    @classmethod
    def ship_create(cls, d):
        start = random.choice(board)
        if start.n < len(board) - d and start.y + d <= 7:

            for i in range(0, d):
                board[start.n + i].z = u"\u25A0"
        else:
            cls.ship_create(d)
            # print(" Сработало")



board = Board.create_board()
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
# Ship.ship_create(1)
# Ship.ship_create(1)
# Ship.ship_create(1)
# Ship.ship_create(1)
# Ship.ship_create(2)
# Ship.ship_create(2)
Ship.ship_create(3)
Board.draw_board()
