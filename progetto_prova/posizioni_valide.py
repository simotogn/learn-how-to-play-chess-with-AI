from re import I


def posizioni_valide_pedoni(mat):
    diz_b = {}
    diz_n = {}

    for i in range(8):
        for j in range(8):
            if ( mat[i][j] == "bP" ):                                           #pedoni bianchi
                diz_b[(i,j)] = []
                if (i+1 < 8 and mat[i+1][j] == ""):                             #controllo la casella alla riga sopra
                    diz_b[(i,j)].append((i+1)*8+j)
                if (i==1 and mat[i+2][j] == "" and mat[i+1][j] == ""):          #controllo la casella una e due righe sopra solo se il pedone non si è mai mosso
                    diz_b[(i,j)].append((i+2)*8+j)
                if (j==0):                                                      #controllo diagonali destre per pedoni sul bordo sx
                    if(i+1<8 and mat[i+1][j+1] != "" and mat[i+1][j+1][0] == "n"):
                        diz_b[(i,j)].append((i+1)*8+(j+1))
                if (j==7):                                                      #controllo diagonali sinistre per pedoni sul bordo dx
                    if(i+1<8 and mat[i+1][j-1] != "" and mat[i+1][j-1][0] == "n"):
                        diz_b[(i,j)].append((i+1)*8+(j-1))                                                    
                if (j>0 and j<7):                                               #controllo diagonali per pedoni centrali                                                      
                    if(i+1<8 and mat[i+1][j+1] != "" and mat[i+1][j+1][0] == "n"):
                        diz_b[(i,j)].append((i+1)*8+(j+1))
                    if(i+1<8 and mat[i+1][j-1] != "" and mat[i+1][j-1][0] == "n"):
                        diz_b[(i,j)].append((i+1)*8+(j-1)) 
            elif (mat[i][j] == "nP" ):                                          #pedoni neri
                diz_n[(i,j)] = []
                if (i-1 >=0 and mat[i-1][j] == ""):                             #controllo la casella alla riga sotto
                    diz_n[(i,j)].append((i-1)*8+j)
                if (i==6 and mat[i-2][j] == "" and mat[i-1][j] == ""):          #controllo la casella due righe sotto solo se il pedone non si è mai mosso
                    diz_n[(i,j)].append((i-2)*8+j)
                if (j==0):                                                      #controllo diagonali destre per pedoni sul bordo sx
                    if(i-1>=0 and mat[i-1][j+1] != "" and mat[i-1][j+1][0] == "b"):
                        diz_n[(i,j)].append((i-1)*8+(j+1))
                if (j==7):                                                      #controllo diagonali sinistre per pedoni sul bordo dx
                    if(i-1>=0 and mat[i-1][j-1] != "" and mat[i-1][j-1][0] == "b"):
                        diz_n[(i,j)].append((i-1)*8+(j-1))                                                    
                if (j>0 and j<7):                                               #controllo diagonali per pedoni centrali                                                      
                    if(i-1>=0 and mat[i-1][j+1] != "" and mat[i-1][j+1][0] == "b"):
                        diz_n[(i,j)].append((i-1)*8+(j+1))
                    if(i-1>=0 and mat[i-1][j-1] != "" and mat[i-1][j-1][0] == "b"):
                        diz_n[(i,j)].append((i-1)*8+(j-1)) 
    return (diz_b, diz_n)

def posizioni_valide_torri(mat):
    diz_b = {}
    diz_n = {}

    for i in range(8):
        for j in range(8):
            if(mat[i][j] == "bT"):
                diz_b[(i,j)] = []
                k = i+1
                while(k<8):                                                             #controllo riga superiore                                      
                    if(mat[k][j] == ""):
                        diz_b[(i,j)].append(k*8+j)
                        k+=1
                    elif(mat[k][j][0] == "n"):
                        diz_b[(i,j)].append(k*8+j)
                        break
                    elif(mat[k][j][0] == "b"):
                        break
                if (j!=7):                                                               #controllo riga laterale dx 
                    ld = j+1
                    while(ld!=7):                                                                                                  
                        if(mat[i][ld] == ""):
                            diz_b[(i,j)].append(i*8+ld)
                            ld+=1
                        elif(mat[i][ld][0] == "n"):
                            diz_b[(i,j)].append(i*8+ld)
                            break
                        elif(mat[i][ld][0] == "b"):
                            break
                    if(ld==7 and (mat[i][ld] == "" or mat[i][ld][0] == "n")):
                        diz_b[(i,j)].append(i*8+ld)
                if (j!=0):                                                                  #controllo riga laterale sx
                    ls = j-1
                    while(ls!=0):                                                                                                 
                        if(mat[i][ls] == ""):
                            diz_b[(i,j)].append(i*8+ls)
                            ls-=1
                        elif(mat[i][ls][0] == "n"):
                            diz_b[(i,j)].append(i*8+ls)
                            break
                        elif(mat[i][ls][0] == "b"):
                            break
                    if(ls==0 and (mat[i][ls] == "" or mat[i][ls][0] == "n")):
                        diz_b[(i,j)].append(i*8+ls)
                d = i-8
                while(d>=0):                                                                #controllo riga inferiore
                    if(mat[d][j] == ""):
                        diz_b[(i,j)].append(d*8+j)
                        d-=1
                    elif(mat[d][j][0] == "n"):
                        diz_b[(i,j)].append(d*8+j)
                        break
                    elif(mat[d][j][0] == "b"):
                        break            
            elif(mat[i][j] == "nT"):
                diz_n[(i,j)] = []
                k = i+1
                while(k<8):                                                             #controllo riga superiore                                      
                    if(mat[k][j] == ""):
                        diz_n[(i,j)].append(k*8+j)
                        k+=1
                    elif(mat[k][j][0] == "b"):
                        diz_n[(i,j)].append(k*8+j)
                        break
                    elif(mat[k][j][0] == "n"):
                        break
                if (j!=7):                                                               #controllo riga laterale dx 
                    ld = j+1
                    while(ld!=7):                                                                                                  
                        if(mat[i][ld] == ""):
                            diz_n[(i,j)].append(i*8+ld)
                            ld+=1
                        elif(mat[i][ld][0] == "b"):
                            diz_n[(i,j)].append(i*8+ld)
                            break
                        elif(mat[i][ld][0] == "n"):
                            break
                    if(ld==7 and (mat[i][ld] == "" or mat[i][ld][0] == "b")):
                        diz_n[(i,j)].append(i*8+ld)
                if (j!=0):                                                   #controllo riga laterale sx
                    ls = j-1
                    while(ls!=0):                                                                                                 
                        if(mat[i][ls] == ""):
                            diz_n[(i,j)].append(i*8+ls)
                            ls-=1
                        elif(mat[i][ls][0] == "b"):
                            diz_n[(i,j)].append(i*8+ls)
                            break
                        elif(mat[i][ls][0] == "n"):
                            break
                    if(ls==0 and (mat[i][ls] == "" or mat[i][ls][0] == "b")):
                        diz_n[(i,j)].append(i*8+ls)
                d = i-1
                while(d>=0):                                                                #controllo riga inferiore
                    if(mat[d][j] == ""):
                        diz_n[(i,j)].append(d*8+j)
                        d-=1
                    elif(mat[d][j][0] == "b"):
                        diz_n[(i,j)].append(d*8+j)
                        break
                    elif(mat[d][j][0] == "n"):
                        break 
          
    return (diz_b, diz_n)

def posizioni_valide_cavalli(mat):
    diz_b = {}
    diz_n = {}
    
    for i in range(8):
        for j in range(8):
            if(mat[i][j] == "bC" or mat[i][j] == "nC"):
                if(mat[i][j] == "bC"):
                    diz_b[(i,j)] = []
                else:
                    diz_n[(i,j)] = []
                colore = mat[i][j][0]
                if(i+1<8 and j+2<8 and (mat[i+1][j+2] == "" or mat[i+1][j+2][0] != colore)):
                    if(colore == "b"):
                        diz_b[(i,j)].append((i+1)*8+j+2)
                    else:
                        diz_n[(i,j)].append((i+1)*8+j+2)
                if(i-1>=0 and j+2<8 and (mat[i-1][j+2] == "" or mat[i-1][j+2][0] != colore)):
                    if(colore == "b"):
                        diz_b[(i,j)].append((i-1)*8+j+2)
                    else:
                        diz_n[(i,j)].append((i-1)*8+j+2)
                if(i+2<8 and j+1<8 and (mat[i+2][j+1] == "" or mat[i+2][j+1][0] != colore)):
                    if(colore == "b"):
                        diz_b[(i,j)].append((i+2)*8+j+1)
                    else:
                        diz_n[(i,j)].append((i+2)*8+j+1)
                if(i-2>=0 and j+1<8 and (mat[i-2][j+1] == "" or mat[i-2][j+1][0] != colore)):
                    if(colore == "b"):
                        diz_b[(i,j)].append((i-2)*8+j+1)
                    else:
                        diz_n[(i,j)].append((i-2)*8+j+1)
                if(i+2<8 and j-1>=0 and (mat[i+2][j-1] == "" or mat[i+2][j-1][0] != colore)):
                    if(colore == "b"):
                        diz_b[(i,j)].append((i+2)*8+j-1)
                    else:
                        diz_n[(i,j)].append((i+2)*8+j-1)
                if(i-2>=0 and j-1>=0 and (mat[i-2][j-1] == "" or mat[i-2][j-1][0] != colore)):
                    if(colore == "b"):
                        diz_b[(i,j)].append((i-2)*8+j-1)
                    else:
                        diz_n[(i,j)].append((i-2)*8+j-1)
                if(i+1<8 and j-2>=0 and (mat[i+1][j-2] == "" or mat[i+1][j-2][0] != colore)):
                    if(colore == "b"):
                        diz_b[(i,j)].append((i+1)*8+j-2)
                    else:
                        diz_n[(i,j)].append((i+1)*8+j-2)
                if(i-1>=0 and j-2>=0 and (mat[i-1][j-2] == "" or mat[i-1][j-2][0] != colore)):
                    if(colore == "b"):
                        diz_b[(i,j)].append((i-1)*8+j-2)
                    else:
                        diz_n[(i,j)].append((i-1)*8+j-2)
    return (diz_b, diz_n)
            
def posizioni_valide_alfieri(mat):
    diz_b = {}
    diz_n = {}

    for i in range(8):
        for j in range(8):
            if(mat[i][j] == "nA" or mat[i][j] == "bA"):
                if(mat[i][j] == "bA"):
                    diz_b[(i,j)] = []
                else:
                    diz_n[(i,j)] = []
                colore = mat[i][j][0]
                #diag sup dx
                k=i
                w=j
                while(k+1<8 and w+1<8):
                    k+=1
                    w+=1
                    if(mat[k][w] == ""):
                        if(colore == "b"):
                            diz_b[(i,j)].append(k*8+w)
                        else:
                            diz_n[(i,j)].append(k*8+w)
                    elif(mat[k][w][0] != colore):
                        if(colore == "b"):
                            diz_b[(i,j)].append(k*8+w)
                        else:
                            diz_n[(i,j)].append(k*8+w)
                        break
                    else:
                        break
                #diag sup sx
                k=i
                w=j
                while(k+1<8 and w-1>=0):
                    k+=1
                    w-=1
                    if(mat[k][w] == ""):
                        if(colore == "b"):
                            diz_b[(i,j)].append(k*8+w)
                        else:
                            diz_n[(i,j)].append(k*8+w)
                    elif(mat[k][w][0] != colore):
                        if(colore == "b"):
                            diz_b[(i,j)].append(k*8+w)
                        else:
                            diz_n[(i,j)].append(k*8+w)
                        break
                    else:
                        break
                #diag inf dx
                k=i
                w=j
                while(k-1>=0 and w+1<8):
                    k-=1
                    w+=1
                    if(mat[k][w] == ""):
                        if(colore == "b"):
                            diz_b[(i,j)].append(k*8+w)
                        else:
                            diz_n[(i,j)].append(k*8+w)
                    elif(mat[k][w][0] != colore):
                        if(colore == "b"):
                            diz_b[(i,j)].append(k*8+w)
                        else:
                            diz_n[(i,j)].append(k*8+w)
                        break
                    else:
                        break
                #diag inf sx
                k=i
                w=j
                while(k-1>=0 and w-1>=0):
                    k-=1
                    w-=1
                    if(mat[k][w] == ""):
                        if(colore == "b"):
                            diz_b[(i,j)].append(k*8+w)
                        else:
                            diz_n[(i,j)].append(k*8+w)
                    elif(mat[k][w][0] != colore):
                        if(colore == "b"):
                            diz_b[(i,j)].append(k*8+w)
                        else:
                            diz_n[(i,j)].append(k*8+w)
                        break
                    else:
                        break
    return (diz_b,diz_n)

def posizioni_valide_re(mat):
    diz_b = {}
    diz_n = {}

    for i in range(8):
        for j in range(8):
            if(mat[i][j] == "bR" or mat[i][j] == "nR"):
                if(mat[i][j] == "bR"):
                    diz_b[(i,j)] = []
                else:
                    diz_n[(i,j)] = []
                colore = mat[i][j][0]
                if(j+1<8 and (mat[i][j+1] == "" or mat[i][j+1][0] != colore)):
                    if(colore == "b"):
                        diz_b[(i,j)].append((i*8+j+1))
                    else:
                        diz_n[(i,j)].append((i*8+j+1))
                if(j-1>=0 and (mat[i][j-1] == "" or mat[i][j-1][0] != colore)):
                    if(colore == "b"):
                        diz_b[(i,j)].append((i*8+j-1))
                    else:
                        diz_n[(i,j)].append((i*8+j-1))
                if(i+1<8 and (mat[i+1][j] == "" or mat[i+1][j][0] != colore)):
                    if(colore == "b"):
                        diz_b[(i,j)].append((i+1)*8+j)
                    else:
                        diz_n[(i,j)].append((i+1)*8+j)
                if(i-1>=0 and (mat[i-1][j] == "" or mat[i-1][j][0] != colore)):
                    if(colore == "b"):
                        diz_b[(i,j)].append((i-1)*8+j)
                    else:
                        diz_n[(i,j)].append((i-1)*8+j)
                if(i+1<8 and j+1<8 and (mat[i+1][j+1] == "" or mat[i+1][j+1][0] != colore)):
                    if(colore == "b"):
                        diz_b[(i,j)].append((i+1)*8+j+1)
                    else:
                        diz_n[(i,j)].append((i+1)*8+j+1)
                if(i-1>=0 and j+1<8 and (mat[i-1][j+1] == "" or mat[i-1][j+1][0] != colore)):
                    if(colore == "b"):
                        diz_b[(i,j)].append((i-1)*8+j+1)
                    else:
                        diz_n[(i,j)].append((i-1)*8+j+1)
                if(i-1>=0 and j-1>=0 and (mat[i-1][j-1] == "" or mat[i-1][j-1][0] != colore)):
                    if(colore == "b"):
                        diz_b[(i,j)].append((i-1)*8+j-1)
                    else:
                        diz_n[(i,j)].append((i-1)*8+j-1)
                if(i+1<8 and j-1>=0 and (mat[i+1][j-1] == "" or mat[i+1][j-1][0] != colore)):
                    if(colore == "b"):
                        diz_b[(i,j)].append((i+1)*8+j-1)
                    else:
                        diz_n[(i,j)].append((i+1)*8+j-1)                   
    return (diz_b,diz_n)

def posizioni_valide_regina(mat):
    diz_b = {}
    diz_n = {}
    
    for i in range(8):
        for j in range(8):
            if(mat[i][j] == "nQ" or mat[i][j] == "bQ"):
                if(mat[i][j] == "bQ"):
                    diz_b[(i,j)] = []
                else:
                    diz_n[(i,j)] = []
                colore = mat[i][j][0]
                #diag sup dx
                k=i
                w=j
                while(k+1<8 and w+1<8):
                    k+=1
                    w+=1
                    if(mat[k][w] == ""):
                        if(colore == "b"):
                            diz_b[(i,j)].append(k*8+w)
                        else:
                            diz_n[(i,j)].append(k*8+w)
                    elif(mat[k][w][0] != colore):
                        if(colore == "b"):
                            diz_b[(i,j)].append(k*8+w)
                        else:
                            diz_n[(i,j)].append(k*8+w)
                        break
                    else:
                        break
                #diag sup sx
                k=i
                w=j
                while(k+1<8 and w-1>=0):
                    k+=1
                    w-=1
                    if(mat[k][w] == ""):
                        if(colore == "b"):
                            diz_b[(i,j)].append(k*8+w)
                        else:
                            diz_n[(i,j)].append(k*8+w)
                    elif(mat[k][w][0] != colore):
                        if(colore == "b"):
                            diz_b[(i,j)].append(k*8+w)
                        else:
                            diz_n[(i,j)].append(k*8+w)
                        break
                    else:
                        break
                #diag inf dx
                k=i
                w=j
                while(k-1>=0 and w+1<8):
                    k-=1
                    w+=1
                    if(mat[k][w] == ""):
                        if(colore == "b"):
                            diz_b[(i,j)].append(k*8+w)
                        else:
                            diz_n[(i,j)].append(k*8+w)
                    elif(mat[k][w][0] != colore):
                        if(colore == "b"):
                            diz_b[(i,j)].append(k*8+w)
                        else:
                            diz_n[(i,j)].append(k*8+w)
                        break
                    else:
                        break
                #diag inf sx
                k=i
                w=j
                while(k-1>=0 and w-1>=0):
                    k-=1
                    w-=1
                    if(mat[k][w] == ""):
                        if(colore == "b"):
                            diz_b[(i,j)].append(k*8+w)
                        else:
                            diz_n[(i,j)].append(k*8+w)
                    elif(mat[k][w][0] != colore):
                        if(colore == "b"):
                            diz_b[(i,j)].append(k*8+w)
                        else:
                            diz_n[(i,j)].append(k*8+w)
                        break
                    else:
                        break
                #riga sup
                k=i
                w=j
                while(k+1<8):
                    k+=1
                    if(mat[k][w] == ""):
                        if(colore == "b"):
                            diz_b[(i,j)].append(k*8+w)
                        else:
                            diz_n[(i,j)].append(k*8+w)
                    elif(mat[k][w][0] != colore):
                        if(colore == "b"):
                            diz_b[(i,j)].append(k*8+w)
                        else:
                            diz_n[(i,j)].append(k*8+w)
                        break
                    else:
                        break
                #riga inf
                k=i
                w=j
                while(k-1>=0):
                    k-=1
                    if(mat[k][w] == ""):
                        if(colore == "b"):
                            diz_b[(i,j)].append(k*8+w)
                        else:
                            diz_n[(i,j)].append(k*8+w)
                    elif(mat[k][w][0] != colore):
                        if(colore == "b"):
                            diz_b[(i,j)].append(k*8+w)
                        else:
                            diz_n[(i,j)].append(k*8+w)
                        break
                    else:
                        break
                #riga lat dx
                k=i
                w=j
                while(w+1<8):
                    w+=1
                    if(mat[k][w] == ""):
                        if(colore == "b"):
                            diz_b[(i,j)].append(k*8+w)
                        else:
                            diz_n[(i,j)].append(k*8+w)
                    elif(mat[k][w][0] != colore):
                        if(colore == "b"):
                            diz_b[(i,j)].append(k*8+w)
                        else:
                            diz_n[(i,j)].append(k*8+w)
                        break
                    else:
                        break
                #riga lat sx
                k=i
                w=j
                while(w-1>=0):
                    w-=1
                    if(mat[k][w] == ""):
                        if(colore == "b"):
                            diz_b[(i,j)].append(k*8+w)
                        else:
                            diz_n[(i,j)].append(k*8+w)
                    elif(mat[k][w][0] != colore):
                        if(colore == "b"):
                            diz_b[(i,j)].append(k*8+w)
                        else:
                            diz_n[(i,j)].append(k*8+w)
                        break
                    else:
                        break

    return (diz_b,diz_n)

def tot_posizioni_valide(board):           
    pos_val_b = 0
    pos_val_n = 0
    
    p_v_p_b = posizioni_valide_pedoni(board)[0]
    for key in p_v_p_b:
        for elem in p_v_p_b[key]:
            pos_val_b+=1
    p_v_p_n = posizioni_valide_pedoni(board)[1]
    for key in p_v_p_n:
        for elem in p_v_p_n[key]:
            pos_val_n+=1

    p_v_p_b = posizioni_valide_alfieri(board)[0]
    for key in p_v_p_b:
        for elem in p_v_p_b[key]:
            pos_val_b+=1
    p_v_p_n = posizioni_valide_alfieri(board)[1]
    for key in p_v_p_n:
        for elem in p_v_p_n[key]:
            pos_val_n+=1

    p_v_p_b = posizioni_valide_cavalli(board)[0]
    for key in p_v_p_b:
        for elem in p_v_p_b[key]:
            pos_val_b+=1
    p_v_p_n = posizioni_valide_cavalli(board)[1]
    for key in p_v_p_n:
        for elem in p_v_p_n[key]:
            pos_val_n+=1

    p_v_p_b = posizioni_valide_regina(board)[0]
    for key in p_v_p_b:
        for elem in p_v_p_b[key]:
            pos_val_b+=1
    p_v_p_n = posizioni_valide_regina(board)[1]
    for key in p_v_p_n:
        for elem in p_v_p_n[key]:
            pos_val_n+=1

    p_v_p_b = posizioni_valide_re(board)[0]
    for key in p_v_p_b:
        for elem in p_v_p_b[key]:
            pos_val_b+=1
    p_v_p_n = posizioni_valide_re(board)[1]
    for key in p_v_p_n:
        for elem in p_v_p_n[key]:
            pos_val_n+=1

    p_v_p_b = posizioni_valide_torri(board)[0]
    for key in p_v_p_b:
        for elem in p_v_p_b[key]:
            pos_val_b+=1
    p_v_p_n = posizioni_valide_torri(board)[1]
    for key in p_v_p_n:
        for elem in p_v_p_n[key]:
            pos_val_n+=1

    return (pos_val_b,pos_val_n) 
