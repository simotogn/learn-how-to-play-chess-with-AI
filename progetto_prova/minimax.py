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

def minimax_init(board,mio_colore):
    minimax(board,mio_colore,4)

def minimax(board,mio_colore,livello):
    """ punteggio = -100000
    mossa_ret = "" """
    if(livello<0):
        return
    elif(livello>0):
        if(mio_colore == "b"):
            diz =calcola_tutte_mosse(board,mio_colore)
            for key in diz:
                for elem in diz[key]:
                    board_copy = [["" for i in range(8)]for i in range(8)]
                    copia_mat(board,board_copy)
                    mossa = converti_mossa(board,key[0],key[1],elem)
                    modifica_board(board_copy,mossa,mio_colore)
                    v = valuta(board_copy)
                    minimax(board_copy,mio_colore,livello-1)
                    """ res = v[0] - v[1]
                    if(res > punteggio):
                        mossa_ret = mossa
                        punteggio = res """
        else:
            diz =calcola_tutte_mosse(board,mio_colore)
            for key in diz:
                for elem in diz[key]:
                    board_copy = [["" for i in range(8)]for i in range(8)]
                    copia_mat(board,board_copy)
                    mossa = converti_mossa(board,key[0],key[1],elem)
                    modifica_board(board_copy,mossa,mio_colore)
                    v = valuta(board_copy)
                    minimax(board_copy,mio_colore,livello-1)
                    """ res = v[1] - v[0]
                    if(res > punteggio):
                        mossa_ret = mossa
                        punteggio = res """
    else:                                               #livello 0, ovvero l'ultimo a cui arriviamo
        

    """ print(mossa_ret,punteggio)
    return mossa_ret """
                







