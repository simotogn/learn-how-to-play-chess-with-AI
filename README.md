# Learn-how-to-play-chess-with-AI

Bachelor Thesis in Computer Science Engineering at La Sapienza - Università di Roma

Ho implementato il gioco degli scacchi in versione tradizionale, con scacchiera 8x8 e, in versione Gardner Chess, con scacchiera 5x5.

Nella versione tradizionale ho implementato la possibilita' di giocare contro un'AI, realizzata con un algoritmo di ricerca in profondita', ovvero il minimax con potatura apha-beta (di cui un esempio e' illustrato in figura).

 ![Image text](https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/AB_pruning.svg/700px-AB_pruning.svg.png) 

Anche nella versione Gardner Chess 5x5 ho implementato la possibilita' di giocare contro un'AI, ovvero, sia il minimax con potatura alpha-beta, che il Monte Carlo Tree Search, un algoritmo di ricerca che usa Reinforcement Learing e la legge dei grandi numeri per scegliere la mossa migliore da effettuare.

Nella versione tradizionale il minimax puo' essere usato fino a profondita' 4 (ovvero 5 semimosse) con un tempo ragionevole (<40 sec). 
Nella versione di Gardner il minimax puo' essere usato fino a profondita' 6 (7 semimosse) con un tempo ragionevole (<1 min e 30 sec) e il mcts con tempo minore ai 3 sec.

Per il corretto funzionamento dell'algoritmo minimax e' stata realizzata un'evaluation function, che valuta la scacchiera in base al valore dei pezzi restanti e alla posizione di pedoni, cavalli e alfieri nella versione tradizionale e solo in base al valore dei pezzi restanti sulla scacchiera nella versione di Gardner.

La versione di scacchi 5x5 e' stata realizzata per poter far giocare un robot con gli algoritmi citati sopra, senza che faccia cadere i pezzi sulla scacchiera.

Inoltre è stata realizzata una chess pieces detection, che partendo da una foto di una scacchiera riesca ad identificare i pezzi sopra di essa e produrre in output la matrice che rappresenta tale scacchiera. Il link al lavoro svolto su colab è il seguente:
https://colab.research.google.com/drive/1OOiH7vUv6m47HOVsuLyv6D8BGxFuXPIE?usp=sharing

Simone Tognocchi 1882405.
