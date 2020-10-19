from MancaDefFinal import *
import random
import copy
level = 500
print("Bienvenido")
print("Ingrese su dificultad")
print("1.Facil")
print("2.Medio")
print("3.Dificil")
dif=input("Ingrese su dificultad: ")
if dif=="1":
    level = 1
elif dif=="2":
    level = 500
elif dif=="3":
    level = 1000

board = [4,4,4,4,4,0,4,4,4,4,4,0]
turn = 0
mIA = [9,10,6,8,7]
cont= [0,0,0,0,0]
over = True
sBoard( board[6:12], board[0:6])
while(over):
    if turn == 0 and over == True:
        move = int(input("Seleccione casilla del 0 al 4: "))
        if move <6 and  verMov(board, move): 
            board, turn, over = play(0,board, move)
            print("##########################################")
            sBoard( board[6:12], board[0:6])
    elif turn == 1 and over == True: 
        cont = [0, 0, 0, 0, 0]
        #Implementacion del algoritmo de montecarlo
        for i in range(0, level):
            try: 
                brd2 = copy.deepcopy(board)
                pmov = lMov(brd2, mIA)  
                move = random.choice(pmov)
                if move in pmov:
                    if verMov(brd2, move):
                        verW = simGame(brd2, move)
                        if move == 6 and verW == 1:
                            cont[0] = cont[0] + verW
                        elif move == 7  and verW == 1:
                            cont[1] = cont[1] + verW
                        elif move == 8  and verW == 1:
                            cont[2] = cont[2] + verW
                        elif move == 9 and verW == 1:
                            cont[3] = cont[3] + verW
                        elif move == 10 and verW == 1:
                            cont[4] = cont[4] + verW
            except: 
                a =1
        mov = max(cont)
        if verMov(board, (cont.index(mov) + 6)) and turn == 1:
            if cont.index(mov) == 0:
                board, turn, over = play(1,board, 6)
                sBoard( board[6:12], board[0:6])
            elif cont.index(mov) == 1:
                board, turn, over = play(1,board, 7)
                sBoard( board[6:12], board[0:6])
            elif cont.index(mov) == 2:
                board, turn, over = play(1,board, 8)
                sBoard( board[6:12], board[0:6])
            elif cont.index(mov) == 3:
                board, turn, over = play(1,board, 9)
                sBoard( board[6:12], board[0:6])
            elif cont.index(mov) == 4:
                board, turn, over = play(1,board, 10)
                sBoard( board[6:12], board[0:6])
