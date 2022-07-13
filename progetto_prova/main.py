from tokenize import String
from chess import E4
import numpy as np
from valuta import valuta
from posizioni_valide import *
from genera_mosse import modifica_board


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
board[4][4] = "nR"
board[7][5] = "nA"
board[7][6] = "nC"
board[7][7] = "nT"


for j in range(8):
    board[6][j] = "nP"



def main():
    stampa_board(board)
    print("---------------------------Digitare la mossa con la seguente codifica PNG in italiano---------------------------")

    

    while(1):
        ret = -1
        while(ret == -1):
            mossa_bianco = input('Digitare la propria mossa (bianco):  ')
            ret = modifica_board(board,mossa_bianco,"b")
            stampa_board(board)
        ret = -1
        while(ret == -1):
            mossa_nero = input('Digitare la propria mossa (nero):  ')
            ret = modifica_board(board,mossa_nero,"n")
            stampa_board(board)


main()