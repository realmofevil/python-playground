import sys


def print_me(x):
    """implementation of a basic print function"""
    x = str(x) + "\n"
    return sys.stdout.write(x)


def len_me(x):
    """implementation of a basic length function"""
    length = 0
    for _ in x:
        length += 1
    return length


def reverse_me(x):
    """implementation of a basic reverse order function"""
    return x[::-1]
    # # alternative algorithms with while and for loops outside of a function
    # index = len_me(x)-1
    # while index >= 0:
    #     print_me(x[index])
    #     index -= 1
    #
    # index = len_me(x)-1
    # for _ in x:
    #     print_me(x[index])
    #     index -= 1


def fizz_buzz(num):
    """implementation of the Fizz Buzz algorithm"""
    fizz = num % 3 == 0
    buzz = num % 5 == 0
    fizzbuzz = num % 15 == 0  # shorthand for num % 3 == 0 and num % 5 == 0
    if fizzbuzz:
        return "FizzBuzz"
    elif fizz:
        return "Fizz"
    elif buzz:
        return "Buzz"
    else:
        return num


# for _ in range(1,101):
#     print_me(fizz_buzz(_))


# create an HTML file and do the FizzBuzz with CSS selectors
with open("fizzbuzz.html", "a") as the_file:
    the_file.write("<style>\n" \
                   "div {display: table-row;}\n" \
                   "div:nth-child(3n+0) {background-color: green;}\n" \
                   "div:nth-child(5n+0) {background-color: red;}\n" \
                   "div:nth-child(15n+0) {background-color: yellow;}\n" \
                   "</style>\n" \
                   "<html><body>\n")
for _ in range(1, 101):
    with open('fizzbuzz.html', "a") as the_file:
        the_file.write("<div>" + str(fizz_buzz(_)) + "</div>\n")
with open("fizzbuzz.html", "a") as the_file:
    the_file.write("</body></html>")
