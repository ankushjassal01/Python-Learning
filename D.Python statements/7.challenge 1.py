#%%
import random
higest=10
answer=random.randint(1,higest)
print(answer)
print('please guess number b/w 1 to',higest,'Enter here : ')
guess=0
while guess != answer:
    guess=int(input())
    if guess== 0:
        print('you out of the game')
        break
    if guess == answer:
        print('your answer is correct')
        print('game over,you Win')
        break
    else:
        if guess > answer:
            print('sorry you guess is incorrect.Please guess lower (to terminate game print 0)')
        elif guess < answer:
            print('sorry you guess is incorrect.Please guess higher (to terminate game print 0)')
#%%
choices=('''please choose any one option from below:\n\t1.learning
    2.reading
    3.writing
    4.all three above
    0:Exit from game''')
print(choices)
while True:
    A =input('\t')
    if A=='1':
        print('\t learn ABC')
    if A=='2':
        print('\t Read ABC ')
    if A=='3':
        print('\t Write ABC ')
    if A=='4':
        print('\t start learning ABC by reading/writing ')
    if A=='0':
        print('\tyou are out of game now')
        break
    if A not in '01234':
        print(choices.replace('please choose any one option from below:','you choose a wrong choice please choose again'))