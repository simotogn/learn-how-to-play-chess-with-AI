from random import randint
import time
from math import log,sqrt,e,inf
from genera_mosse_gardner import *

class node():
    def __init__(self):
        self.state = None
        self.action = ''
        self.children = set()
        self.parent = None
        self.N = 0                      #number of times parent node has been visited
        self.n = 0                      #number of times child node has been visited
        self.t = 0                      #winning score of current node

diz_cod_png = {0 : "a",1 : "b",2 : "c",3 : "d",4 : "e"}

def copia_mat(mat1, mat2):
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            mat2[i][j] = mat1[i][j]

def converti_mossa(board,i,j,mossa):                   #passa da (0,1) : 14 a Ta6
    ret = ""
    if(board[i][j] != "" and board[i][j][1] == "P"):
        nuova_i = mossa//5
        nuova_j = mossa - nuova_i*5
        ret1 = diz_cod_png[nuova_j]
        ret2 = nuova_i + 1 
        ret = str(ret1) + str(ret2)
    elif(board[i][j] != "" and board[i][j][1] != "P"):
        nuova_i = mossa//5
        nuova_j = mossa - nuova_i*5
        ret1 = diz_cod_png[nuova_j]
        ret2 = nuova_i + 1 
        ret = board[i][j][1] + str(ret1) + str(ret2)
    return ret

def ucb(curr_node):                                                                 #UPPER CONFIDENCE BOUND
    ans = curr_node.t+2*(sqrt(log(curr_node.N+e+(10**-6))/(curr_node.n+(10**-10))))
    return ans

def is_game_over(b):
    n=0
    for i in range(5):
        for j in range(5):
            if(b[i][j] == "bR"):
                n=1
    if(n==0):
        return -1                                   #ha vinto il nero
    for i in range(5):
        for j in range(5):
            if(b[i][j] == "nR"):
                n=-1
    if(n == 1):
        return 1                                    #ha vinto il bianco
    else:
        return 0                                    #non ha ancora vinto nessuno

def fai_mossa(key, elem, turno,board):
    board_copy = [["" for i in range(8)]for i in range(8)]
    copia_mat(board,board_copy)
    mossa = converti_mossa(board,key[0],key[1],elem)
    modifica_board(board_copy,mossa,turno)
    return board_copy

def mossa_random(board,colore):
    all_moves = calcola_tutte_mosse(board,colore)
    mosse = []
    for key in all_moves:
        for elem in all_moves[key]:
            mosse.append(converti_mossa(board, key[0],key[1],elem))
    n = len(mosse) -1
    r = randint(0,n)
    return mosse[r]

def rollout(board_att,t):
    if(t == "b"):
        st = "n"
    else:
        st = "b"

    while(not is_game_over(board_att)):
        mossa = mossa_random(board_att, t)
        modifica_board(board_att,mossa,t)
        if(not is_game_over(board_att)):
            mossa = mossa_random(board_att, st)
            modifica_board(board_att,mossa,st)
    return is_game_over(board_att)


def mcts_pred(turno,curr_node,board):
    all_moves = calcola_tutte_mosse(board,turno)
    for key in all_moves:
        for elem in all_moves[key]:
            tmp_state = fai_mossa(key,elem,turno,board)
            child = node()
            child.state = tmp_state
            child.parent = curr_node
            child.action = converti_mossa(board,key[0],key[1],elem)
            child.action = str(child.action)
            curr_node.children.add(child)

    n  = len(curr_node.children)
    while(n>0):
        max_ucb = -inf
        best_child = None
        for c in curr_node.children:
            if(ucb(c) > max_ucb and c.n == 0):
                max_ucb = ucb(c)
                best_child = c
        best_child.n = 1
        curr_node.n+=1
        best_child.N +=1
        if(turno == "b"):
            t = "n"
        else:
            t = "b"
        n-=1
        wn = 0
        wb = 0
        for i in range(100):
            b = [["" for i in range(8)]for i in range(8)]
            copia_mat(best_child.state,b)
            r = rollout(b,t)
            if(r == -1):
                wn+=1
            elif(r == 1):
                wb+=1
        if(turno == "b"):
            best_child.t = wb
        else:
            best_child.t = wn
        curr_node.t += best_child.t
    mossa_migliore = -inf
    m_m = ""
    for elem in curr_node.children:
        if(elem.t >= mossa_migliore):
            mossa_migliore = elem.t
            m_m = elem.action
    return m_m    

def mcts(turno,board):
    root = node()
    root.state = board
    result = mcts_pred(turno,root,board)
    return result

        