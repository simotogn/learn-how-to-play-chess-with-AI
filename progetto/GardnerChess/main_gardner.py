from minimax_gardner import *
from posizioni_valide_gardner import *
from genera_mosse_gardner import *
from mcts_gardner import *
from tts_gardner import text_to_speech
import time



def stampa_board(board):
    s = ""
    print("a b c d e")
    print()
    for i in range(5):
        for j in range(5):
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


board = [["" for i in range(5)] for j in range(5)]

board[0][0]  = "bT"
board[0][1]  = "bC"
board[0][2]  = "bA"
board[0][3]  = "bQ"
board[0][4]  = "bR"

for i in range(5):
    board[1][i] = "bP"

board[4][0]  = "nT"
board[4][1]  = "nC"
board[4][2]  = "nA"
board[4][3]  = "nQ"
board[4][4]  = "nR"

for i in range(5):
    board[3][i] = "nP"

stampa_board(board)

def main():
    t=1
    scacco_matto = False

    
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
    against = ""
    while((scelta == "b" or scelta == "n") and (against != "mcts" and against != "minimax")):
        against = input("Contro chi vuoi giocare? (minimax o mcts) ")
        if(against == "minimax"):
            d = input("Digitare depth del minimax (consigliato 2/3/4/5): ")
    pl1 = ""
    pl2 = ""
    while(scelta == "nessuno" and (pl1 != "mcts" and pl1 != "minimax")):
        pl1 = input("Chi vuoi che sia il player 1? (minimax o mcts) ")
        if(pl1 == "minimax"):
            d = input("Digitare depth del minimax (consigliato 2/3/4/5): ")
    while(scelta == "nessuno" and (pl2 != "mcts" and pl2 != "minimax")):
        pl2 = input("Chi vuoi che sia il player 2? (minimax o mcts) ")
        if(pl2 == "minimax"):
            d2 = input("Digitare depth del minimax (consigliato 2/3/4/5): ")

    print("---------------------------Digitare la mossa con la codifica PNG in italiano---------------------------")

    while(not scacco_matto):
        print("Turno: ",end=" ")
        print(t)
        print(valuta(board)[0] - valuta(board)[1])
        
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
                if((scelta == "n" and against == "mcts") or (scelta == "nessuno" and pl1=="mcts")):
                    mossa_bianco = mcts("b",board)
                elif((scelta == "n" and against == "minimax") or (scelta == "nessuno" and pl1=="minimax")):
                    mossa_bianco = minimax_init_bianco(board,int(d))[1]
                print("mossa_bianco: ",end=" ")
                print(mossa_bianco)
                text_to_speech(mossa_bianco)
                ret = modifica_board(board,mossa_bianco,"b")
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
                if((scelta == "b" and against == "mcts") or (scelta == "nessuno" and pl2 == "mcts")):
                    mossa_nero = mcts("n",board)
                elif(scelta == "b" and against == "minimax"):
                    mossa_nero = minimax_init_nero(board,int(d))[1]
                elif(scelta == "nessuno" and pl2 == "minimax"):
                    mossa_nero = minimax_init_nero(board,int(d2))[1]
                print("mossa_nero: ",end=" ")
                print(mossa_nero)
                text_to_speech(mossa_nero)
                ret = modifica_board(board,mossa_nero,"n")
                stampa_board(board)
                if(ret == 11):
                    scacco_matto = True
                    print("Il nero ha vinto!!!")

    time.sleep(5)   
    if(ret == 11):
        text_to_speech("Il nero ha vinto")
    else:
        text_to_speech("Il bianco ha vinto")

main()

