'''
Algorithms Contest: Sudoku - GUI Helpers Script
Author: Pratiksha Jain
'''




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

