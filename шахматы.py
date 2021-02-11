



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
            with open("text.txt", "r") as file:
                first_line = file.readline()
                print(first_line)
                second_line = file.readline()
                print(second_line)
                third_line = file.readline()
                print(third_line)

        elif move_vertical == black_figure_vertical:
            with open("text.txt", "r") as file:
                first_line = file.readline()
                print(first_line)
        else:
            with open("text.txt", "r") as file:
                second_line = file.readline()
                print(second_line)


    else:
        with open("text.txt", "r") as file:
            third_line = file.readline()
        print(third_line)












