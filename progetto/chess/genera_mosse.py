from re import M
from posizioni_valide import *


diz_cod_png = {"a" : 0,"b" : 1,"c" : 2,"d" : 3,"e" : 4,"f" : 5,"g" : 6,"h" : 7}

num = ["1", "2", "3", "4", "5", "6", "7", "8"]

def check_fine_partita(i,j,board):
    if(board[i][j] == "bR"):
        return 11
    elif(board[i][j] == "nR"):
        return 10
    return 0

def modifica_board(board,mossa,colore):
    #check correttezza mossa
    if((len(mossa) != 2) and (len(mossa) != 3)):
        print("mossa errata!!!")
        return -1
    elif(len(mossa) == 2):
        if(not mossa[0].islower()):
            print("mossa errata!!!")
            return -1
        if(mossa[1] not in num):
            print("mossa errata!!!")
            return -1
    elif(len(mossa) == 3):
        if(not mossa[0].isupper()):
            print("mossa errata!!!")
            return -1
        if(not mossa[1].islower()):
            print("mossa errata!!!")
            return -1
        if(mossa[2] not in num):
            print("mossa errata!!!")
            return -1

    #mossa di un cavallo, alfiere, torre, regina o re
    if(len(mossa) == 3):
        j = diz_cod_png[mossa[1]]
        i = int(mossa[2]) -1
        pezzo = mossa[0]
        if(pezzo == "C"):                                                                           #mossa cavallo
            if(colore == "b"):
                pos_cav = posizioni_valide_cavalli(board)[0]
                x = i*8+j
                for key in pos_cav:
                    for elem in pos_cav[key]:
                        if (elem == x):
                            r = check_fine_partita(i,j,board)
                            board[key[0]][key[1]] = ""
                            board[i][j] = "bC"
                            if(r!=0):
                                return r
                            return 0
                return -1
            else:
                pos_cav = posizioni_valide_cavalli(board)[1]
                x = i*8+j
                for key in pos_cav:
                    for elem in pos_cav[key]:
                        if (elem == x):
                            r = check_fine_partita(i,j,board)
                            board[key[0]][key[1]] = ""
                            board[i][j] = "nC"
                            if(r!=0):
                                return r
                            return 0
                return -1
        elif(pezzo == "A"):                                                                         #mossa di un alfiere
            if(colore == "b"):
                pos_alf = posizioni_valide_alfieri(board)[0]
                x = i*8+j
                for key in pos_alf:
                    for elem in pos_alf[key]:
                        if (elem == x):
                            r = check_fine_partita(i,j,board)
                            board[key[0]][key[1]] = ""
                            board[i][j] = "bA"
                            if(r!=0):
                                return r
                            return 0
                return -1
            else:
                pos_alf = posizioni_valide_alfieri(board)[1]
                x = i*8+j
                for key in pos_alf:
                    for elem in pos_alf[key]:
                        if (elem == x):
                            r = check_fine_partita(i,j,board)
                            board[key[0]][key[1]] = ""
                            board[i][j] = "nA"
                            if(r!=0):
                                return r
                            return 0
                return -1
        elif(pezzo == "T"):                                                                         #mossa di una torre
            if(colore == "b"):
                pos_tow = posizioni_valide_torri(board)[0]
                x = i*8+j
                for key in pos_tow:
                    for elem in pos_tow[key]:
                        if (elem == x):
                            r = check_fine_partita(i,j,board)
                            board[key[0]][key[1]] = ""
                            board[i][j] = "bT"
                            if(r!=0):
                                return r
                            return 0
                return -1
            else:
                pos_tow = posizioni_valide_torri(board)[1]
                x = i*8+j
                for key in pos_tow:
                    for elem in pos_tow[key]:
                        if (elem == x):
                            r = check_fine_partita(i,j,board)
                            board[key[0]][key[1]] = ""
                            board[i][j] = "nT"
                            if(r!=0):
                                return r
                            return 0
                return -1
        elif(pezzo == "Q"):                                                                         #mossa di una regina
            if(colore == "b"):
                pos_queen = posizioni_valide_regina(board)[0]
                x = i*8+j
                for key in pos_queen:
                    for elem in pos_queen[key]:
                        if (elem == x):
                            r = check_fine_partita(i,j,board)
                            board[key[0]][key[1]] = ""
                            board[i][j] = "bQ"
                            if(r!=0):
                                return r
                            return 0
                return -1
            else:
                pos_queen = posizioni_valide_regina(board)[1]
                x = i*8+j
                for key in pos_queen:
                    for elem in pos_queen[key]:
                        if (elem == x):
                            r = check_fine_partita(i,j,board)
                            board[key[0]][key[1]] = ""
                            board[i][j] = "nQ"
                            if(r!=0):
                                return r
                            return 0
                return -1
        elif(pezzo == "R"):                                                                     #mossa di un re                                                                 
            if(colore == "b"):
                pos_re = posizioni_valide_re(board)[0]
                x = i*8+j
                for key in pos_re:
                    if(key[0] == 0 and key[1] == 4 and i==0 and j==6 and board[0][7] == "bT"):
                        board[0][4] = ""
                        board[0][7] = ""
                        board[0][5] = "bT"
                        board[0][6] = "bR"
                        return 0
                    if(key == (0,4) and i==0 and j==2 and board[0][0] == "bT"):
                        board[0][4] = ""
                        board[0][0] = ""
                        board[0][3] = "bT"
                        board[0][2] = "bR"
                        return 0
                    for elem in pos_re[key]:
                        if (elem == x):
                            board[key[0]][key[1]] = ""
                            board[i][j] = "bR"
                            return 0
                return -1
            else:
                pos_re = posizioni_valide_re(board)[1]
                x = i*8+j
                for key in pos_re:
                    if(key[0] == 7 and key[1] == 4 and i==7 and j==6 and board[7][7] == "nT"):
                        board[7][4] = ""
                        board[7][7] = ""
                        board[7][5] = "nT"
                        board[7][6] = "nR"
                        return 0
                    if(key[0] == 7 and key[1] == 4 and i==7 and j==2 and board[7][0] == "nT"):
                        board[7][4] = ""
                        board[7][0] = ""
                        board[7][3] = "nT"
                        board[7][2] = "nR"
                        return 0
                    for elem in pos_re[key]:
                        if (elem == x):
                            board[key[0]][key[1]] = ""
                            board[i][j] = "nR"
                            return 0
                return -1
    
    elif(len(mossa) == 2):                                                                          #mossa di un pedone
        j = diz_cod_png[mossa[0]]
        i = int(mossa[1]) -1
        if(i<0 or i>7 or j<0 or j>7):
            print("mossa errata!!!")
            return -1
        if(colore == "b"):
            pos_pedoni = posizioni_valide_pedoni(board)[0]
            x = i*8+j
            for key in pos_pedoni:
                for elem in pos_pedoni[key]:
                    if (elem == x):
                        board[key[0]][key[1]] = ""
                        if(i == 7):
                            r = check_fine_partita(i,j,board)
                            board[i][j] = "bQ"
                            if(r!=0):
                                return r
                        else:
                            r = check_fine_partita(i,j,board)
                            board[i][j] = "bP"
                            if(r!=0):
                                return r
                        return 0
            return -1
        else:
            pos_pedoni = posizioni_valide_pedoni(board)[1]
            x = i*8+j
            for key in pos_pedoni:
                for elem in pos_pedoni[key]:
                    if (elem == x):
                        board[key[0]][key[1]] = ""
                        if(i == 0):
                            r = check_fine_partita(i,j,board)
                            board[i][j] = "nQ"
                            if(r!=0):
                                return r
                        else:
                            r = check_fine_partita(i,j,board)
                            board[i][j] = "nP"
                            if(r!=0):
                                return r
                        return 0
            return -1
    

    
            
            