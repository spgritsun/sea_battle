cells = list(range(1, 10))
# cells = [1,2,3,4,'O',6,'X',8,9]
st = list(range(0, 3))


def drow_board():
    n = 0
    print('-------------')
    for i in st:
        print('|', cells[n], '|', cells[n + 1], '|', cells[n + 2], '|')
        n += 3
    print('-------------')
    print('Ход номер: ', move)


def win_case():
    win_line = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7),
                (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))
    for i, v, g in win_line:
        if cells[i - 1] == cells[v - 1] == cells[g - 1]:
            print('Тадамм!!! Вы выиграли!!!')
            global break_flag
            break_flag = False
            break

def game_draw():
    global break_flag
    if move >= 9 and break_flag == True:
        print('Ничья! Попробуйте ещё раз!')
        break_flag = False



def change_player(sign):
    if sign == 'X':
        sign = 'O'
        return sign
    if sign == 'O':
        sign = 'X'
        return sign


def do_input(sign):
    while break_flag:
        sign = change_player(sign)
        value = input('Куда поставить: ' + sign)
        if not value.isdigit() or int(value) not in list(range(1, 10)):
            print('Неправильный ввод! Вводить можно только цифры от 1 до 9')
            sign = change_player(sign)
            continue
        elif str(cells[int(value) - 1]) in 'XO':
            print('Неправильный ввод! Эта клетка уже занята')
            sign = change_player(sign)
            continue
        else:
            cells[int(value) - 1] = sign
            global move
            move += 1
            drow_board()
            win_case()
            game_draw()


break_flag = True
move = 1
drow_board()
do_input('O')
