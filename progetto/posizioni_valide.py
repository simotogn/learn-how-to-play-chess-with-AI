from re import I



def posizioni_valide_pedoni(mat,l):
    diz_b = {}
    diz_n = {}

    for i in range(l):
        for j in range(l):
            if ( mat[i][j] == "bP" ):                                           #pedoni bianchi
                diz_b[(i,j)] = []
                if (i+1 < l and mat[i+1][j] == ""):                             #controllo la casella alla riga sopra
                    diz_b[(i,j)].append((i+1)*l+j)
                if (i==1 and mat[i+2][j] == "" and mat[i+1][j] == ""):          #controllo la casella una e due righe sopra solo se il pedone non si è mai mosso
                    diz_b[(i,j)].append((i+2)*l+j)
                if (j==0):                                                      #controllo diagonali destre per pedoni sul bordo sx
                    if(i+1<l and mat[i+1][j+1] != "" and mat[i+1][j+1][0] == "n"):
                        diz_b[(i,j)].append((i+1)*l+(j+1))
                if (j==(l-1)):                                                      #controllo diagonali sinistre per pedoni sul bordo dx
                    if(i+1<l and mat[i+1][j-1] != "" and mat[i+1][j-1][0] == "n"):
                        diz_b[(i,j)].append((i+1)*l+(j-1))                                                    
                if (j>0 and j<l-1):                                               #controllo diagonali per pedoni centrali                                                      
                    if(i+1<l and mat[i+1][j+1] != "" and mat[i+1][j+1][0] == "n"):
                        diz_b[(i,j)].append((i+1)*l+(j+1))
                    if(i+1<l and mat[i+1][j-1] != "" and mat[i+1][j-1][0] == "n"):
                        diz_b[(i,j)].append((i+1)*l+(j-1)) 
            elif (mat[i][j] == "nP" ):                                          #pedoni neri
                diz_n[(i,j)] = []
                if (i-1 >=0 and mat[i-1][j] == ""):                             #controllo la casella alla riga sotto
                    diz_n[(i,j)].append((i-1)*l+j)
                if (i==(l-1) and mat[i-2][j] == "" and mat[i-1][j] == ""):          #controllo la casella due righe sotto solo se il pedone non si è mai mosso
                    diz_n[(i,j)].append((i-2)*l+j)
                if (j==0):                                                      #controllo diagonali destre per pedoni sul bordo sx
                    if(i-1>=0 and mat[i-1][j+1] != "" and mat[i-1][j+1][0] == "b"):
                        diz_n[(i,j)].append((i-1)*l+(j+1))
                if (j==(l-1)):                                                      #controllo diagonali sinistre per pedoni sul bordo dx
                    if(i-1>=0 and mat[i-1][j-1] != "" and mat[i-1][j-1][0] == "b"):
                        diz_n[(i,j)].append((i-1)*l+(j-1))                                                    
                if (j>0 and j<(l-1)):                                               #controllo diagonali per pedoni centrali                                                      
                    if(i-1>=0 and mat[i-1][j+1] != "" and mat[i-1][j+1][0] == "b"):
                        diz_n[(i,j)].append((i-1)*l+(j+1))
                    if(i-1>=0 and mat[i-1][j-1] != "" and mat[i-1][j-1][0] == "b"):
                        diz_n[(i,j)].append((i-1)*l+(j-1)) 
    return (diz_b, diz_n)

def posizioni_valide_torri(mat,l):
    diz_b = {}
    diz_n = {}

    for i in range(l):
        for j in range(l):
            if(mat[i][j] == "bT"):
                diz_b[(i,j)] = []
                k = i+1
                while(k<l):                                                             #controllo riga superiore                                      
                    if(mat[k][j] == ""):
                        diz_b[(i,j)].append(k*l+j)
                        k+=1
                    elif(mat[k][j][0] == "n"):
                        diz_b[(i,j)].append(k*l+j)
                        break
                    elif(mat[k][j][0] == "b"):
                        break
                if (j!=(l-1)):                                                               #controllo riga laterale dx 
                    ld = j+1
                    while(ld!=(l-1)):                                                                                                  
                        if(mat[i][ld] == ""):
                            diz_b[(i,j)].append(i*l+ld)
                            ld+=1
                        elif(mat[i][ld][0] == "n"):
                            diz_b[(i,j)].append(i*l+ld)
                            break
                        elif(mat[i][ld][0] == "b"):
                            break
                    if(ld==(l-1) and (mat[i][ld] == "" or mat[i][ld][0] == "n")):
                        diz_b[(i,j)].append(i*l+ld)
                if (j!=0):                                                                  #controllo riga laterale sx
                    ls = j-1
                    while(ls!=0):                                                                                                 
                        if(mat[i][ls] == ""):
                            diz_b[(i,j)].append(i*l+ls)
                            ls-=1
                        elif(mat[i][ls][0] == "n"):
                            diz_b[(i,j)].append(i*l+ls)
                            break
                        elif(mat[i][ls][0] == "b"):
                            break
                    if(ls==0 and (mat[i][ls] == "" or mat[i][ls][0] == "n")):
                        diz_b[(i,j)].append(i*l+ls)
                d = i-5
                while(d>=0):                                                                #controllo riga inferiore
                    if(mat[d][j] == ""):
                        diz_b[(i,j)].append(d*l+j)
                        d-=1
                    elif(mat[d][j][0] == "n"):
                        diz_b[(i,j)].append(d*l+j)
                        break
                    elif(mat[d][j][0] == "b"):
                        break            
            elif(mat[i][j] == "nT"):
                diz_n[(i,j)] = []
                k = i+1
                while(k<l):                                                             #controllo riga superiore                                      
                    if(mat[k][j] == ""):
                        diz_n[(i,j)].append(k*l+j)
                        k+=1
                    elif(mat[k][j][0] == "b"):
                        diz_n[(i,j)].append(k*l+j)
                        break
                    elif(mat[k][j][0] == "n"):
                        break
                if (j!=(l-1)):                                                               #controllo riga laterale dx 
                    ld = j+1
                    while(ld!=(l-1)):                                                                                                  
                        if(mat[i][ld] == ""):
                            diz_n[(i,j)].append(i*l+ld)
                            ld+=1
                        elif(mat[i][ld][0] == "b"):
                            diz_n[(i,j)].append(i*l+ld)
                            break
                        elif(mat[i][ld][0] == "n"):
                            break
                    if(ld==(l-1) and (mat[i][ld] == "" or mat[i][ld][0] == "b")):
                        diz_n[(i,j)].append(i*l+ld)
                if (j!=0):                                                   #controllo riga laterale sx
                    ls = j-1
                    while(ls!=0):                                                                                                 
                        if(mat[i][ls] == ""):
                            diz_n[(i,j)].append(i*l+ls)
                            ls-=1
                        elif(mat[i][ls][0] == "b"):
                            diz_n[(i,j)].append(i*l+ls)
                            break
                        elif(mat[i][ls][0] == "n"):
                            break
                    if(ls==0 and (mat[i][ls] == "" or mat[i][ls][0] == "b")):
                        diz_n[(i,j)].append(i*l+ls)
                d = i-1
                while(d>=0):                                                                #controllo riga inferiore
                    if(mat[d][j] == ""):
                        diz_n[(i,j)].append(d*l+j)
                        d-=1
                    elif(mat[d][j][0] == "b"):
                        diz_n[(i,j)].append(d*l+j)
                        break
                    elif(mat[d][j][0] == "n"):
                        break 
          
    return (diz_b, diz_n)

def posizioni_valide_cavalli(mat,l):
    diz_b = {}
    diz_n = {}
    
    for i in range(l):
        for j in range(l):
            if(mat[i][j] == "bC" or mat[i][j] == "nC"):
                if(mat[i][j] == "bC"):
                    diz_b[(i,j)] = []
                else:
                    diz_n[(i,j)] = []
                colore = mat[i][j][0]
                if(i+1<l and j+2<l and (mat[i+1][j+2] == "" or mat[i+1][j+2][0] != colore)):
                    if(colore == "b"):
                        diz_b[(i,j)].append((i+1)*l+j+2)
                    else:
                        diz_n[(i,j)].append((i+1)*l+j+2)
                if(i-1>=0 and j+2<l and (mat[i-1][j+2] == "" or mat[i-1][j+2][0] != colore)):
                    if(colore == "b"):
                        diz_b[(i,j)].append((i-1)*l+j+2)
                    else:
                        diz_n[(i,j)].append((i-1)*l+j+2)
                if(i+2<l and j+1<l and (mat[i+2][j+1] == "" or mat[i+2][j+1][0] != colore)):
                    if(colore == "b"):
                        diz_b[(i,j)].append((i+2)*l+j+1)
                    else:
                        diz_n[(i,j)].append((i+2)*l+j+1)
                if(i-2>=0 and j+1<l and (mat[i-2][j+1] == "" or mat[i-2][j+1][0] != colore)):
                    if(colore == "b"):
                        diz_b[(i,j)].append((i-2)*l+j+1)
                    else:
                        diz_n[(i,j)].append((i-2)*l+j+1)
                if(i+2<l and j-1>=0 and (mat[i+2][j-1] == "" or mat[i+2][j-1][0] != colore)):
                    if(colore == "b"):
                        diz_b[(i,j)].append((i+2)*l+j-1)
                    else:
                        diz_n[(i,j)].append((i+2)*l+j-1)
                if(i-2>=0 and j-1>=0 and (mat[i-2][j-1] == "" or mat[i-2][j-1][0] != colore)):
                    if(colore == "b"):
                        diz_b[(i,j)].append((i-2)*l+j-1)
                    else:
                        diz_n[(i,j)].append((i-2)*l+j-1)
                if(i+1<l and j-2>=0 and (mat[i+1][j-2] == "" or mat[i+1][j-2][0] != colore)):
                    if(colore == "b"):
                        diz_b[(i,j)].append((i+1)*l+j-2)
                    else:
                        diz_n[(i,j)].append((i+1)*l+j-2)
                if(i-1>=0 and j-2>=0 and (mat[i-1][j-2] == "" or mat[i-1][j-2][0] != colore)):
                    if(colore == "b"):
                        diz_b[(i,j)].append((i-1)*l+j-2)
                    else:
                        diz_n[(i,j)].append((i-1)*l+j-2)
    return (diz_b, diz_n)
            
def posizioni_valide_alfieri(mat,l):
    diz_b = {}
    diz_n = {}

    for i in range(l):
        for j in range(l):
            if(mat[i][j] == "nA" or mat[i][j] == "bA"):
                if(mat[i][j] == "bA"):
                    diz_b[(i,j)] = []
                else:
                    diz_n[(i,j)] = []
                colore = mat[i][j][0]
                #diag sup dx
                k=i
                w=j
                while(k+1<l and w+1<l):
                    k+=1
                    w+=1
                    if(mat[k][w] == ""):
                        if(colore == "b"):
                            diz_b[(i,j)].append(k*l+w)
                        else:
                            diz_n[(i,j)].append(k*l+w)
                    elif(mat[k][w][0] != colore):
                        if(colore == "b"):
                            diz_b[(i,j)].append(k*l+w)
                        else:
                            diz_n[(i,j)].append(k*l+w)
                        break
                    else:
                        break
                #diag sup sx
                k=i
                w=j
                while(k+1<l and w-1>=0):
                    k+=1
                    w-=1
                    if(mat[k][w] == ""):
                        if(colore == "b"):
                            diz_b[(i,j)].append(k*l+w)
                        else:
                            diz_n[(i,j)].append(k*l+w)
                    elif(mat[k][w][0] != colore):
                        if(colore == "b"):
                            diz_b[(i,j)].append(k*l+w)
                        else:
                            diz_n[(i,j)].append(k*l+w)
                        break
                    else:
                        break
                #diag inf dx
                k=i
                w=j
                while(k-1>=0 and w+1<l):
                    k-=1
                    w+=1
                    if(mat[k][w] == ""):
                        if(colore == "b"):
                            diz_b[(i,j)].append(k*l+w)
                        else:
                            diz_n[(i,j)].append(k*l+w)
                    elif(mat[k][w][0] != colore):
                        if(colore == "b"):
                            diz_b[(i,j)].append(k*l+w)
                        else:
                            diz_n[(i,j)].append(k*l+w)
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
                            diz_b[(i,j)].append(k*l+w)
                        else:
                            diz_n[(i,j)].append(k*l+w)
                    elif(mat[k][w][0] != colore):
                        if(colore == "b"):
                            diz_b[(i,j)].append(k*l+w)
                        else:
                            diz_n[(i,j)].append(k*l+w)
                        break
                    else:
                        break
    return (diz_b,diz_n)

def posizioni_valide_re(mat,l):
    diz_b = {}
    diz_n = {}

    for i in range(l):
        for j in range(l):
            if(mat[i][j] == "bR" or mat[i][j] == "nR"):
                if(mat[i][j] == "bR"):
                    diz_b[(i,j)] = []
                else:
                    diz_n[(i,j)] = []
                colore = mat[i][j][0]
                if(j+1<l and (mat[i][j+1] == "" or mat[i][j+1][0] != colore)):
                    if(colore == "b"):
                        diz_b[(i,j)].append((i*l+j+1))
                    else:
                        diz_n[(i,j)].append((i*l+j+1))
                if(j-1>=0 and (mat[i][j-1] == "" or mat[i][j-1][0] != colore)):
                    if(colore == "b"):
                        diz_b[(i,j)].append((i*l+j-1))
                    else:
                        diz_n[(i,j)].append((i*l+j-1))
                if(i+1<l and (mat[i+1][j] == "" or mat[i+1][j][0] != colore)):
                    if(colore == "b"):
                        diz_b[(i,j)].append((i+1)*l+j)
                    else:
                        diz_n[(i,j)].append((i+1)*l+j)
                if(i-1>=0 and (mat[i-1][j] == "" or mat[i-1][j][0] != colore)):
                    if(colore == "b"):
                        diz_b[(i,j)].append((i-1)*l+j)
                    else:
                        diz_n[(i,j)].append((i-1)*l+j)
                if(i+1<l and j+1<l and (mat[i+1][j+1] == "" or mat[i+1][j+1][0] != colore)):
                    if(colore == "b"):
                        diz_b[(i,j)].append((i+1)*l+j+1)
                    else:
                        diz_n[(i,j)].append((i+1)*l+j+1)
                if(i-1>=0 and j+1<l and (mat[i-1][j+1] == "" or mat[i-1][j+1][0] != colore)):
                    if(colore == "b"):
                        diz_b[(i,j)].append((i-1)*l+j+1)
                    else:
                        diz_n[(i,j)].append((i-1)*l+j+1)
                if(i-1>=0 and j-1>=0 and (mat[i-1][j-1] == "" or mat[i-1][j-1][0] != colore)):
                    if(colore == "b"):
                        diz_b[(i,j)].append((i-1)*l+j-1)
                    else:
                        diz_n[(i,j)].append((i-1)*l+j-1)
                if(i+1<l and j-1>=0 and (mat[i+1][j-1] == "" or mat[i+1][j-1][0] != colore)):
                    if(colore == "b"):
                        diz_b[(i,j)].append((i+1)*l+j-1)
                    else:
                        diz_n[(i,j)].append((i+1)*l+j-1)                   
    return (diz_b,diz_n)

def posizioni_valide_regina(mat,l):
    diz_b = {}
    diz_n = {}
    
    for i in range(l):
        for j in range(l):
            if(mat[i][j] == "nQ" or mat[i][j] == "bQ"):
                if(mat[i][j] == "bQ"):
                    diz_b[(i,j)] = []
                else:
                    diz_n[(i,j)] = []
                colore = mat[i][j][0]
                #diag sup dx
                k=i
                w=j
                while(k+1<l and w+1<l):
                    k+=1
                    w+=1
                    if(mat[k][w] == ""):
                        if(colore == "b"):
                            diz_b[(i,j)].append(k*l+w)
                        else:
                            diz_n[(i,j)].append(k*l+w)
                    elif(mat[k][w][0] != colore):
                        if(colore == "b"):
                            diz_b[(i,j)].append(k*l+w)
                        else:
                            diz_n[(i,j)].append(k*l+w)
                        break
                    else:
                        break
                #diag sup sx
                k=i
                w=j
                while(k+1<l and w-1>=0):
                    k+=1
                    w-=1
                    if(mat[k][w] == ""):
                        if(colore == "b"):
                            diz_b[(i,j)].append(k*l+w)
                        else:
                            diz_n[(i,j)].append(k*l+w)
                    elif(mat[k][w][0] != colore):
                        if(colore == "b"):
                            diz_b[(i,j)].append(k*l+w)
                        else:
                            diz_n[(i,j)].append(k*l+w)
                        break
                    else:
                        break
                #diag inf dx
                k=i
                w=j
                while(k-1>=0 and w+1<l):
                    k-=1
                    w+=1
                    if(mat[k][w] == ""):
                        if(colore == "b"):
                            diz_b[(i,j)].append(k*l+w)
                        else:
                            diz_n[(i,j)].append(k*l+w)
                    elif(mat[k][w][0] != colore):
                        if(colore == "b"):
                            diz_b[(i,j)].append(k*l+w)
                        else:
                            diz_n[(i,j)].append(k*l+w)
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
                            diz_b[(i,j)].append(k*l+w)
                        else:
                            diz_n[(i,j)].append(k*l+w)
                    elif(mat[k][w][0] != colore):
                        if(colore == "b"):
                            diz_b[(i,j)].append(k*l+w)
                        else:
                            diz_n[(i,j)].append(k*l+w)
                        break
                    else:
                        break
                #riga sup
                k=i
                w=j
                while(k+1<l):
                    k+=1
                    if(mat[k][w] == ""):
                        if(colore == "b"):
                            diz_b[(i,j)].append(k*l+w)
                        else:
                            diz_n[(i,j)].append(k*l+w)
                    elif(mat[k][w][0] != colore):
                        if(colore == "b"):
                            diz_b[(i,j)].append(k*l+w)
                        else:
                            diz_n[(i,j)].append(k*l+w)
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
                            diz_b[(i,j)].append(k*l+w)
                        else:
                            diz_n[(i,j)].append(k*l+w)
                    elif(mat[k][w][0] != colore):
                        if(colore == "b"):
                            diz_b[(i,j)].append(k*l+w)
                        else:
                            diz_n[(i,j)].append(k*l+w)
                        break
                    else:
                        break
                #riga lat dx
                k=i
                w=j
                while(w+1<l):
                    w+=1
                    if(mat[k][w] == ""):
                        if(colore == "b"):
                            diz_b[(i,j)].append(k*l+w)
                        else:
                            diz_n[(i,j)].append(k*l+w)
                    elif(mat[k][w][0] != colore):
                        if(colore == "b"):
                            diz_b[(i,j)].append(k*l+w)
                        else:
                            diz_n[(i,j)].append(k*l+w)
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
                            diz_b[(i,j)].append(k*l+w)
                        else:
                            diz_n[(i,j)].append(k*l+w)
                    elif(mat[k][w][0] != colore):
                        if(colore == "b"):
                            diz_b[(i,j)].append(k*l+w)
                        else:
                            diz_n[(i,j)].append(k*l+w)
                        break
                    else:
                        break

    return (diz_b,diz_n)

def tot_posizioni_valide(board,l):           
    pos_val_b = 0
    pos_val_n = 0
    
    p_v_p_b = posizioni_valide_pedoni(board,l)[0]
    for key in p_v_p_b:
        for elem in p_v_p_b[key]:
            pos_val_b+=1
    p_v_p_n = posizioni_valide_pedoni(board,l)[1]
    for key in p_v_p_n:
        for elem in p_v_p_n[key]:
            pos_val_n+=1

    p_v_p_b = posizioni_valide_alfieri(board,l)[0]
    for key in p_v_p_b:
        for elem in p_v_p_b[key]:
            pos_val_b+=1
    p_v_p_n = posizioni_valide_alfieri(board,l)[1]
    for key in p_v_p_n:
        for elem in p_v_p_n[key]:
            pos_val_n+=1

    p_v_p_b = posizioni_valide_cavalli(board,l)[0]
    for key in p_v_p_b:
        for elem in p_v_p_b[key]:
            pos_val_b+=1
    p_v_p_n = posizioni_valide_cavalli(board,l)[1]
    for key in p_v_p_n:
        for elem in p_v_p_n[key]:
            pos_val_n+=1

    p_v_p_b = posizioni_valide_regina(board,l)[0]
    for key in p_v_p_b:
        for elem in p_v_p_b[key]:
            pos_val_b+=1
    p_v_p_n = posizioni_valide_regina(board,l)[1]
    for key in p_v_p_n:
        for elem in p_v_p_n[key]:
            pos_val_n+=1

    p_v_p_b = posizioni_valide_re(board,l)[0]
    for key in p_v_p_b:
        for elem in p_v_p_b[key]:
            pos_val_b+=1
    p_v_p_n = posizioni_valide_re(board,l)[1]
    for key in p_v_p_n:
        for elem in p_v_p_n[key]:
            pos_val_n+=1

    p_v_p_b = posizioni_valide_torri(board,l)[0]
    for key in p_v_p_b:
        for elem in p_v_p_b[key]:
            pos_val_b+=1
    p_v_p_n = posizioni_valide_torri(board,l)[1]
    for key in p_v_p_n:
        for elem in p_v_p_n[key]:
            pos_val_n+=1

    return (pos_val_b,pos_val_n) 

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

def calcola_tutte_mosse(board,colore,l):
    diz_b = posizioni_valide_pedoni(board,l)[0]
    diz_n = posizioni_valide_pedoni(board,l)[1]
    if(colore == "b"):
        pvt_b = posizioni_valide_torri(board,l)[0]
        pvc_b = posizioni_valide_cavalli(board,l)[0]
        pva_b = posizioni_valide_alfieri(board,l)[0]
        pvq_b = posizioni_valide_regina(board,l)[0]
        pvr_b = posizioni_valide_re(board,l)[0]
        diz_b = unisci_dizionari(diz_b,pvt_b)
        diz_b = unisci_dizionari(diz_b,pvc_b)
        diz_b = unisci_dizionari(diz_b,pva_b)
        diz_b = unisci_dizionari(diz_b,pvq_b)
        diz_b = unisci_dizionari(diz_b,pvr_b)  
        return diz_b  
    else:
        pvt_n = posizioni_valide_torri(board,l)[1]
        pvc_n = posizioni_valide_cavalli(board,l)[1]
        pva_n = posizioni_valide_alfieri(board,l)[1]
        pvq_n = posizioni_valide_regina(board,l)[1]
        pvr_n = posizioni_valide_re(board,l)[1]
        diz_n = unisci_dizionari(diz_n,pvt_n)
        diz_n = unisci_dizionari(diz_n,pvc_n)
        diz_n = unisci_dizionari(diz_n,pva_n)
        diz_n = unisci_dizionari(diz_n,pvq_n)
        diz_n = unisci_dizionari(diz_n,pvr_n)
        return diz_n
