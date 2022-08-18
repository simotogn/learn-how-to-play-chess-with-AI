from operator import truediv
from genera_mosse import modifica_board
from posizioni_valide import *
from valuta import *

diz_cod_png = {0 : "a",1 : "b",2 : "c",3 : "d",4 : "e",5 : "f",6 : "g",7 : "h"}

def unisci_dizionari(diz_a, diz_b):
    if(diz_a == {}):
        return diz_b
    elif(diz_b == {}):
        return diz_a
    for key in diz_b:
        for elem in diz_b[key]:
            if(key not in diz_a):
                diz_a[key] = [elem]
            else:
                diz_a[key].append(elem)
    return diz_a

def copia_mat(mat1, mat2):
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            mat2[i][j] = mat1[i][j]

def calcola_tutte_mosse(board,colore):
    diz_b = posizioni_valide_pedoni(board)[0]
    diz_n = posizioni_valide_pedoni(board)[1]
    if(colore == "b"):
        pvt_b = posizioni_valide_torri(board)[0]
        pvc_b = posizioni_valide_cavalli(board)[0]
        pva_b = posizioni_valide_alfieri(board)[0]
        pvq_b = posizioni_valide_regina(board)[0]
        pvr_b = posizioni_valide_re(board)[0]
        diz_b = unisci_dizionari(diz_b,pvt_b)
        diz_b = unisci_dizionari(diz_b,pvc_b)
        diz_b = unisci_dizionari(diz_b,pva_b)
        diz_b = unisci_dizionari(diz_b,pvq_b)
        diz_b = unisci_dizionari(diz_b,pvr_b)  
        return diz_b  
    else:
        pvt_n = posizioni_valide_torri(board)[1]
        pvc_n = posizioni_valide_cavalli(board)[1]
        pva_n = posizioni_valide_alfieri(board)[1]
        pvq_n = posizioni_valide_regina(board)[1]
        pvr_n = posizioni_valide_re(board)[1]
        diz_n = unisci_dizionari(diz_n,pvt_n)
        diz_n = unisci_dizionari(diz_n,pvc_n)
        diz_n = unisci_dizionari(diz_n,pva_n)
        diz_n = unisci_dizionari(diz_n,pvq_n)
        diz_n = unisci_dizionari(diz_n,pvr_n)
        return diz_n
          

def converti_mossa(board,i,j,mossa):                   #passa da (0,1) : 14 a Ta6
    ret = ""
    if(board[i][j] != "" and board[i][j][1] == "P"):
        nuova_i = mossa//8
        nuova_j = mossa - nuova_i*8
        ret1 = diz_cod_png[nuova_j]
        ret2 = nuova_i + 1 
        ret = str(ret1) + str(ret2)
    elif(board[i][j] != "" and board[i][j][1] != "P"):
        nuova_i = mossa//8
        nuova_j = mossa - nuova_i*8
        ret1 = diz_cod_png[nuova_j]
        ret2 = nuova_i + 1 
        ret = board[i][j][1] + str(ret1) + str(ret2)
    return ret

def minimax_init_nero(board,d):
    return minimax("",board,d,False,-1000000,1000000)

def minimax_init_bianco(board,d):
    return minimax("",board,d,True,-1000000,1000000)                 
                                                                      #se gioca col bianco massimizza, altrimenti minimizza
def minimax(m,board,livello,massimizza,a,b):
    if(livello==0):
        ret = valuta(board)
        val = ret[0] - ret[1]                                          #punteggio bianco - punteggio nero
        return (val,m)
    if(massimizza):                                        
        max = -10000000
        mossa_migliore = ""
        mio_colore = "b"
        diz = calcola_tutte_mosse(board,mio_colore)
        for key in diz:
            for elem in diz[key]:
                board_copy = [["" for i in range(8)]for i in range(8)]
                copia_mat(board,board_copy)
                mossa = converti_mossa(board,key[0],key[1],elem)
                modifica_board(board_copy,mossa,mio_colore)
                v = minimax(mossa,board_copy,livello-1,False,a,b)[0]
                if(v > max):
                    max = v
                    mossa_migliore = mossa
                if(v>a):
                    a = v
                if(b<=a):
                    break
        return (max,mossa_migliore)  
    else:
        min = 10000000
        mossa_migliore = ""
        mio_colore = "n"
        diz = calcola_tutte_mosse(board,mio_colore)
        for key in diz:
            for elem in diz[key]:
                board_copy = [["" for i in range(8)]for i in range(8)]
                copia_mat(board,board_copy)
                mossa = converti_mossa(board,key[0],key[1],elem)
                modifica_board(board_copy,mossa,mio_colore)
                v = minimax(mossa,board_copy,livello-1,True,a,b)[0]                                                                               
                if(v < min):
                    min = v
                    mossa_migliore = mossa
                if(v<b):
                    b = v
                if(b<=a):
                    break
        return (min,mossa_migliore)

                







