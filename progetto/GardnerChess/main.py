from posizioni_valide import *
from genera_mosse import *



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
    t=0
    scacco_matto = False

    while(not scacco_matto):
        print("Turno: ",end=" ")
        print(t)
        t+=1

        
        break

        """ ret = -1
        while(ret == -1 and not scacco_matto):
            mossa_bianco = input('Digitare la propria mossa (bianco):  ')
            print("mossa_bianco: ",end=" ")
            print(mossa_bianco)
            ret = modifica_board(board,mossa_bianco,"b")
            stampa_board(board)
            if(ret == 10):
                scacco_matto = True
                print("Il bianco ha vinto!!!") 

        ret = -1
        while(ret == -1 and not scacco_matto):
            mossa_nero = input('Digitare la propria mossa (nero):  ')
            print("mossa_nero: ",end=" ")
            print(mossa_nero)
            ret = modifica_board(board,mossa_nero,"n")
            stampa_board(board)
            if(ret == 11):
                scacco_matto = True
                print("Il nero ha vinto!!!") """

#main()

print(calcola_tutte_mosse(board,"b"))