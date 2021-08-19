from tkinter import *
import random


# Кнопка 
# Обработка нажатия на кнопки
def new_game():
    for row in range(3):
        for col in range(3):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = 'Cornsilk'
        global game_end
        game_end = True
        global cross_count
        cross_count = 0

# Случайно опеределяет кто будет ходить первым
def who_goes_first():
    if random.randint(0, 1) == 0:
        return 'компьютер'
    else:
        return 'игрок'

# Начало игры
def clicked(row, col):
    if game_end and field[row][col]['text'] == ' ':
        field[row][col]['text'] = 'X'
        global cross_count
        cross_count += 1
        # Добавляем проверку на выигрыш
        check_wins('X')
        if game_end and cross_count < 5:
            computer_step()
            check_wins('O')

# Проверка выигрыша
def check_wins(symbol):
    for i in range(3):
        check_line(field[i][0], field[i][1], field[i][2], symbol)
        check_line(field[0][i], field[1][i], field[2][i], symbol)
    check_line(field[0][0], field[1][1], field[2][2], symbol)
    check_line(field[2][0], field[1][1], field[0][2], symbol)

def check_line(col_1, col_2, col_3, symbol):
    if col_1['text'] == symbol and col_2['text'] == symbol and col_3['text'] == symbol:
        col_1['background'] = col_2['background'] = col_3['background'] = 'Maroon'
        global game_end
        game_end = False

# Ходы компьютера
def computer_can_win(col_1, col_2, col_3, symbol):
    result = False
    if col_1['text'] == ' ' and col_2['text'] == symbol and col_3['text'] == symbol:
        col_1['text'] = 'O'
        result = True
    if col_1['text'] == symbol and col_2['text'] == ' ' and col_3['text'] == symbol:
        col_2['text'] = 'O'
        result = True
    if col_1['text'] == symbol and col_2['text'] == symbol and col_3['text'] == ' ':
        col_3['text'] = 'O'
        result = True
    return result

def computer_step():
    for i in range(3):
        if computer_can_win(field[i][0], field[i][1], field[i][2], 'O'):
            return
        if computer_can_win(field[0][i], field[1][i], field[2][i], 'O'):
            return
    if computer_can_win(field[0][0], field[1][1], field[2][2], 'O'):
        return
    if computer_can_win(field[2][0], field[1][1], field[0][2], 'O'):
        return
    for i in range(3):
        if computer_can_win(field[i][0], field[i][1], field[i][2], 'X'):
            return
        if computer_can_win(field[0][i], field[1][i], field[2][i], 'X'):
             return
    if computer_can_win(field[0][0], field[1][1], field[2][2], 'X'):
        return
    if computer_can_win(field[2][0], field[1][1], field[0][2], 'X'):
        return
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if field[row][col]['text'] == ' ':
            field[row][col]['text'] = 'O'
            break

root = Tk()
root.title('Tic Tak Toe')
game_end = True  # Записываем False при завершении игры, чтобы запретить дальнейшие ходы
field = []  # Поле, в котором хранятся кнопки
cross_count = 0  #  Отслеживание количества крестиков. По выставлению 5 кретика в случае, когда никто не выиграл фиксировать ничью

# Внешний вид
for row in range(3):
    line = []
    for col in range(3):
        button = Button(root, text = ' ', width = 4, height = 2,
                        font =('Arial Bold', 20, 'bold'),
                        background = 'Cornsilk',
                        command = lambda row=row, col=col: clicked(row, col))
        button.grid(row=row, column=col, sticky = 'nsew')
        line.append(button)
    field.append(line)

new_button = Button(root, text = 'Начать заново', command = new_game,
                    background = 'SandyBrown',
                    font =('Arial Bold', 10, 'bold'))
new_button.grid(row = 3, column = 0, columnspan = 3, sticky= 'nsew')
          
root.mainloop()  # Запускает бесконечный цикл окна, пока сами не закроем