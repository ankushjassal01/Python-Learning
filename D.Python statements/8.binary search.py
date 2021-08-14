# in binary search we can divide our data set into half and find the value in it.
# if data present in first half then we will follow the first half data set 
# if data present in second half then we will follow the second half data set
# in both data set we need to find it mid point . and then if it again gives us 
# two data set. if it lies in that dataset.1st half then in that dataset we will 
# we will follow same procedure of half
# this binary search method divide the dataset into two parts and by mid point we
# can find our required value

# like we need to find the value in 1(lowest) to 10(highest) 
# its doesnt required more then 5 gues
# like i guess 9. So computer will ask me if data present in 1 to 10 then give me 
# its mid point which is 5 then i have to guess higher . which give us data set of 
# 6(lowest(previous guess) +1) to 10 . it will again round of it to its mid oint which 
# is 8. if its higher then that then again 9 (lowest(previous guess) +1)  to 10
#formula is lowest +(high-lowest)//2
#in that data set it will give me 9

import randoml
high=1000
low=1
answer=random.randint(low,high)
guess=1
guesses=1
print(answer)
while guess != answer:
    guess=low+(high-low)//2
    com_guess=input('My guess is {}. should i guess high, then type h ? should i guess low then type l ? if correct then type c = '.format(guess))
    if com_guess =='h':
        low=guess+1
    if com_guess =='l':
        high=guess-1
    if com_guess == 'c':
        print('your number is {}. i took {} guesses'.format(guess, guesses))
        break
    guesses=guesses+1