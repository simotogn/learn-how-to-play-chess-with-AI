from posizioni_valide import tot_posizioni_valide

# Tabella per il pedone 
spostaAvanti = [
      0,  0,  0,  0,  0,  0,  0,  0,
	  5, 10, 15, 20, 20, 15, 10,  5,
	  4,  8, 12, 16, 16, 12,  8,  4,
	  3,  6,  9, 12, 12,  9,  6,  3,
	  2,  4,  6,  8,  8,  6,  4,  2,
	  1,  2,  3,  4,  4,  3,  2,  1,
	  0,  0,  0, -4, -4,  0,  0,  0,
	  0,  0,  0,  0,  0,  0,  0,  0]

# Tabella per il cavallo e l'alfiere 
alCentro = [
    0,  0,  0,  0,  0,  0,  0,  0,
	0,  0,  0,  0,  0,  0,  0,  0,
	0,  0,  5,  5,  5,  5,  0,  0,
	0,  0,  5, 10, 10,  5,  0,  0,
	0,  0,  5, 10, 10,  5,  0,  0,
	0,  0,  5,  5,  5,  5,  0,  0,
	0,  0,  0,  0,  0,  0,  0,  0,
	0, -5, -4,  0,  0, -4, -5,  0]

# Il vettore RuotaScacchiera usato per ottenere il valore della posizione dei pezzi neri 
RuotaScacchiera = [
	 56,  57,  58,  59,  60,  61,  62,  63,
	 48,  49,  50,  51,  52,  53,  54,  55,
	 40,  41,  42,  43,  44,  45,  46,  47,
	 32,  33,  34,  35,  36,  37,  38,  39,
	 24,  25,  26,  27,  28,  29,  30,  31,
	 16,  17,  18,  19,  20,  21,  22,  23,
	  8,   9,  10,  11,  12,  13,  14,  15,
	  0,   1,   2,   3,   4,   5,   6,   7]

def valorePezzi(pezzo):
    if(pezzo == "nP" or pezzo == "bP"):
        return 100
    elif(pezzo == "nC" or pezzo == "bC" or pezzo == "nA" or pezzo == "bA"):
        return 300   
    elif(pezzo == "nQ" or pezzo == "bQ"):
        return 900
    elif(pezzo == "nT" or pezzo == "bT"):
        return 500
    elif(pezzo=="nR" or pezzo=="bR"):
        return 60000
    else:
        return 0

#valuta una posizione sulla scacchiera
def valuta(board):
    punteggioBianco = 0
    punteggioNero = 0
    for i in range(8):
        for j in range(8):
            if (board[i][j] != ""):
                if (board[i][j][0] == "b"):
                    # valore del pezzo
                    punteggioBianco += valorePezzi(board[i][j])
                    # posizione del pezzo 
                    if(board[i][j][1] == "P"):
                        punteggioBianco += spostaAvanti[i*8+j]
                    elif (board[i][j][1] == "C"):
                        punteggioBianco += alCentro[i*8+j]
                    elif (board[i][j][1] == "A"):
                        punteggioBianco += alCentro[i*8+j]  
                elif (board[i][j][0] == "n"):
                    # valore del pezzo
                    punteggioNero += valorePezzi(board[i][j])
                    # posizione del pezzo 
                    if(board[i][j][1] == "P"):
                        punteggioNero += spostaAvanti[RuotaScacchiera[i*8+j]]
                    elif (board[i][j][1] == "C"):
                        punteggioNero += alCentro[RuotaScacchiera[i*8+j]]
                    elif (board[i][j][1] == "A"):
                        punteggioNero += alCentro[RuotaScacchiera[i*8+j]] 
    punteggioBianco += tot_posizioni_valide(board)[0] * 100
    punteggioNero += tot_posizioni_valide(board)[1] * 100
    return (punteggioBianco,punteggioNero)
    




