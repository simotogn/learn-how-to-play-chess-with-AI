from tokenize import String
from chess import E4
import numpy as np
from valuta import valuta
from posizioni_valide import *
from genera_mosse import modifica_board
from minimax import *
#from draw import *



#inizializzo la scacchiera implementata come array bidimensionale


def stampa_board(board):
    s = ""
    print("a b c d e f g h")
    print()
    for i in range(8):
        for j in range(8):
            if(board[i][j] == ''):
                s+=". "
            else:
                if(board[i][j][0]== "n"):
                    s+=board[i][j][1].lower() + " "
                else:
                    s+=board[i][j][1] + " "
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
    scacco_matto = False
    stampa_board(board)
    print(valuta(board))
    print("---------------------------Digitare la mossa con la  codifica PNG in italiano---------------------------")

    scelta = ""
    while(scelta == ""):
        scelta = input("Con che colore vuoi giocare? (b, n, nessuno): ")
        if(scelta == "b"):
            scelta = "b"
        elif(scelta == "n"):
            scelta = "n"
        elif(scelta == "nessuno"):
            scelta = "nessuno"
        else:
            scelta = ""
    d = 0
    while(d == 0):
        d = input("Scegliere la profondità del minimax (conisgliato da 2 a 4): ")
    if(scelta == "nessuno"):
        d2 = 0
        while(d2 == 0):
            d2 = input("Scegliere la profondità del minimax (conisgliato da 2 a 4): ")
    else:
        d2 = d

    while(not scacco_matto):
        print("Turno: ",end=" ")
        print(t)
        t+=1
        
        if(scelta == "b"):
            ret = -1
            while(ret == -1 and not scacco_matto):
                mossa_bianco = input('Digitare la propria mossa (bianco):  ')
                print("mossa_bianco: ",end=" ")
                print(mossa_bianco)
                ret = modifica_board(board,mossa_bianco,"b")
                stampa_board(board)
                if(ret == 10):
                    scacco_matto = True
                    print("Il bianco ha vinto!!!")
        
        elif(scelta == "nessuno" or scelta == "n"):
            ret = -1
            while(ret == -1 and not scacco_matto):
                mossa_bianco = minimax_init_bianco(board,int(d))
                print("mossa_bianco: ",end=" ")
                print(mossa_bianco)
                ret = modifica_board(board,mossa_bianco[1],"b")
                stampa_board(board)
                if(ret == 10):
                    scacco_matto = True
                    print("Il bianco ha vinto!!!")
        
        if(scelta == "n"):
            ret = -1
            while(ret == -1 and not scacco_matto):
                mossa_nero = input('Digitare la propria mossa (nero):  ')
                print("mossa_nero: ",end=" ")
                print(mossa_nero)
                ret = modifica_board(board,mossa_nero,"n")
                stampa_board(board)
                if(ret == 11):
                    scacco_matto = True
                    print("Il nero ha vinto!!!")
        if(scelta=="nessuno" or scelta == "b"):
            ret = -1
            while(ret == -1 and not scacco_matto):
                mossa_nero = minimax_init_nero(board,int(d2))
                print("mossa_nero: ",end=" ")
                print(mossa_nero)
                ret = modifica_board(board,mossa_nero[1],"n")
                stampa_board(board)
                if(ret == 11):
                    scacco_matto = True
                    print("Il nero ha vinto!!!")     

 
main()