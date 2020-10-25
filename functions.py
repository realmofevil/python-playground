import sys


def print_me(x=""):
    """implementation of a basic print function"""
    x = str(x) + "\n"
    return sys.stdout.write(x)


def len_me(x=None):
    """implementation of a basic length function"""
    x = str(x)
    for length, _ in enumerate(x, 1):
        pass
    return length


def reverse_me(x=None):
    """implementation of a basic reverse order function"""
    return x[::-1]
    # # alternative algorithms with while and for loops outside of a function
    # index = len_me(x)-1
    # while index >= 0:
    #     print_me(x[index])
    #     index -= 1
    #
    # for index, _ in enumerate(x, 1):
    #     print_me(x[-index], end="")


def mirror_me(x=None):
    """implementation of a basic mirror sting function, as a side-effect of the above reversed order algorithms"""
    x = str(x)
    mirrored = ""
    for index, _ in enumerate(x, 1):
        mirrored += x[-index]
    return mirrored


def is_palindrome(x, y):
    """implementation of a basic palindrome function, as a side-effect of the above mirror function"""
    x = str(x)
    mirrored = ""
    for index, _ in enumerate(x, 1):
        mirrored += x[-index]
    if str(y) == mirrored:
        return True
    else:
        return False


def fizz_buzz(num):
def fizz_buzz(num=None):
    """implementation of the Fizz Buzz algorithm"""
    fizz = num % 3 == 0
    buzz = num % 5 == 0
    fizzbuzz = num % 15 == 0	# shorthand for num % 3 == 0 and num % 5 == 0
    if fizzbuzz:
        return "FizzBuzz"
    elif fizz:
        return "Fizz"
    elif buzz:
        return "Buzz"
    else:
        return num


# arcane solution of FizzBuzz with slicing, within a list comprehension and unpacking it
# fizzbuzz = ["Fizz"[num%3*4::]+"Buzz"[num%5*4::] or num for num in range(1,101)]
# print_me(*fizzbuzz, sep = "\n")

# create an HTML file, generate sample data, and solve FizzBuzz with CSS selectors
with open("fizzbuzz.html", "a") as the_file:
    the_file.write("<html>\n"
                   "<style>\n"
                   "div {display: table-row;}\n"
                   "div:nth-child(3n+0) {background-color: green;}\n"
                   "div:nth-child(5n+0) {background-color: red;}\n"
                   "div:nth-child(15n+0) {background-color: yellow;}\n"
                   "</style>\n"
                   "<body>\n")
for _ in range(1, 101):
    with open('fizzbuzz.html', "a") as the_file:
        the_file.write("<div>" + str(fizz_buzz(_)) + "</div>\n")
with open("fizzbuzz.html", "a") as the_file:
    the_file.write("</body>\n</html>")
