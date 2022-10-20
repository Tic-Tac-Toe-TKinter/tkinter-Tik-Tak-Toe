import tkinter as tk
import tkinter.font as font
from tkinter import *
from eventhandler import EventHandler
from random import randint

root = Tk()


def bot_second_level(lst1: list[list[int]], val: int):
    """
    Function for player to play against computer with easy level. Input argument is list of lists of integers
    that represents all X: 1 and O: 2 on the board. It returns the list with new value of val

    :param lst1: list of lists of integers(0: empty, 1: X, 2: O) that represents the game board
    :param val: value to play for as computer
    :return: list with added value(val) to any row or column
    """
    oppositeValue = 1 if val == 2 else 2
    # check if there are two values of other player in this row, if yes place other third value
    for i in range(len(lst1)):
        if sum(lst1[i]) == oppositeValue * 2 and lst1[i].count(0) == 1:
            lst1[i][lst1[i].index(0)] = val
            print("two values in a row")
            return None

    # check if there are two values of other player in this column, if yes place other third value
    for i in range(len(lst1)):
        if sum([lst1[0][i], lst1[1][i], lst1[2][i]]) == oppositeValue * 2:
            for j in range(3):
                if lst1[j][i] == 0:
                    lst1[j][i] = val
                    print("two values in a column")
                    return None

    # check if there are two values of other player on the cross lines, if yes place other third value
    if sum([lst1[0][0], lst1[1][1], lst1[2][2]]) == oppositeValue * 2 and 0 in [lst1[0][0], lst1[1][1], lst1[2][2]]:
        for i in range(3):
            if lst1[i][i] == 0:
                lst1[i][i] = val
                print("two values in a line left right")
                return None

    elif sum([lst1[0][2], lst1[1][1], lst1[2][0]]) == oppositeValue * 2 and 0 in [lst1[0][0], lst1[1][1], lst1[2][2]]:
        for i in range(3):
            if lst1[i][2 - i] == 0:
                lst1[i][2 - i] = val
                print("two values in a line right left")
                return None

    # place val to random place in this row if it is empty
    if sum(lst1[0]) == 0:
        lst1[0][randint(0, 2)] = val
    elif sum(lst1[1]) == 0:
        lst1[1][randint(0, 2)] = val
    elif sum(lst1[2]) == 0:
        lst1[2][randint(0, 2)] = val
    return None


def bot_first_level(lst1: list[list[int]], val: int) -> None:
    """
    Function for player to play against computer with easy level. Input argument is list of lists of integers
    that represents all X: 1 and O: 2 on the board. It returns the list with new value of val

    :param lst1: list of lists of integers(0: empty, 1: X, 2: O) that represents the game board
    :param val: value to play for as computer
    :return: None
    """
    while True:
        x = randint(0, 3)
        y = randint(0, 3)
        if lst1[x][y] != 0:
            continue
        else:
            lst1[x][y] = val
            break


def win_check() -> None:
    """

    :return:
    """
    for k in range(3):
        if game[0][k] + game[1][k] + game[2][k] == 3:
            print("X - won")
            break
        elif game[0][k] + game[1][k] + game[2][k] == -3:
            print("O - won")
            break

    for i in game:  # Checking for rows and diagonals
        if i[0] + i[1] + i[2] == 3 or game[0][0] + game[1][1] + game[2][2] == 3 or game[0][2] + game[1][1] + game[2][
            0] == 3:
            print("X - won")
            break
        elif i[0] + i[1] + i[2] == -3 or game[0][0] + game[1][1] + game[2][2] == -3 or game[0][2] + game[1][1] + \
                game[2][0] == -3:
            print("O - won")
            break


if __name__ == '__main__':
    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack()

    labels = [['1 a', '1 b', '1 c'],
              ['2 a', '2 b', '2 c'],  # game board organized in a grid
              ['3 a', '3 b', '3 c']]

    game = [[0, 0, 0],
            [0, 0, 0],  # game scores organized in a grid
            [0, 0, 0]]
    # label = root.Label(background="black")
    turn = 1
    myFont = font.Font(size=20)
    for r in range(3):
        for c in range(3):

            def tkk(x=labels[r][c]):
                global game
                global turn
                roww = 0
                column = 0

                turn *= -1

                for i in range(3):
                    if x.find(chr(97 + i)) == 2:
                        column = i  # detecting the column by letters after the click
                        roww = int(x.split()[0]) - 1  # detecting the row by num after the click
                        break

                game[roww][column] = turn  # connecting the number of the button with the element in the list of lists
                cell = str(roww) + str(column)

                new_button = tk.Button(frame, width="10", height="10", padx=10)

                if turn == 1:  # Creation of a new button with the symbol (depends on turn)
                    new_button.config(text="x")
                    new_button['font'] = myFont
                    new_button.grid(row=roww, column=column)
                else:
                    new_button.config(text="O")
                    new_button['font'] = myFont
                    new_button.grid(row=roww, column=column)

                # button.getattribute("text")
                print(cell)
                print(game)
                win_check()


            button = tk.Button(frame, width="10", height="10", padx=10,
                               text=labels[r][c], command=tkk)
            button['font'] = myFont
            button.grid(row=r, column=c)

    # print(frame.grid(row=1, column=2).getattr())
    root.mainloop()

# CheckButton(bitmap)
root.mainloop()
