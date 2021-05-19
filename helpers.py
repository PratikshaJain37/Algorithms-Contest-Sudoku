'''
Algorithms Contest: Sudoku - Helpers Script
Author: Pratiksha Jain
'''
import pygame
from backtrack import Grid, Cube
import time
pygame.font.init()

colour_dict = {0:(255,0,0), 1:(0,25,0), 2:(0,50,0), 3:(0,75,0), 4:(0,100,0),5:(0,125,0), 6:(0,150,0), 7:(0,175,0), 8:(0,200,0), 9:(0,225,0)}


# 
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
def printBoard(s) : 
        model = s.model
        print("    1 2 3     4 5 6     7 8 9")
        for i in range(9) : 
            if i%3 == 0  :#and i != 0:
                print("  - - - - - - - - - - - - - - ")

            for j in range(9) : 
                if j %3 == 0 :#and j != 0 : 
                    print(" |  ", end = "")
                if j == 8 :
                    print(model[i][j]," | ", i+1)
                else : 
                    print(f"{ model[i][j] } ", end="")
        print("  - - - - - - - - - - - - - - ")

def getMappedMatrix() : 
    matrix = [[0 for cols in range(9)] 
    for rows in range(9)]

    count = 1
    for rows in range(9) : 
        for cols in range(9):
            matrix[rows][cols] = count
            count+=1
    return matrix

    

def graphColoringInitializeColor(SudokuBoard, sudokuGraph, mappedGrid):
    """
    fill the already given colors
    """
    color = [0] * (sudokuGraph.graph.totalV+1)
    given = [] # list of all the ids whos value is already given. Thus cannot be changed
    for row in range(len(SudokuBoard.board)) : 
        for col in range(len(SudokuBoard.board[row])) : 
            if SudokuBoard.board[row][col] != 0 : 
                #first get the idx of the position
                idx = mappedGrid[row][col]
                #update the color
                color[idx] = SudokuBoard.board[row][col] # this is the main imp part
                given.append(idx)
    
    return color, given

def solveGraphColoring(SudokuBoard,sudokuGraph,mappedGrid, width, height, win,start, m=9) : 

    color, given = graphColoringInitializeColor(SudokuBoard, sudokuGraph, mappedGrid)

    color = [[Cube(color[i*9+j+1], i,j,width,height) for j in range(9)] for i in range (9)]

    """
    for i in range(9):
        for j in range(9):
            print(color[i][j].value, end="")
    """
    
    if graphColorUtility(SudokuBoard, sudokuGraph,m, color, 1, given,start=start, win=win) is None :
        print(":(")
        return False
    #print(color)

    update_gui_board(SudokuBoard, color, start, win)
    
    return True

def update_gui_board(SudokuBoard, color,start,win, width=540, height=600):

    #color = [[Cube(color[i*9+j+1], i,j,width,height) for j in range(9)] for i in range (9)] #

    SudokuBoard.cubes = color
    SudokuBoard.update_model()
    SudokuBoard.draw()
    
    #printBoard(SudokuBoard)
    update_time(win, round(time.time() - start))
    pygame.display.update()
    pygame.time.delay(200)
    
    

def graphColorUtility(SudokuBoard,sudokuGraph, m, color, v, given, start, win,width=540, height=600) :

    #print('1')
    if v == sudokuGraph.graph.totalV+1  : 
        return True
    for c in range(1, m+1) : 
        if isSafe2Color(sudokuGraph, v, color, c, given) == True :
            # draw_change
            color[(v-1)//9][(v-1)%9].set(c)
            #color[v] = c
            # color is list of cubes
            #color = [[Cube(color[i*9+j+1], i,j,width,height) for i in range(9)] for j in range (9)]
            color[(v-1)//9][(v-1)%9].draw_change(win, colour=colour_dict[c]) 
            
            update_gui_board(SudokuBoard, color, start, win)
            
            if graphColorUtility(SudokuBoard, sudokuGraph,m, color, v+1, given, start, win) : 
                return True
        if v not in given : 
            # draw_change but with a different colour

            color[(v-1)//9][(v-1)%9].set(0)
            color[(v-1)//9][(v-1)%9].draw_change(win, colour=colour_dict[c]) 
            pygame.display.update()
            #update_gui_board(SudokuBoard, color, start, win)

           
        

def isSafe2Color(sudokuGraph, v, color, c, given) : 
    
    if v in given and color[(v-1)//9][(v-1)%9].value == c: 
        return True
    elif v in given : 
        return False
    #
    for i in range(1, sudokuGraph.graph.totalV+1) :
        #print(i)
        #print((i-1)//9,(i-1)%9)
        if color[(i-1)//9][(i-1)%9].value == c and sudokuGraph.graph.isNeighbour(v, i) :
            return False
    return True


