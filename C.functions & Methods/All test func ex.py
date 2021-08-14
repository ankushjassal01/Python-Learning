# sum of even numbers but failed test case in hackerrank
range_output = int(input('write the input'))
a=1
b=2
sum=0
for i in range(1,range_output+1):
    if 1<= i <=2:
        output =i
        if output <= range_output:
            if output % 2 ==0:
                sum += output
    else:
        output = a+b
        a = b
        b = output
        if output <= range_output:
            if output % 2 ==0:
                sum += output
print(sum)





# recursion function uses
def sum2_one_digit(n):
    n = str(n)
    temp = 0
    if len(n) == 1:
        return n
    else:
        for i in n:
            i = int(i)
            temp += i
        if len(str(temp)) == 1:
            return temp
        else:
            return sum2_one_digit(temp)  # recursion function


print(sum2_one_digit(888888888888888888888))  # 21*8 =168 =15 = 6


# %%binary numbers
L = 1
H = 1000

# print("Please think of a number between 1 and 1000")
# input("Press ENTER to start")


def guess_binary(answer, low, high):
    guesses = 1
    while True:
        # print("\tGuessing in the range {} to {}".format(low, high))
        guess = low + (high - low) // 2
        # high_low = input("My guess is {}. Should I guess higher or lower? Enter h or l, or c if my guess was correct."
        #                  .format(guess)).casefold()

        # if high_low == "h":
        if guess < answer:
            # I have to guess higher.  The low end of the range becomes 1 greater than the guess.
            low = guess + 1
        # elif high_low == "l":
        elif guess > answer:
            # I have to guess lower.  The high end of the range becomes 1 less than the guess.
            high = guess - 1
        # elif high_low == "c":
        elif guess == answer:
            # print("I got it in {} guesses!".format(guesses))
            # break
            return guesses
        # else:
        #     print("Please enter h, l or c")

        guesses += 1

count_num=0
for number in range(L, H + 1):
    number_of_guesses = guess_binary(number, L, H)
    if number_of_guesses == 10:
        count_num+=1
print("{} guessed in {}".format(count_num, number_of_guesses))


def fizz_buzz(number: int) -> str:
    """
    Play Fizz buzz

    :param number: The number to check.
    :return: 'fizz' if the number is divisible by 3.
        'buzz' if it's divisible by 5.
        'fizz buzz' if it's divisible by both 3 and 5.
        The number, as a string, otherwise.
    """
    if number % 15 == 0:
        return "fizz buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return str(number)


input("Play Fizz Buzz.   Press ENTER to start")
print("""Rule of the game 
1.You have to guess numbers between 1 to 100.only in increment manner.
2.numbers which are divisible by 3 will need input from you as fizz.
3.if it's divisible by 5 then 'buzz' 
4.if it's divisible by both 3 and 5 then 'fizz buzz' 
5.Each time computer will give its value and also at same time computer number value will increment to next number 
like if 1 2 fizz(3 divisible by 3) 4 etc . you have to choose next number and provide correct answer per above rules
6.if you choose correctly then game move on untill 100 and if not then you lost the game and correct answer displayed
""")
print()

next_number = 0
while next_number < 99:
    next_number += 1
    print('my go is {}'.format(fizz_buzz(next_number)))
    next_number += 1
    correct_answer = fizz_buzz(next_number)
    players_answer = input("Your go: ")
    if players_answer != correct_answer:
        print("You lose, the correct answer was {}".format(correct_answer))
        break
else:
    print("Well done, you reached {}".format(next_number))


