


                                    #### Python Project 6: Tic-Tac-Toe Game ####

from random import randint
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
hum = []
com = []


def human():
    print("Human's turn: ")
    #human_moves = []
    num  = int(input('Select the cell: '))
    hum.append(num)
    print(f'Human Moves: {hum}')
    if num == 1:
        #print("Enter either 'x' or 'o'")
        move = 'x'
        a[0] = move
        print(a)
        print(b)
        print(c)
    elif num == 2:
        #print("Enter either 'x' or 'o'")
        move = 'x'
        a[1] = move
        print(a)
        print(b)
        print(c)
    elif num == 3:
        #print("Enter either 'x' or 'o'")
        move = 'x'
        a[2] = move
        print(a)
        print(b)
        print(c)
    elif num == 4:
        #print("Enter either 'x' or 'o'")
        move = 'x'
        b[0] = move
        print(a)
        print(b)
        print(c)
    elif num == 5:
        #print("Enter either 'x' or 'o'")
        move = 'x'
        b[1] = move
        print(a)
        print(b)
        print(c)
    elif num == 6:
        #print("Enter either 'x' or 'o'")
        move = 'x'
        b[2] = move
        print(a)
        print(b)
        print(c)
    elif num == 7:
        #print("Enter either 'x' or 'o'")
        move = 'x'
        c[0] = move
        print(a)
        print(b)
        print(c)
    elif num == 8:
        #print("Enter either 'x' or 'o'")
        move = 'x'
        c[1] = move
        print(a)
        print(b)
        print(c)
    elif num == 9:
        # print("Enter either 'x' or 'o'")
        #move = input("Enter 'x': ")
        move = 'x'
        c[2] = move
        print(a)
        print(b)
        print(c)

    hum_rules()
    print("Computer's turn: ")
    computer()



def computer():
    #print(hum)
    #print("Computer's turn: ")
    #computer_moves = []
    num = randint(1,9)
    #num = int(input('Select the cell: '))
    if num in hum:
        #print('This move is not allowed')
        computer()
    elif num in com:
        #print('This move is not allowed')
        computer()
    else:
        #print(f'Computer selected cell: {num}')
        com.append(num)
        print(f'Computer Moves: {com}')
    if num == 1:
        move = 'o'
        print(f"Enter 'o': {move}")
        a[0] = move
        print(a)
        print(b)
        print(c)
    elif num == 2:
        move = 'o'
        print(f"Enter 'o': {move}")
        a[1] = move
        print(a)
        print(b)
        print(c)
    elif num == 3:
        move = 'o'
        print(f"Enter 'o': {move}")
        a[2] = move
        print(a)
        print(b)
        print(c)
    elif num == 4:
        move = 'o'
        print(f"Enter 'o': {move}")
        b[0] = move
        print(a)
        print(b)
        print(c)
    elif num == 5:
        move = 'o'
        print(f"Enter 'o': {move}")
        b[1] = move
        print(a)
        print(b)
        print(c)
    elif num == 6:
        move = 'o'
        print(f"Enter 'o': {move}")
        b[2] = move
        print(a)
        print(b)
        print(c)
    elif num == 7:
        move = 'o'
        print(f"Enter 'o': {move}")
        c[0] = move
        print(a)
        print(b)
        print(c)
    elif num == 8:
        move = 'o'
        print(f"Enter 'o': {move}")
        c[1] = move
        print(a)
        print(b)
        print(c)
    elif num == 9:
        move = 'o'
        print(f"Enter 'o': {move}")
        c[2] = move
        print(a)
        print(b)
        print(c)
    com_rules()
    human()


def hum_rules():
    #Rule1 (If Columns are equal)
    #print('These are the rules')

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
    exit()



print(".............Let's play Tic-Tac-Toe game.............")
print("You can enter either 'x' or 'o' in the canvas")
print('You can type 1 to select cell 1,\
         You can type 2 to select cell 2,\
         You can type 3 to select cell 3,\
         You can type 4 to select cell 4,\
         You can type 5 to select cell 5,\
         You can type 6 to select cell 6,\
         You can type 7 to select cell 7,\
         You can type 8 to select cell 8,\
         You can type 9 to select cell 9'
     )
human()






