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



answer = None
Bool = True
number = input('write the Number: ')
while Bool:
    temp = 0
    for i in number:
        i = int(i)
        temp += i
    number = '{}'.format(temp)
    if len(number) == 1:
        answer = temp
        print(answer)
        Bool = False




n = int(input('enter the number: '))
total = 0
final = 0
while n > 0:
    dig = n%10
    total += dig  # total = total +dig (augments assignment)
    n = n//10
    # if while loop end here it will give us answer in more then 1 digits for total of n more then 9
    # so below might help to get the answer again
if len(str(total)) != 1:
    for i in str(total):
        i = int(i)
        final += i
    print(final)
else:
    final = total
    print(final)


def arr(n):
    n= str(n) #
    answer='' # str
    for i in n:
        if n.count(i) == 1:
            answer += i
    return int(answer)

    # for i in n:
    #     if i in temp:
    #         temp[i] += 1
    #     else:
    #         temp[i]= 1
    # for j in temp:
    #     if temp[j]==1:
    #        answer += j
    # return int(answer)

print(arr(1213245172962468))



def coat_price_for(months_of_service,month_service_payment):
    total_month=12
    served_month = months_of_service
    year_service_payment= 240
    temp=months_of_service/total_month
    C=((temp*year_service_payment)-month_service_payment)/(1-temp)
    return C


print(coat_price_for(9,150))


