l=[1,2,3,4,5,6,7,8,9]
# l1=[1,2,3,4,5,6,7,8,9]
user1_value='X'
user2_value='O'
def choose_signature():
    user1_value=input('Enter your signature character')
    user2_value=input('Enter your signature character')

win=False

def basic():
    def user1_info():
        user1_position = int(input(" First person enter your position "))
        l[user1_position]=user1_value
        structure()

    def user2_info():
        user2_position = int(input(" Second person enter your position "))
        l[user2_position] = user2_value
        structure()

    def structure():
        print('        |        |          \n    {}   |    {}   |    {}    \n        |        |         '.format(l[6],l[7],l[8]))
        print('--------+--------+---------')
        print('        |        |          \n    {}   |    {}   |    {}    \n        |        |         '.format(l[3],l[4],l[5]))
        print('--------+--------+---------')
        print('        |        |          \n    {}   |    {}   |    {}    \n        |        |         \n'.format(l[0],l[1],l[2]))

    structure()
    user1_info()
    user2_info()

basic()
def win():
    if(l[0]=='X' & l[1]=='X' & l[2]=='X'):
        print('Player 1 wins')
        win=True
    elif (l[0] == 'X' & l[4] == 'X' & l[8] == 'X'):
        print('Player 1 wins')
        win = True
    elif (l[8] == 'X' & l[5] == 'X' & l[2] == 'X'):
        print('Player 1 wins')
        win = True
    elif (l[6] == 'X' & l[7] == 'X' & l[8] == 'X'):
        print('Player 1 wins')
        win = True
    elif (l[6] == 'X' & l[4] == 'X' & l[2] == 'X'):
        print('Player 1 wins')
        win = True
    elif (l[6] == 'X' & l[3] == 'X' & l[0] == 'X'):
        print('Player 1 wins')
        win = True
    elif (l[3] == 'X' & l[4] == 'X' & l[5] == 'X'):
        print('Player 1 wins')
        win = True
    elif (l[7] == 'X' & l[4] == 'X' & l[1] == 'X'):
        print('Player 1 wins')
        win = True
    elif (l[0] == 'O' & l[1] == 'O' & l[2] == 'O'):
        print('player 2 wins')
        win = True
    elif (l[0] == 'O' & l[4] == 'O' & l[8] == 'O'):
        print('player 2 wins')
        win = True
    elif (l[8] == 'O' & l[5] == 'O' & l[2] == 'O'):
        print('player 2 wins')
        win = True
    elif (l[6] == 'O' & l[7] == 'O' & l[8] == 'O'):
        print('player 2 wins')
        win = True
    elif (l[6] == 'O' & l[4] == 'O' & l[2] == 'O'):
        print('player 2 wins')
        win = True
    elif (l[6] == 'O' & l[3] == 'O' & l[0] == 'O'):
        print('player 2 wins')
        win = True
    elif (l[3] == 'O' & l[4] == 'O' & l[5] == 'O'):
        print('player 2 wins')
        win = True
    elif (l[7] == 'O' & l[4] == 'O' & l[1] == 'O'):
        print('player 2 wins')
        win = True

