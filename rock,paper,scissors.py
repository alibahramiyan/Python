import random
level = 1
x = 0
y = 0
while True:
    b = random.choice(['rock', 'paper', 'scissors'])
    a = input('please select: rock, paper, scissors')
    if (a == 'rock'and b == 'paper')or(a == 'paper' and b == 'scissors')or(a == 'scissors' and b == 'rock'):
        print('cpu win')
        x += 1
        print('cpu score is :',(x))
        print('user score is :',(y))

    elif (a == 'rock'and b == 'scissors')or(a == 'paper'and b == 'rock')or(a == 'scissors' and b == 'paper'):
        print('user win')
        y += 1
        print('cpu score is :',(x))
        print('user score is :',(y))
    else:
        print('draw')
    level += 1
    print('level : ',level)

