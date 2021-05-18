'''
Algorithms Contest: Sudoku - Main Script
Author: Pratiksha Jain
'''

import pygame
import time
from helpers import get_board, update_time
from solvers import backtrack_gui, graph_coloring_gui
from backtrack import Grid

import getopt
import sys

start = time.time()

# For processing Command Line Arguments
args = sys.argv

try:
    method = args[1] 
except:
    print('ERROR: Invalid Input')
    exit()

def main():
    global start
    win = pygame.display.set_mode((540,600))
    win.fill((255,255,255))
    pygame.display.set_caption("Sudoku")
    board = Grid(get_board(), 540, 540, win)
    run = True
    
    while run:

        play_time = round(time.time() - start)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_SPACE:
                    if method == 'backtrack':
                        backtrack_gui(board, start)
                    elif method == 'graph':
                        graph_coloring_gui(board, start)
                    win.fill((255,255,255))

        # draw grid
        board.draw()     
        # draw time   
        update_time(win, play_time)
        # update display
        pygame.display.update()


main()
pygame.quit()
