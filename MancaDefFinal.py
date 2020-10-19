import random
#Funcion que verifica que el movimiento es legal
def verMov(array, pos):
    if array[pos] >0 :
        return True
    else: 
        return False
#Reinicia el tablero al terminar
def clean(board):
    for i in range(5):
        board[i]= 0
    for i in range (6,11):
        board[i]= 0
#Muestra el tablero
def sBoard(ia, p1):
    ia.reverse()
    print('IA 11 10  9  8  7')
    print(ia[:1], ia[1:6])
    print('   ', p1[0:5],p1[5:])
    print('P1:  0  1  2  3  4')
    ia.reverse()
#Funcion para manejo de juego
def play(turn, board, move):
    vIA = sum(board[0:5])
    vP1 = sum(board[6:11])
    if(vIA!= 0 and vP1!=0): 
        if(verMov(board, move) == True):
            over = True
            dot = board[move]
            board[move] = 0
            while dot > 0:
                move += 1
                if move == 12:
                    move = 0
                if dot == 1 and turn == 0:
                    if move == 5:
                        cTurn = 0
                    else: 
                        cTurn = 1
                if dot == 1 and turn == 1:
                    if move == 11:
                        cTurn = 1
                    else: 
                        cTurn = 0
                if turn == 0: 
                    if move == 11:
                        move = 0 
                if turn == 1: 
                    if move == 6:
                        move = 0 
                if dot == 1 and board[move] == 0 and turn == 0 and move <= 4 and move != 5 and  board[10 - move] != 0 :
                    sDot = board[10 - move]
                    board[5] += sDot +1
                    board[10-move] = 0  
                    board[move] = 0
                    turn = 1
                elif dot == 1 and board[move] == 0 and turn == 1 and move >= 6 and move != 11  and  board[10 - move] != 0:
                    sDot = board[10 - move]
                    board[11] += sDot +1
                    board[10-move] = 0  
                    board[move] = 0
                    turn = 0
                else: 
                    board[move] += 1    
                dot -= 1
                vP1 = sum(board[0:5])
                vIA = sum(board[6:11])
                if vIA == 0 or vP1 == 0:
                    over = False 
                    board[11] += vIA
                    board[5] += vP1
                    clean(board)
            return board, cTurn, over
#Funcion que dictamina como termino el juego
def verW(board):
    if board[5] > board[11]:
        return 0
    if board[11] > board[5]:
        return 1
    if board[11] == board[5]:
        return 2
#Se encarga de la simulacion del juego contra la maquina
def simGame(board, move):
    turn = 1
    cP1 = [0,1,2,3,4]
    cIa = [6,7,8,9,10]
    board, turn, over = play(turn, board, move)
    while over == True:
        if turn == 0 and over == True:
            move = random.choice(cP1)
            if verMov(board, move):
                if move <= 5: 
                    board, turn, over = play(0, board, move)
        if turn == 1 and over == True: 
            move = random.choice(cIa)
            if verMov(board, move):
                if  move > 5 and move < 11:
                    board, turn, over = play(1, board, move)
    return verW(board)
#Movimientos
def lMov(board, array):
    lm = []
    if verMov(board, array[0]) == True:
        lm.append(array[0])    
    if verMov( board, array[1]) == True:
        lm.append(array[1])
    if verMov( board, array[2]) == True:
        lm.append(array[2])
    if verMov( board, array[3]) == True:
        lm.append(array[3])
    if verMov( board, array[4]) == True:
        lm.append(array[4])
    return lm