import pygame



pygame.init()

display_width = 600
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Chess')

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
scacco_matto = False
boardIMG = pygame.image.load('img/chessboard.png').convert_alpha()

pedIMG_n = pygame.image.load('img/pedone.png').convert_alpha()
pedIMG_b = pygame.image.load('img/pedone_b.png').convert_alpha()

cavIMG_b = pygame.image.load('img/cavallo_b.png').convert_alpha()
cavIMG_n = pygame.image.load('img/cavallo.png').convert_alpha()

alfIMG_b = pygame.image.load('img/alfiere_b.png').convert_alpha()
alfIMG_n = pygame.image.load('img/alfiere.png').convert_alpha()

torreIMG_b = pygame.image.load('img/torre_b.png').convert_alpha()
torreIMG_n = pygame.image.load('img/torre.png').convert_alpha()

reginaIMG_b = pygame.image.load('img/regina_b.png').convert_alpha()
reginaIMG_n = pygame.image.load('img/regina.png').convert_alpha()

reIMG_b = pygame.image.load('img/re_b.png').convert_alpha()
reIMG_n = pygame.image.load('img/re.png').convert_alpha()



def board_chess(x,y):
    gameDisplay.blit(boardIMG, (x,y))
x = 0
y = 0


def pedone_n(xi,yi):
    gameDisplay.blit(pedIMG_n, (xi,yi))

def cavallo_n(xi,yi):
    gameDisplay.blit(cavIMG_n, (xi,yi))

def alfiere_n(xi,yi):
    gameDisplay.blit(alfIMG_n, (xi,yi))

def torre_n(xi,yi):
    gameDisplay.blit(torreIMG_n, (xi,yi))

def re_n(xi,yi):
    gameDisplay.blit(reIMG_n, (xi,yi))

def regina_n(xi,yi):
    gameDisplay.blit(reginaIMG_n, (xi,yi))

def pedone_b(xi,yi):
    gameDisplay.blit(pedIMG_b, (xi,yi))

def cavallo_b(xi,yi):
    gameDisplay.blit(cavIMG_b, (xi,yi))

def alfiere_b(xi,yi):
    gameDisplay.blit(alfIMG_b, (xi,yi))

def torre_b(xi,yi):
    gameDisplay.blit(torreIMG_b, (xi,yi))

def re_b(xi,yi):
    gameDisplay.blit(reIMG_b, (xi,yi))

def regina_b(xi,yi):
    gameDisplay.blit(reginaIMG_b, (xi,yi))

def draw(board):

    while not scacco_matto:
        
        gameDisplay.fill(black)
        board_chess(x,y)
        for i in range(8):
            for j in range(8):
                if(board[i][j] == "nP"):
                    pedone_n(j*75,i*75)
                if(board[i][j] == "bP"):
                    pedone_b(j*75,(i)*75)
                if(board[i][j] == "nC"):
                    cavallo_n(j*75,i*75)
                if(board[i][j] == "bC"):
                    cavallo_b(j*75,(i)*75)
                if(board[i][j] == "nA"):
                    alfiere_n(j*75,i*75)
                if(board[i][j] == "bA"):
                    alfiere_b(j*75,(i)*75)
                if(board[i][j] == "nT"):
                    torre_n(j*75,i*75)
                if(board[i][j] == "bT"):
                    torre_b(j*75,(i)*75)
                if(board[i][j] == "nR"):
                    re_n(j*75,i*75)
                if(board[i][j] == "bR"):
                    re_b(j*75,(i)*75)
                if(board[i][j] == "nQ"):
                    regina_n(j*75,i*75)
                if(board[i][j] == "bQ"):
                    regina_b(j*75,(i)*75)

            
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()