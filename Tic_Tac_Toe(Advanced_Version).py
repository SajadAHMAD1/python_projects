


                                    #### Python Project 6: Tic-Tac-Toe Game ####
#Programmer: Dr. Sajad Ahmad Rather
#Language: Python
#Dated: 10th June 2023

from random import randint
import time
a = ['|   |','|   |','|   |']
b = ['|   |','|   |','|   |']
c = ['|   |','|   |','|   |']
hum = []
com = []


def human():
    #print("Human's turn: ")
    #human_moves = []
    #num  = input('Select the cell: ')
    num = int(input("Human's turn: "))
    hum.append(num)
    #print(f'Human Moves: {hum}')
    if num == 1:
        #print("Enter either 'x' or 'o'")
        move = '| X |'
        a[0] = move
        print(' '. join(a))
        print(' '. join(b))
        print(' '. join(c))
    elif num == 2:
        #print("Enter either 'x' or 'o'")
        move = '| X |'
        a[1] = move
        print(' '.join(a))
        print(' '.join(b))
        print(' '.join(c))
    elif num == 3:
        #print("Enter either 'x' or 'o'")
        move = '| X |'
        a[2] = move
        print(' '.join(a))
        print(' '.join(b))
        print(' '.join(c))
    elif num == 4:
        #print("Enter either 'x' or 'o'")
        move = '| X |'
        b[0] = move
        print(' '.join(a))
        print(' '.join(b))
        print(' '.join(c))
    elif num == 5:
        #print("Enter either 'x' or 'o'")
        move = '| X |'
        b[1] = move
        print(' '.join(a))
        print(' '.join(b))
        print(' '.join(c))
    elif num == 6:
        #print("Enter either 'x' or 'o'")
        move = '| X |'
        b[2] = move
        print(' '.join(a))
        print(' '.join(b))
        print(' '.join(c))
    elif num == 7:
        #print("Enter either 'x' or 'o'")
        move = '| X |'
        c[0] = move
        print(' '.join(a))
        print(' '.join(b))
        print(' '.join(c))
    elif num == 8:
        #print("Enter either 'x' or 'o'")
        move = '| X |'
        c[1] = move
        print(' '.join(a))
        print(' '.join(b))
        print(' '.join(c))
    elif num == 9:
        # print("Enter either 'x' or 'o'")
        #move = input("Enter 'x': ")
        move = '| X |'
        c[2] = move
        print(' '.join(a))
        print(' '.join(b))
        print(' '.join(c))

    hum_rules()
    ###Add some break###
    time.sleep(0.9)
    print("Computer's turn: ")
    computer()

def computer():
    #print(hum)
    #print("Computer's turn: ")
    #computer_moves = []
    num = randint(1,9)

    ###Test Purpose###
    #num = str(input('Select the cell: '))
    ####  #### ####

    if num in hum:
        #print('This move is not allowed')
        computer()
    elif num in com:
        #print('This move is not allowed')
        computer()
    else:
        #print(f'Computer selected cell: {num}')
        com.append(num)
        #print(f'Computer Moves: {com}')
    if num == 1:
        print(f'Computer selected cell {num}')
        move = '| O |'
        a[0] = move
        print(' '.join(a))
        print(' '.join(b))
        print(' '.join(c))
    elif num == 2:
        print(f'Computer selected cell {num}')
        move = '| O |'
        a[1] = move
        print(' '.join(a))
        print(' '.join(b))
        print(' '.join(c))
    elif num == 3:
        print(f'Computer selected cell {num}')
        move = '| O |'
        a[2] = move
        print(' '.join(a))
        print(' '.join(b))
        print(' '.join(c))
    elif num == 4:
        print(f'Computer selected cell {num}')
        move = '| O |'
        b[0] = move
        print(' '.join(a))
        print(' '.join(b))
        print(' '.join(c))
    elif num == 5:
        print(f'Computer selected cell {num}')
        move = '| O |'
        b[1] = move
        print(' '.join(a))
        print(' '.join(b))
        print(' '.join(c))
    elif num == 6:
        print(f'Computer selected cell {num}')
        move = '| O |'
        b[2] = move
        print(' '.join(a))
        print(' '.join(b))
        print(' '.join(c))
    elif num == 7:
        print(f'Computer selected cell {num}')
        move = '| O |'
        c[0] = move
        print(' '.join(a))
        print(' '.join(b))
        print(' '.join(c))
    elif num == 8:
        print(f'Computer selected cell {num}')
        move = '| O |'
        c[1] = move
        print(' '.join(a))
        print(' '.join(b))
        print(' '.join(c))
    elif num == 9:
        print(f'Computer selected cell {num}')
        move = '| O |'
        c[2] = move
        print(' '.join(a))
        print(' '.join(b))
        print(' '.join(c))
    com_rules()
    human()


def hum_rules():
    #Rule1 (If Columns are equal)
    #print('These are the rules')
    # a[0] == 'X'
    # b[0] == 'X'
    # c[0] == 'X'
    # a[1] == 'X'
    # b[1] == 'X'
    # c[1] == 'X'
    # a[2] == 'X'
    # b[2] == 'X'
    # c[2] == 'X'
    if ((a[0] == '|   |') and (b[0] == '|   |') and (c[0] == '|   |')) or ((a[1] == '|   |') and (b[1] == '|   |') and (c[1] == '|   |')) or \
            ((a[2] == '|   |') and (b[2] == '|   |') and (c[2] == '|   |')) or \
            ((a[0] == '|   |') and (a[1] == '|   |') and (a[2] == '|   |')) or ((b[0] == '|   |') and (b[1] == '|   |') and (b[2] == '|   |')) or \
            ((c[0] == '|   |') and (c[1] == '|   |') and (c[2] == '|   |')) or \
            ((a[0] == '|   |') and (b[1] == '|   |') and (c[2] == '|   |')) or \
            ((c[0] == '|   |') and (b[1] == '|   |') and (a[2] == '|   |')):
        time.sleep(0.9)
        print("Computer's turn: ")
        computer()
    else:
        if ((a[0] == b[0]) and (b[0] == c[0])) or ((a[1] == b[1]) and (b[1] == c[1])) or \
                ((a[2] == b[2]) and (b[2] == c[2])):
            print('Human won!')
            GameOver()
            # Rule2 (If Rows are equal)
        elif ((a[0] == a[1]) and (a[1] == a[2])) or ((b[0] == b[1]) and (b[1] == b[2])) or \
                ((c[0] == c[1]) and (c[1] == c[2])):
            print('Human won!')
            GameOver()
     # Rule3 (If one or two Diagonals are equal)
        elif ((a[0] == b[1]) and (b[1] == c[2])) or ((c[0] == b[1]) and (b[1] == a[2])):
            print('Human won!')
            GameOver()
        elif len(hum) == 5:
            print('Game Draw!')
            print('\n')
            GameOver()


def com_rules():
    #Rule1 (If Columns are equal)
    #print('These are the rules')
    if ((a[0] == '|   |') and (b[0] == '|   |') and (c[0] == '|   |')) or ((a[1] == '|   |') and (b[1] == '|   |') and (c[1] == '|   |')) or \
            ((a[2] == '|   |') and (b[2] == '|   |') and (c[2] == '|   |')) or \
            ((a[0] == '|   |') and (a[1] == '|   |') and (a[2] == '|   |')) or ((b[0] == '|   |') and (b[1] == '|   |') and (b[2] == '|   |')) or \
            ((c[0] == '|   |') and (c[1] == '|   |') and (c[2] == '|   |')) or \
            ((a[0] == '|   |') and (b[1] == '|   |') and (c[2] == '|   |')) or \
            ((c[0] == '|   |') and (b[1] == '|   |') and (a[2] == '|   |')):
        time.sleep(0.9)
        human()
    else:
        if ((a[0] == b[0]) and (b[0] == c[0])) or ((a[1] == b[1]) and (b[1] == c[1])) or \
                ((a[2] == b[2]) and (b[2] == c[2])):
            print('Computer won!')
            GameOver()
        # Rule2 (If Rows are equal)
        elif ((a[0] == a[1]) and (a[1] == a[2])) or ((b[0] == b[1]) and (b[1] == b[2])) or \
                ((c[0] == c[1]) and (c[1] == c[2])):
            print('Computer won!')
            GameOver()
        # Rule3 (If one or two Diagonals are equal)
        elif ((a[0] == b[1]) and (b[1] == c[2])) or ((c[0] == b[1]) and (b[1] == a[2])):
            print('Computer won!')
            GameOver()
        elif len(com) == 5:
            print('Game Draw!')
            print('\n')
            GameOver()


def GameOver():
    print('...Thank you for playing the game...')
    time.sleep(3)
    exit()



print(".............Let's play Tic-Tac-Toe game.............")

print('This is the canvas: ')

a1 = ['| 1 |','| 2 |','| 3 |']
b1 = ['| 4 |','| 5 |','| 6 |']
c1 = ['| 7 |','| 8 |','| 9 |']

print(' '.join(a1))
print(' '.join(b1))
print(' '.join(c1))


print('Human has to type the digit to select the cell in the canvas')
print('Human: X  Computer: O')
human()






