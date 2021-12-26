
from pygame.constants import MOUSEBUTTONDOWN
import pygame
import sudoku

class Box:

    locked = False

    def __init__(self, value, row, column):

        self.value = value
        self.row = row
        self.column = column

        #self.value = sudoku_grid[row][column]

        self.width = 20 * 1.5
        self.height = 20 * 1.5

        self.x = self.column * self.width + sudoku.screen_center[0] - 9 * self.width / 2
        self.y = self.row * self.height + sudoku.screen_center[1] - 9 * self.height / 2

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def __repr__(self):

        return f"value: { self.value }, row: { self.row } , column: { self.column }"

    def draw_values(self):

        pygame.draw.rect(pygame.display.get_surface(),(255,0,0),(self.rect))

        text = pygame.font.Font('freesansbold.ttf', 20).render(str(self.value), True, (0,0,0))

        textRect = text.get_rect()
        textRect.center = ((self.x + self.width / 2), (self.y + self.height / 2))
        
        screen = pygame.display.get_surface()

        screen.blit(text, textRect)

    def check_mouse_clicks(self):

        for event in pygame.event.get():

            if event.type == MOUSEBUTTONDOWN and event.button == 1:

                if self.rect.collidepoint(pygame.mouse.get_pos()):

                    self.value += 1
                    print("value +1")

            if event.type == MOUSEBUTTONDOWN and event.button == 3:

                if self.rect.collidepoint(pygame.mouse.get_pos()):

                    self.value += -1
                    print("value -1")


    def update_value(self):

        self.value = sudoku_grid[self.row][self.column]

    def change_value(new_value, r, c):

        sudoku_grid[r][c] = new_value

    