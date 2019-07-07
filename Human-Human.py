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

