import pygame
import sys
from settings import Settings

x = 0
y = 0
grid =[
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
# grid =[
#         [8, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 3, 6, 0, 0, 0, 0, 0],
#         [0, 7, 0, 0, 9, 0, 2, 0, 0],
#         [0, 5, 0, 0, 0, 7, 0, 0, 0],
#         [0, 0, 0, 0, 4, 5, 7, 0, 0],
#         [0, 0, 0, 1, 0, 0, 0, 3, 0],
#         [0, 0, 1, 0, 0, 0, 0, 6, 8],
#         [0, 0, 8, 5, 0, 0, 0, 1, 0],
#         [0, 9, 0, 0, 0, 0, 4, 0, 0]
# ]
class Sudoku:
    def __init__(self):
        self.settings = Settings()
        pygame.init()
        screen_size = self.settings.grid_width*9 + self.settings.thick_bar *4 + self.settings.thin_bar*6
        self.screen = pygame.display.set_mode(size=(screen_size,screen_size))
        self.bg_colour = (self.settings.bg_colour)

    def draw_board(self):
        cor = 0
        for i in range(0,9):
            for j in range(0,9):
                text = self.settings.font.render(str(grid[i][j]),True ,(0,0,0))
                text_rect = text.get_rect()
                text_rect.topleft = (self.settings.grid_width*i + self.settings.thick_bar*(int(i/3)+1) + self.settings.thin_bar*(i-int(i/3)), self.settings.grid_width*j + self.settings.thick_bar*(int(j/3)+1) + self.settings.thin_bar*(j-int(j/3)))
                self.screen.blit(text,text_rect)
        for i in range(0,10):
            if i % 3 == 0:
                thick = self.settings.thick_bar
            else:
                thick = self.settings.thin_bar
            bar1 = pygame.Rect(cor,0, thick, 500)
            bar2 = pygame.Rect(0, cor, 500, thick)
            pygame.draw.rect(self.screen, (0,0,0), bar1)
            pygame.draw.rect(self.screen, (0,0,0), bar2)
            cor += thick
            cor += self.settings.grid_width

    def draw_box(self):
        tl_x = x * self.settings.grid_width + (int(x / 3) + 1) *self.settings.thick_bar + (x - int(x / 3)) * self.settings.thin_bar - self.settings.thick_bar
        tl_y = y * self.settings.grid_width + (int(y / 3) + 1) *self.settings.thick_bar + (y - int(y / 3)) * self.settings.thin_bar  - self.settings.thick_bar
        length = self.settings.grid_width + 2 * self.settings.thick_bar
        distance = self.settings.grid_width + self.settings.thick_bar
        for i in range(2):
            box_hor = pygame.Rect(tl_x + i*distance,tl_y, self.settings.thick_bar, length)
            box_ver = pygame.Rect(tl_x,tl_y+ i*distance, length, self.settings.thick_bar)
            pygame.draw.rect(self.screen, (0,128,0),box_ver)
            pygame.draw.rect(self.screen, (0,128,0),box_hor)
    
    def is_valid(self, grid, i, j, num):
        for k in range(0,9):
            if  grid[i][k] == num:
                return False
            if grid[k][j] == num:
                return False
        i -= i % 3
        j -= j % 3
        for k in range(0,3):
            for h in range(0,3):
                if grid[k+i][j+h] == num:
                    return False
        return True
    
    def solve(self,grid,i,j):
        self.check_events()
        while grid[i][j] != 0:
            if i< 8:
                i += 1
            elif i == 8 and j < 8:
                j += 1
                i = 0 
            else:
                return True

        for num in range(1,10):
            if self.is_valid(grid,i,j,num) == True:
                global x,y
                x = i -1
                y = j -1
                grid[i][j] = num
                self.update_screen()
                pygame.time.delay(20)
                if self.solve(grid,i,j) != False:
                    return True
                else:
                    grid[i][j] = 0
                self.update_screen()
        return False

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update_screen(self):
        self.screen.fill((self.bg_colour))
        self.draw_board()
        self.draw_box()
        pygame.display.update()

    def run_game(self):
        while True:
           # pygame.event.get() 
            self.check_events()
            self.update_screen()
            self.solve(grid,0,0)

if __name__ == "__main__":
    settings = Settings()
    
    sudoku = Sudoku()
    sudoku.run_game() 