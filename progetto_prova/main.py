from tokenize import String
from chess import E4
import numpy as np
from valuta import valuta
from posizioni_valide import *
from genera_mosse import modifica_board
from minimax import *
from draw import *


#inizializzo la scacchiera implementata come array bidimensionale


def stampa_board(board):
    s = ""
    print("a  b  c  d  e  f  g  h")
    print()
    for i in range(8):
        for j in range(8):
            if(board[i][j] == ''):
                s+="-- "
            else:
                s+=board[i][j] + " "
        s+= "  "
        s+= str(i+1)
        s+="\n"
    print(s)


board = [["" for i in range(8)] for j in range(8)]

#pezzi bianchi

board[0][0] = "bT"
board[0][1] = "bC"
board[0][2] = "bA"
board[0][3] = "bQ"
board[0][4] = "bR"
board[0][5] = "bA"
board[0][6] = "bC"
board[0][7] = "bT"


for j in range(8):
    board[1][j] = "bP"


#pezzi neri

board[7][0] = "nT"
board[7][1] = "nC"
board[7][2] = "nA"
board[7][3] = "nQ"
board[7][4] = "nR"
board[7][5] = "nA"
board[7][6] = "nC"
board[7][7] = "nT"


for j in range(8):
    board[6][j] = "nP"



def main():
    t = 1
    scacco = False
    stampa_board(board)
    print(valuta(board))
    print("---------------------------Digitare la mossa con la seguente codifica PNG in italiano---------------------------")

    while(not scacco):
        print("Turno: ",end=" ")
        print(t)
        t+=1

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

        ret = -1
        while(ret == -1 and not scacco):
            #mossa_bianco = minimax_init_bianco(board)
            mossa_bianco = input('Digitare la propria mossa (bianco):  ')
            print("mossa_bianco: ",end=" ")
            print(mossa_bianco)
            #ret = modifica_board(board,mossa_bianco[1],"b")
            ret = modifica_board(board,mossa_bianco,"b")
            stampa_board(board)
            if(ret == 10):
                scacco = True
                print("Il bianco ha vinto!!!")
            #draw(board)
        ret = -1
        while(ret == -1 and not scacco):
            #mossa_nero = input('Digitare la propria mossa (nero):  ')
            mossa_nero = minimax_init_nero(board)
            print("mossa_nero: ",end=" ")
            print(mossa_nero)
            ret = modifica_board(board,mossa_nero[1],"n")
            #ret = modifica_board(board,mossa_nero,"n")
            stampa_board(board)
            if(ret == 11):
                scacco = True
                print("Il nero ha vinto!!!")
            #draw(board)

    
    
main()