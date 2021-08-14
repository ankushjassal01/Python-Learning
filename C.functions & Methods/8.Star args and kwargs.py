# star args and kwargs
# these called as VAR-POSITIONAL PARAMETERS.
# it is required when we need to pass multiple arguments and we are not defining the keyword argumets in functions
# it unpack the arguments and pass it to function
# this *arg is always shows as tuple so aware of the for loop. it will work only like tuple length ..
# if string pass then it inclosed in tuple so it will pass as 1 parameter to for loop and it wont print each letters
# instead it print the whole string as its coming from tuple value
# *args always gives output in form of tuples
# it minimize the error of keyword and position params as they need to call as written in order
# def students_info(*args, **kwargs)  ## Kwargs means keyword arguments
# these packed the arguments in tuple and dict # important point ref: line 36
# like below math art will be in tuple and name and class will be in dict but those not passed as tuple or dict
# student_info('Math','Art',name='John',class='12th')
# here math and art is *args and name and class are **kwargs
# *args gives o/p as tuple and **kwargs gives as dict
# these * and ** methodology can work with simple variables too like
# important below
# but it have rule we cannot pass other then dict to **kwargs as it not mapped correctly
# but we can pass any sequence to *args if dict then it will pass the keys only .. like dict unpacking

# normal *variable unpacking below
# print(*info) it works like that too but answer will be not in any tuple as its unpack it
# it works as unpack sequence or dictionary ref:check line 42

#  this is accept the arbitrary or keyword arguments
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


# with variables inside the functions for args and kwargs
# in these *args function python also packs the unpacked values to tuple and pass them as tuple
# like below math and art are unpacked arguments it packed in *args and give us values
# student_info('Math', 'Art', name='John', class_name='12th')

courses = ['math', 'art']
info = {'name': 'John', 'class': ('12th', 3), 'age': (1, 2)}
class_totals = {'1st': 33, '2nd': 43}

# its unpack the values
# if dict passed as *arg then keys in tuples and values will not print but the empty dict will be there.
student_info(**info)
student_info(*courses, *info, *class_totals)  # multiple *args works too
# **args will result in dict but empty tuple will be there.
student_info(*courses, *class_totals, *info, **info, **class_totals)  # multiple **kwargs also works and multiple *args
print(*class_totals)
student_info()  # with no arguments  # it give () and {} in return but no error like tradition func


# %% with return
# it give issue as when return pass function stop so only *args will be returned , no matter if you pass **kwargs
# it wont return **kwargs value instead it return empty tuple
def student_info(*args, **kwargs):
    return args
    return kwargs


# student_info('Math','Art',name='John',class_name='12th')

# its unpack the values
# print('return function start here')
# print(student_info())  # ()
# print(student_info(*info))  # ('name', 'class', 'age')
# print(student_info(**info))  # ()




# numbers = (0, 1, 2, 3, 4, 5)
# print(numbers, sep=";")
# print(*numbers, sep=";")
# print(0, 1, 2, 3, 4, 5, sep=";")


# def test_star(*args):
#     print(args)
#     for x in args:
#         print(x)
#
#
# test_star([1,2,3])
# print()
