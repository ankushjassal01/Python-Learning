def add(a,b):
    return a+b


def subtraction(a,b):
    return a-b


def divide(a,b):
    return a/b


def multiplication(a,b):
    return a*b


def python_food():
    width = 80
    text = "Spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


def centre_text(*args, sep=' ', end='\n', file=None, flush=False):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text, end=end, file=file, flush=flush)


# call the function
centre_text("spam and eggs")
centre_text("spam, spam and eggs")
centre_text(12)
centre_text("spam, spam, spam and spam")

print("first", "second", 3, 4, "spam")

