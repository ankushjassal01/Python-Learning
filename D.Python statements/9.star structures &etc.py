for i in range(1,11):
    print('*'*i ,end =' ')
print()
for j in range(10,0,-1):
        print('*'*j)
    
#%%
u_input=input('pleasetype the sentence or word :')
Vowel='aeiou'
output={}
for char in u_input.casefold():
    if char in Vowel:
        if char in output.keys():
            # output[char]=output[char]+1
            # output['a']=output['a']+1
            # output['a']=1+1
            # output['a']=2
            output[char]+=1 
        else:
            # to create or append the key and default first value
            # the key in dict concatination dont work so we need to do that
            output.update({char:1})
print(output)

#%%
u_input='Ankush Jassal'     # input('pleasetype the sentence or word :')
Vowel='aeiou'
output={}
for char in u_input.casefold():
    if char in Vowel:
        if char in output.keys():
            # output[char]=output[char]+1
            # output['a']=output['a']+1
            # output['a']=1+1
            # output['a']=2
            output[char]+=1 
        else:
            # to create or append the key and default first value
            # the key in dict concatination dont work so we need to do that
            output[char]=1 
print(output) 
#%%
menu = [
    ['egg', 'bacon'],
    ['egg', 'sausage', 'bacon'],
    ['egg', 'spam'],
    ['egg', 'sausage', 'bacon', 'spam'],
    ['spam', 'sausage', 'bacon', 'spam'],
    ['spam', 'sausage', 'spam', 'bacon', 'spam', 'spam', 'tomato', 'spam'],
    ['spam', 'egg', 'spam', 'spam', 'bacon', 'spam'], ]
for meal in menu:
    for item in meal:
        if item != 'spam':
            print(item,end=' ')
    print()
#%%
menu = [
    ['egg', 'bacon'],
    ['egg', 'sausage', 'bacon'],
    ['egg', 'spam'],
    ['egg', 'sausage', 'bacon', 'spam'],
    ['spam', 'sausage', 'bacon', 'spam'],
    ['spam', 'sausage', 'spam', 'bacon', 'spam', 'spam', 'tomato', 'spam'],
    ['spam', 'egg', 'spam', 'spam', 'bacon', 'spam'], 
    ]   
for meal in menu:
    # if 'spam' not in meal:
    #     print(meal)
    # else:
    for index in range(len(meal)-1,-1,-1):
            if meal[index] == 'spam':
                meal.remove('spam')
    print(meal)
print(menu)


#%%
for row in range(0,7):
    for col in range(0,7):
        if (col == 0 or col == 6):
            print('*', end='')
        elif (row == 1 and (col == 2 or col == 5)):
            print('*', end='')
        elif (row == 2 and (col == 2 or col == 4 )):
            print('*',end='')
        elif row == col ==3:
            print('*',end='')
        else:
            print(' ',end='')
    print()    # this used to end the inner for loop end keyword, if not used then next outer for loop will start printing on same line



for row in range(0,7):
    for col in range(0,7):
        if (row ==0 and col == 3):
            print('*' ,end='')
        elif (row ==1 and (col ==2 or col == 4)):
            print('*',end='')
        elif (row==2 and (0 <col<=3)):
            print('*',end=' ')
        elif (row ==3 and (col==0 or col==5)):
            print('*',end=' ')
        else:
            print(' ',end='')
    print()

