
from pygame.constants import KEYDOWN, MOUSEBUTTONDOWN, K_a
import pygame
from modules import functions
from modules import box
import sudoku_answers

pygame.init()

#booleans
levelMenu = False
playing = False
correct = False
checked = False

#screen settings
screen = pygame.display.set_mode((800,500))
pygame.display.set_caption('Basic sudoku')

screen_dimensions = pygame.display.get_window_size()
screen_center = (screen_dimensions[0]/2, screen_dimensions[1]/2)

#Menu texts
menu_font = pygame.font.Font('freesansbold.ttf', 80)
level_font = pygame.font.Font('freesansbold.ttf', 55)
button_font = pygame.font.Font('freesansbold.ttf', 32)
small_font = pygame.font.Font('freesansbold.ttf', 22)

play_text = menu_font.render('Play', True, (225,225,225))
quit_text = menu_font.render('Quit', True, (225,225,225))
back_text = button_font.render('<Back', True, (0,0,0))
check_text = button_font.render('Check', True, (0,0,0))
correct_text = button_font.render('Correct solution!', True, (0,0,0))
incorrect_text = button_font.render('Incorrect solution', True, (0,0,0))
instruction_text = button_font.render('left click: +1, right click: -1', True, (0,0,0))
answer_text = button_font.render('Show answer', True, (0,0,0))
levels_text = menu_font.render('Levels:', True, (0,0,0))

level1_text = level_font.render('1', True, (0,0,0))
level2_text = level_font.render('2', True, (0,0,0))
level3_text = level_font.render('3', True, (0,0,0))
level4_text = level_font.render('4', True, (0,0,0))
level5_text = level_font.render('5', True, (0,0,0))
level6_text = level_font.render('6', True, (0,0,0))
level7_text = level_font.render('7', True, (0,0,0))
level8_text = level_font.render('8', True, (0,0,0))

level_list = [level1_text, level2_text, level3_text, level4_text, level5_text, level6_text, level7_text, level8_text]

playRect = play_text.get_rect()
playRect2 = playRect.inflate(10,10)
quitRect = quit_text.get_rect()
quitRect2 = quitRect.inflate(10,10)
backRect = back_text.get_rect()
backRect2 = backRect.inflate(8,8)
checkRect = check_text.get_rect()
checkRect2 = checkRect.inflate(8,8)
answerRect = correct_text.get_rect()
instructionRect = instruction_text.get_rect()
solutionRect = answer_text.get_rect()
solutionRect2 = solutionRect.inflate(8,8)

levelsRect = levels_text.get_rect()

levelRects = [level.get_rect() for level in level_list]

playRect.center = (screen_center[0], screen_center[1] - screen_dimensions[1]/5)
playRect2.center = (screen_center[0], screen_center[1] - screen_dimensions[1]/5)
quitRect.center = (screen_center[0], screen_center[1] + screen_dimensions[1]/5)
quitRect2.center = (screen_center[0], screen_center[1] + screen_dimensions[1]/5)
backRect.center = (screen_center[0] / 3, screen_center[1]*2.5 / 3)
backRect2.center = (screen_center[0] / 3, screen_center[1]*2.5 / 3)
checkRect.center = (screen_center[0] / 3, screen_center[1]*1.2)
checkRect2.center = (screen_center[0] / 3, screen_center[1]*1.2)
answerRect.center = (screen_center[0], screen_center[1] + screen_dimensions[1]/3)
solutionRect.center = (screen_center[0] + screen_dimensions[0]/3, screen_center[1])
solutionRect2.center = (screen_center[0] + screen_dimensions[0]/3, screen_center[1])
instructionRect.center = (screen_center[0], screen_center[1]/5)

levelsRect.center = (screen_center[0], screen_center[1] - screen_dimensions[1]/3)

rectCount = 1

for rect in levelRects:

    if rectCount <= 4:

        rect.center = (screen_dimensions[0] / 4 * rectCount - screen_dimensions[0] / 8, screen_center[1] - screen_dimensions[1]/8)

    else:

        rect.center = (screen_dimensions[0] / 4 * (rectCount - 4) - screen_dimensions[0] / 8, screen_center[1] + screen_dimensions[1]/8)

    rectCount += 1

ids = [i for i in range(1,9)]

levels = tuple(zip(level_list, levelRects, ids))

def draw_menu():

    if playing == False and levelMenu == False:

        pygame.draw.rect(pygame.display.get_surface(),(0,0,0),(playRect2))
        pygame.draw.rect(pygame.display.get_surface(),(0,0,245),(playRect))

        pygame.draw.rect(pygame.display.get_surface(),(0,0,0),(quitRect2))
        pygame.draw.rect(pygame.display.get_surface(),(255,0,0),(quitRect))

        screen.blit(play_text, playRect)
        screen.blit(quit_text, quitRect)

    elif playing == False and levelMenu == True:

        screen.blit(levels_text, levelsRect)

        for level in levels:

            screen.blit(level[0], level[1])

        quitRect.center = (screen_center[0], screen_center[1] + screen_dimensions[1]/3)
        quitRect2.center = (screen_center[0], screen_center[1] + screen_dimensions[1]/3)

        pygame.draw.rect(pygame.display.get_surface(),(0,0,0),(quitRect2))
        pygame.draw.rect(pygame.display.get_surface(),(255,0,0),(quitRect))

        screen.blit(quit_text, quitRect)

    else:

        pygame.draw.rect(pygame.display.get_surface(),(0,0,0),(backRect2))
        pygame.draw.rect(pygame.display.get_surface(),(62,143,224),(backRect))
        screen.blit(back_text, backRect)
        pygame.draw.rect(pygame.display.get_surface(),(0,0,0),(checkRect2))
        pygame.draw.rect(pygame.display.get_surface(),(255,127,0),(checkRect))
        screen.blit(check_text, checkRect)
        pygame.draw.rect(pygame.display.get_surface(),(0,0,0),(solutionRect2))
        pygame.draw.rect(pygame.display.get_surface(),(255,127,0),(solutionRect))
        screen.blit(answer_text, solutionRect)

        screen.blit(instruction_text, instructionRect)

        if checked == True and correct == False:

            screen.blit(incorrect_text, answerRect)

        if checked == True and correct == True:

            screen.blit(correct_text, answerRect)


def draw_values(b):

    border_rect_x = (b.rect[0],b.rect[1],b.rect[2],b.rect[3]/10)
    border_rect_y = (b.rect[0],b.rect[1],b.rect[2]/10,b.rect[3])

    if b in clickable_boxes:

        pygame.draw.rect(pygame.display.get_surface(),(255,255,255),(b.rect))

    else:

        pygame.draw.rect(pygame.display.get_surface(),(0,255,0),(b.rect))

    pygame.draw.rect(pygame.display.get_surface(),(0,0,0),(border_rect_x))
    pygame.draw.rect(pygame.display.get_surface(),(0,0,0),(border_rect_y))


    text = pygame.font.Font('freesansbold.ttf', 20).render(str(b.value), True, (0,0,0))

    textRect = text.get_rect()
    textRect.center = ((b.x + b.width / 2), (b.y + b.width / 2))

    if b.value != 0:

        screen.blit(text, textRect)

if __name__ == "__main__":

    box_list = []

    clickable_boxes = []

    x = 0
    y = 0

    #represents the current level loaded
    level = 1

    clock = pygame.time.Clock()

    while True:

        screen.fill((200,200,200))

        draw_menu()

        if playing == True:

            #draw values from sudoku_grid

            for b in box_list:

                draw_values(b)

            for b in clickable_boxes:

                draw_values(b)

        #handling mouse-events

        for event in pygame.event.get():

            if event.type == MOUSEBUTTONDOWN:

                pos = pygame.mouse.get_pos()

                #start menu

                if playing == False and levelMenu == False:

                    if playRect.collidepoint(pos):
                    
                        levelMenu = True
                        print("moro")

                    if quitRect.collidepoint(pos):

                        pygame.quit()
                        quit()

                #level menu

                if playing == False and levelMenu == True:

                    if quitRect.collidepoint(pos):

                        pygame.quit()
                        quit()

                    clicked_levels = [l for l in levels if l[1].collidepoint(pos)]

                    for level in clicked_levels:

                        functions.print_matrix

                        functions.load_Level(level[2])

                        functions.print_matrix

                        clicked_levels.clear()

                        box_list.clear()
                        clickable_boxes.clear()

                        level = level[2]

                        #make boxes needed for gameplay

                        for row in functions.sudoku_grid:

                            for value in row:

                                box_list.append(box.Box(value, y, x))

                                if value == 0:

                                    clickable_boxes.append(box.Box(value, y, x))
                                    
                                print(value)

                                x += 1

                            y += 1
                            x = 0

                        print(box_list)

                        playing = True
                        levelMenu = False

                    x = 0
                    y = 0

                    #continue so leftclick doesn't change values in the grid in the same loop

                    continue

                #Actual game running

                if playing == True:

                    if backRect.collidepoint(pos):

                        playing = False
                        levelMenu = True
                        checked = False

                    if checkRect.collidepoint(pos):

                        print(functions.sudoku_grid)

                        if functions.check_grid() == True:

                            print("oikea vastaus!")

                            correct = True

                        else:

                            correct = False
                        
                        checked = True

                        print(functions.sudoku_grid)

                    if solutionRect.collidepoint(pos):

                        functions.sudoku_grid = sudoku_answers.sudoku_list[level-1]

                        box_list.clear()
                        clickable_boxes.clear()

                        for row in functions.sudoku_grid:

                            for value in row:

                                box_list.append(box.Box(value, y, x))

                                if value == 0:

                                    clickable_boxes.append(box.Box(value, y, x))
                                    
                                print(value)

                                x += 1

                            y += 1
                            x = 0

                        print(box_list)

                        x = 0
                        y = 0

                    if event.button == 1:

                        clicked_boxes_add = [b for b in clickable_boxes if b.rect.collidepoint(pos)]

                        for b in clicked_boxes_add:

                            if functions.sudoku_grid[b.row][b.column] < 9:

                                functions.sudoku_grid[b.row][b.column] += 1
                                b.value += 1

                            else:

                                functions.sudoku_grid[b.row][b.column] = 1
                                b.value = 1

                    if event.button == 3:

                        clicked_boxes_add = [b for b in clickable_boxes if b.rect.collidepoint(pos)]

                        for b in clicked_boxes_add:

                            if functions.sudoku_grid[b.row][b.column] > 0:

                                functions.sudoku_grid[b.row][b.column] += -1
                                b.value -= 1

                            else:

                                functions.sudoku_grid[b.row][b.column] = 9
                                b.value = 9

            if event.type == pygame.QUIT:

                pygame.quit()

                quit()

            pygame.display.update()
            
        clock.tick(30)