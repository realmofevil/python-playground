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
    """implementation of a basic palindrome function, as a side-effect of the above mirror function,
    shorthand alternative with slicing x[::] == y[::-1]"""
    x = str(x)
    mirrored = ""
    for index, _ in enumerate(x, 1):
        mirrored += x[-index]
    if str(y) == mirrored:
        return True
    return False


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


def is_valid_card(x):
    """implementation of the https://en.wikipedia.org/wiki/Luhn_algorithm for bank card validation,
    tasked by https://cs50.harvard.edu/x/2020/psets/1/credit/"""

    amex = ("34", "37")
    maestro = ("5018", "5020", "5038", "5612", "5893", "6304", "6759", "6761", "6762", "6763", "0604", "6390")
    master = ("51", "52", "53", "54", "55")
    master2017 = (str(_) for _ in range(2221, 2721))
    visa = ("4",)
    visa_e = ("4026", "417500", "4405", "4508", "4844", "4913", "4917")

    reverse = x[::-1]
    # even_digits = ""
    # for i in reverse[1::2]:
    #     multiply = int(i) * 2
    #     even_digits += str(multiply)
    #
    # odd_digits = ""
    # for i in reverse[::2]:
    #     odd_digits += str(i)
    #
    # odd_digits = ""
    # for index, i in enumerate(reverse):
    #     if index % 2 != 0:
    #         odd_digits += str(i)
    every_second_digit = [int(i) * 2 for i in reverse[1::2]]
    every_second_digit = "".join([str(i) for i in every_second_digit])
    odd_digits = [i for i in reverse[::2]]
    odd_digits = "".join([str(i) for i in odd_digits])

    sum_even = 0
    for i in every_second_digit:
        sum_even += int(i)

    sum_odd = 0
    for i in odd_digits:
        sum_odd += int(i)

    checksum = sum_even + sum_odd

    if checksum % 10 == 0 and 11 < len(x) < 20:
        if x[:2] in amex:
            return "AMEX"
        elif x[:4] in maestro:
            return "Maestro"
        elif x[:2] in master or x[:4] in master2017:
            return "MasterCard"
        elif x[:4] in visa_e:
            return "Visa Electron"
        elif x[:1] in visa:
            return "Visa"
        else:
            return "Valid number but issuer not identified"
    else:
        return "INVALID"
