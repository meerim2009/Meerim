1) создать список ходов коня
2)



white_figure_vertical = int(input("Введите позицию белой фигуры по вертикали"))
white_figure_horizontal = int(input("Введите позицию белой фигуры по горизонтали"))

black_figure_vertical = int(input("Введите позицию черной фигуры по вертикали"))
black_figure_horizontal = int(input("Введите позицию черной фигуры по горизонтали"))

move_vertical = int(input("Куда пойдем по вертикали"))
move_horizontal = int(input("Куда пойдем по горизонтали"))

which_figure = input("Какой фигурой ходим")
if which_figure == "ладья":
    if move_horizontal == white_figure_horizontal or move_vertical == white_figure_vertical:
        if move_horizontal == black_figure_horizontal:
            print("Вы не можете ходить")

        elif move_vertical == black_figure_vertical:
            print("Вы не можете ходить")
        else:
            print("Вы можете ходить")

    else:
        print("Так ходить нельзя")
kon_vertical = white_figure_vertical - black_figure_vertical
kon_horizontal = white_figure_horizontal - black_figure_horizontal
if which_figure == "конь":  # kon i kon
    if white_figure_vertical < 0:
       white_figure_vertical = -black_figure_vertical
    if white_figure_horizontal > 0:
       white_figure_horizontal = -black_figure_horizontal





# subtraction
sub_a = a - aa
sub_b = b - bb

if sub_a < 0:
    sub_a = -sub_a
if sub_b < 0:
    sub_b = -sub_b

if a == b == aa == bb:
    print('The same point')
elif a <= 0 or b <= 0 or aa <= 0 or bb <= 0 or a > 8 or aa > 8 or b > 8 or bb > 8:
    print('Error, wrong point')

if sub_a == 1 and sub_b == 2 or sub_a == 2 and sub_b == 1:
    print('Yes')
else:
    print('No')





