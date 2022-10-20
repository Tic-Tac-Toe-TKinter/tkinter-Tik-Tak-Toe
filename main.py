from tkinter import Tk, Label, Button, Frame
import tkinter.font as font
from tkinter import *
from random import randint
from PIL import ImageTk, Image
from sys import exit
root = Tk()


def changer(value: int, row_1: int, column_1: int, font_size: font) -> None:
    """
     Function to change the existing empty button to new one with value of User

    :param value: value to put into the square
    :param row_1: row as an index where to place new button
    :param column_1: row as an index where to place new button
    :param font_size: styles of font to use in button
    :return:
    """
    button_to_change = Button(root, width="10", height="5", padx=10)
    if value == 1:  # Creation of a new button with the symbol (depends on turn)
        button_to_change.config(image=img)
        button_to_change['font'] = font_size
        button_to_change.grid(row=row_1, column=column_1)
    else:
        button_to_change.config(text="O")
        button_to_change['font'] = font_size
        button_to_change.grid(row=row_1, column=column_1)


def bot_second_level(lst1: list[list[int]], userValue: int, font_size: font) -> None:
    """
    Function for player to play against computer with easy level. Input argument is list of lists of integers
    that represents all X: 1 and O: -1 on the board. It returns the list with new value of val

    :param font_size: set-ups of the font to use in button
    :param button_to_change: variable of Button class to be added to game board after move
    :param lst1: list of lists of integers(0: empty, 1: X, -1: O) that represents the game board
    :param userValue: value to play for as computer
    :return: list with added value(val) to any row or column
    """
    botValue = 1 if userValue == -1 else -1
    # check if there are two values of other player in this row, if yes place other third value
    for i in range(len(lst1)):
        if sum(lst1[i]) == userValue * 2 and lst1[i].count(0) == 1:

            changer(botValue, i, lst1[i].index(0), font_size)
            lst1[i][lst1[i].index(0)] = botValue

            return None

    # check if there are two values of other player in this column, if yes place other third value
    for i in range(len(lst1)):
        if sum([lst1[0][i], lst1[1][i], lst1[2][i]]) == userValue * 2:
            for j in range(3):
                if lst1[j][i] == 0:

                    changer(botValue, j, i, font_size)
                    lst1[j][i] = botValue

                    return None

    # check if there are two values of other player on the cross lines, if yes place other third value
    if sum([lst1[0][0], lst1[1][1], lst1[2][2]]) == userValue * 2 and 0 in [lst1[0][0], lst1[1][1], lst1[2][2]]:
        for i in range(3):
            if lst1[i][i] == 0:

                changer(botValue, i, i, font_size)
                lst1[i][i] = botValue

                return None

    elif sum([lst1[0][2], lst1[1][1], lst1[2][0]]) == userValue * 2 and 0 in [lst1[0][0], lst1[1][1], lst1[2][2]]:
        for i in range(3):
            if lst1[i][2 - i] == 0:

                changer(botValue, i, 2-i, font_size)
                lst1[i][2 - i] = botValue

                return None

    # place val to random place in this row if it is empty
    randVal = randint(0, 2)
    if sum(lst1[0]) == 0:
        lst1[0][randVal] = botValue
        changer(botValue, 0, randVal, font_size)
    elif sum(lst1[1]) == 0:
        lst1[1][randVal] = botValue
        changer(botValue, 1, randVal, font_size)
    elif sum(lst1[2]) == 0:
        lst1[2][randVal] = botValue
        changer(botValue, 0, randVal, font_size)
    return None


def bot_first_level(lst1: list[list[int]], userValue: int, font_size: font) -> None:
    """
    Function for player to play against computer with easy level. Input argument is list of lists of integers
    that represents all X: 1 and O: 2 on the board. It returns the list with new value of val

    :param font_size: styles of font to use in button
    :param lst1: list of lists of integers(0: empty, 1: X, 2: O) that represents the game board
    :param userValue: value the user use to play
    :return: None
    """
    botValue = 1 if userValue == -1 else -1

    while True:
        x = randint(0, 2)
        y = randint(0, 2)
        if lst1[x][y] != 0:
            continue
        else:
            lst1[x][y] = botValue
            changer(botValue, x, y, font_size)
            break


def win_check() -> None:
    """
    Function that checks if the game is ended and who wins and then terminate the process

    :return: None
    """
    for k in range(3):
        if game[0][k] + game[1][k] + game[2][k] == 3:
            print("X - won")
            print("game[0][k] + game[1][k] + game[2][k] == 3")
            exit(1)
            break
        elif game[0][k] + game[1][k] + game[2][k] == -3:
            print("O - won")
            print('game[0][k] + game[1][k] + game[2][k] == -3')
            exit(1)
            break

    for i in game:  # Checking for rows and diagonals
        if i[0] + i[1] + i[2] == 3 or game[0][0] + game[1][1] + game[2][2] == 3 or game[0][2] + game[1][1] + game[2][
            0] == 3:
            print("X - won")
            print('3 X in a row or diagonal')
            exit(1)
            break
        elif i[0] + i[1] + i[2] == -3 or game[0][0] + game[1][1] + game[2][2] == -3 or game[0][2] + game[1][1] + \
                game[2][0] == -3:
            print("O - won")
            exit(1)
            break


if __name__ == '__main__':

    img = PhotoImage(file="Cross.png")

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
                row_1 = 0
                column_1 = 0

                # turn *= -1

                for i in range(3):
                    if x.find(chr(97 + i)) == 2:
                        column_1 = i  # detecting the column_1 by letters after the click
                        row_1 = int(x.split()[0]) - 1  # detecting the row by num after the click
                        break

                game[row_1][
                    column_1] = turn  # connecting the number of the button with the element in the list of lists

                cell = str(row_1) + str(column_1)

                changer(turn, row_1, column_1, myFont)

                # bot_second_level(game, turn, myFont)
                bot_first_level(game, turn, myFont)
                # button.getattribute("text")
                print(cell)
                print(game)
                win_check()


            button = Button(root, width="10", height="5", padx=10,
                            text=labels[r][c], command=tkk)
            button['font'] = myFont
            button.grid(row=r, column=c)

    # print(frame.grid(row=1, column=2).getattr())
    root.mainloop()

# CheckButton(bitmap)
