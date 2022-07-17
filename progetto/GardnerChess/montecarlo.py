import random
import time
from math import log,sqrt,e,inf
from main import board
from genera_mosse import *

class node():
    def __init__(self):
        self.state = board
        self.action = ''
        self.children = set()
        self.parent = None
        self.N = 0                      #number of times parent node has been visited
        self.n = 0                      #number of times child node has been visited
        self.v = 0                      #winning score of current node

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

def ucb1(curr_node):
    ans = curr_node.v+2*(sqrt(log(curr_node.N+e+(10**-6))/(curr_node.n+(10**-10))))
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

def fai_mossa(key, elem, turno):
    board_copy = [["" for i in range(8)]for i in range(8)]
    copia_mat(board,board_copy)
    mossa = converti_mossa(board,key[0],key[1],elem)
    modifica_board(board_copy,mossa,turno)
    return board_copy

def rollout(curr_node,turno):
    
    if(is_game_over(curr_node.state) != 0):
        res = is_game_over(curr_node.state)
        if(res==1):
            #print("h1")
            return (1,curr_node)
        elif(res==-1):
            #print("h2")
            return (-1,curr_node)
        else:
            return (0.5,curr_node)
    if(turno == "b"):
        all_moves = calcola_tutte_mosse(board,turno)
    else:
        all_moves = calcola_tutte_mosse(board,turno)
    
    for key in all_moves:
        for elem in all_moves[key]:
            tmp_state = fai_mossa(key,elem,turno)
            child = node()
            child.state = tmp_state
            child.parent = curr_node
            curr_node.children.add(child)
    rnd_state = random.choice(list(curr_node.children))

    return rollout(rnd_state,turno)

def expand(curr_node,white):
    if(len(curr_node.children)==0):
        return curr_node
    max_ucb = -inf
    if(white):
        idx = -1
        max_ucb = -inf
        sel_child = None
        for i in curr_node.children:
            tmp = ucb1(i)
            if(tmp>max_ucb):
                idx = i
                max_ucb = tmp
                sel_child = i

        return(expand(sel_child,0))

    else:
        idx = -1
        min_ucb = inf
        sel_child = None
        for i in curr_node.children:
            tmp = ucb1(i)
            if(tmp<min_ucb):
                idx = i
                min_ucb = tmp
                sel_child = i

        return expand(sel_child,1)

def rollback(curr_node,reward):
    curr_node.n+=1
    curr_node.v+=reward
    while(curr_node.parent!=None):
        curr_node.N+=1
        curr_node = curr_node.parent
    return curr_node

def mcts_pred(turno,curr_node,over,iterations=2):
    if(over):
        return -1
    if(turno == "b"):
        all_moves = calcola_tutte_mosse(board,turno)
    else:
        all_moves = calcola_tutte_mosse(board,turno)
    map_state_move = dict()
    #print(all_moves)
    for key in all_moves:
        for elem in all_moves[key]:
            tmp_state = fai_mossa(key,elem,turno)
            child = node()
            child.state = tmp_state
            child.parent = curr_node
            child.parent = curr_node
            curr_node.children.add(child)
            #map_state_move[child] = i
        
    while(iterations>0):
        if(turno == "b"):
            idx = -1
            max_ucb = -inf
            sel_child = None
            for i in curr_node.children:
                tmp = ucb1(i)
                if(tmp>max_ucb):
                    idx = i
                    max_ucb = tmp
                    sel_child = i
            ex_child = expand(sel_child,0)
            reward,state = rollout(ex_child,turno)
            curr_node = rollback(state,reward)
            iterations-=1
        else:
            idx = -1
            min_ucb = inf
            sel_child = None
            for i in curr_node.children:
                tmp = ucb1(i)
                if(tmp<min_ucb):
                    idx = i
                    min_ucb = tmp
                    sel_child = i

            ex_child = expand(sel_child,1)

            reward,state = rollout(ex_child,turno)

            curr_node = rollback(state,reward)
            iterations-=1
    if(turno == "b"):
        
        mx = -inf
        idx = -1
        selected_move = ''
        for i in (curr_node.children):
            tmp = ucb1(i)
            if(tmp>mx):
                mx = tmp
                selected_move = map_state_move[i]
        return selected_move
    else:
        mn = inf
        idx = -1
        selected_move = ''
        for i in (curr_node.children):
            tmp = ucb1(i)
            if(tmp<mn):
                mn = tmp
                selected_move = map_state_move[i]
        return selected_move

""" board = chess.Board()
engine = chess.engine.SimpleEngine.popen_uci(r'C:/Users/Fabio/Desktop/stockfish_15_win_x64_avx2/stockfish_15_x64_avx2.exe')

white = 1
moves = 0
pgn = []
game = chess.pgn.Game()
evaluations = []
sm = 0
cnt = 0
while((not board.is_game_over())):
    all_moves = [board.san(i) for i in list(board.legal_moves)]
    #start = time.time()
    root = node()
    root.state = board
    result = mcts_pred("b",root,board.is_game_over())
    #sm+=(time.time()-start)
    board.push_san(result)
    #print(result)
    pgn.append(result)
    white ^= 1
    #cnt+=1
    
    moves+=1
    #board_evaluation = evaluate(board.fen().split()[0])
    #evaluations.append(board_evaluation)
#print("Average Time per move = ",sm/cnt)
print(board)
print(" ".join(pgn))
print()
#print(evaluations)
print(board.result())
game.headers["Result"] = board.result()
#print(game)
engine.quit() """

root = node()
root.state = board
result = mcts_pred("b",root,is_game_over(board))
print(result)