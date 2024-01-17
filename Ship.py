class Board:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def create_board(cls):
        line = []
        for l in range(1,7):
            for r in range(1,7):
                c = cls(l, r, z = '-')
                line.append(c)
        return line

    @classmethod
    def draw_board(cls):
        field = [[i for i in range(1, 7)]] * 6
        for i in range(1, 7):
            if i == 1:
                print('     ', i, ' ', end=' ')
            else:
                print(i, ' ', end=' ')
        print('\n')

        for g in range(1, 7):
            st = ''
            for k in field[g-1]:
                st += '-' + '   '

            print(g, '   ', st)


print(Board.create_board()[35].__dict__)

Board.draw_board()