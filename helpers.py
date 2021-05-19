'''
Algorithms Contest: Sudoku - Helpers Script
Author: Pratiksha Jain
'''
import pygame
from backtrack import Grid, Cube
from graph import SudokuConnections
import time
pygame.font.init()

colour_dict = {0:(255,0,0), 1:(0,95,115), 2:(5,121,133), 3:(10,147,150), 4:(148,210,189),5:(191,213,178), 6:(233,216,166), 7:(238,155,0), 8:(220,129,1), 9:(124,151,75)}


def get_board():
    board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]
    return board

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None

# pos is (i,j)
def valid(bo, num, pos): 
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True

# gui helpers #

def format_time(secs):
    sec = secs%60
    minute = secs//60
    hour = minute//60

    mat = " " + str(minute) + ":" + str(sec)
    return mat
    
def update_time(win, time):
    fnt = pygame.font.SysFont("comicsans", 40)
    
    text = fnt.render("Time: " + format_time(time), 1, (0,0,0))
    text_rect = text.get_rect()
    text_rect.topleft = (540 - 160, 560)
    win.fill((255,255,255),text_rect)
    win.blit(text, text_rect)


# graph helpers functions 

def initializeBoard(s):

    sudokuGraph = SudokuConnections()
    color = [[Cube(s.board[i][j], i,j, s.width, s.height) for j in range(9)] for i in range (9)]

    given = []
    for row in range(9):
        for col in range(9):
            if s.board[row][col] != 0:
                given.append(row*9+col)
                
                # gui
                color[row][col].draw_change(s.win, colour_dict[s.board[row][col]])    

    s.cubes = color

    return given, sudokuGraph


# validating function
def isSafe2Color(sudokuGraph, v, color, c, given) : 
    
    if v in given and color[v//9][v%9].value == c: 
        return True
    elif v in given : 
        return False

    for i in range(0, sudokuGraph.graph.totalV) :
 
        if color[i//9][i%9].value == c and sudokuGraph.graph.isNeighbour(v+1, i+1) :
            return False
    return True


