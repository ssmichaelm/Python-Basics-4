import string
import random

# Michael Moreland - Smoothstack, Python basics 4; 11/11/2021

# 1.Create a function func() which prints a text ‘Hello World’
print("\nPart 1")

def helloWorld():
    print("Hello World")

helloWorld()

# 2.Create a function func1(name) which takes a value name and prints the output “Hi My name is Google’
print("\nPart 2")

def func1(name):
    print(f"Hi! My name is {name}")

func1(input("What's your name? "))

# 3.Define a function func3(x,y,z) that takes three arguments x,y,z. When z is true it will return x and when z is false it should return y.
# func3(‘hello’,'goodbye’,false)
print("\nPart 3")

def func3(x, y, z):
    if z:
        return x
    else:
        return y

print(f"{func3('hello','goodbye',True)}")
print(f"{func3('hello','goodbye',False)}")

# 4.Define a function func4(x,y) which returns the product of both the values.
print("\nPart 4")

def func4(x, y):
    return x*y

# While input invalid
while True:
    try:
        x, y = [ int(i) for i in input("Enter two factors to be multiplied: ").split() ] # List comprehension
    except:
        print("Please enter two numbers with space between them.")
        continue
    else:
        print(f"{x} * {y} = {func4(x,y)}")
        break # Break when input finally valid

# 5.Define a function called as is_even that takes one argument, which returns true when even values is passed and false if it is not.
print("\nPart 5")

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

# While input invalid
while True:
    try:
        x = int(input("Check if a number is even or odd: "))
    except:
        print("Please enter an integer")
        continue
    else:
        if is_even(x):
            print("Even")
        else:
            print("Odd")
        break # Break

# 6.Define a function that takes two arguments
# Returns true if the first value is greater than the second value and returns false if it is less than or equal to the second.
print("\nPart 6")

def isGreater(x, y):
    if x > y:
        return True
    else:
        return False

# While input invalid
while True:
    try:
        x, y = [ int(i) for i in input("Enter two values to see which is greater: ").split() ]
    except:
        print("Please enter two numbers with space between them.")
        continue
    else:
        if isGreater(x, y):
            print(f"{x} is > {y}")
        else:
            print(f"{y} is >= {x}")
        break

# 7.Define a function which takes arbitrary number of arguments and returns the sum of the arguments.
print("\nPart 7")

def getSum(*args):
    return sum(args)

while True:
    try:
        numList = [ int(i) for i in input("Enter a list of numbers to get sum of: ").split() ]
    except:
        print("Please enter a list of numbers, with space between each, for all values")
        continue
    else:
        print(f"Sum: {getSum(*numList)}") # Unpack the list in the argument parameter, since *args is used in the function
        break

# 8.Define a function which takes arbitrary number of arguments and returns a list containing only the arguments that are even.
print("\nPart 8")

def onlyEven(*args):
    return list(filter(lambda n: n % 2 == 0, args)) # Returns a list with only even values

while True:
    try:
        numList = [ int(i) for i in input("Enter a list of values to retrieve evens: ").split() ]
    except:
        print("Enter a list of numbers with space between each")
        continue
    else:
        print(f"All evens in the list: {onlyEven(*numList)}")
        break

# 9.Define a function that takes a string and returns a matching string where every even letter is uppercase and every odd letter is lowercase 
print("\nPart 9")

def mutateString(user_str):
    operations = (str.lower, str.upper) # Tuple used to alternate between either lowercase or uppercase 
    return ''.join(operations[i%2](x) for i, x in enumerate(user_str)) # If string index is even, make it lowercase; else, uppercase

print(mutateString(input("Enter a string to mutate: ")))

# 10.Write a function which gives lesser than two given numbers if both the numbers are even, but returns a number greater if one or both or odd.
print("\nPart 10")

def numComparison(x, y):
    if x % 2 == 0 and y % 2 == 0:
        return random.randint(min(x,y)-10, min(x, y)-1) # If both are even, output value smaller than both numbers
    else:
        return random.randint(max(x,y)+1, max(x,y)+10) # If at least one is odd, output value greater than both

while True:
    try:
        x, y = [ int(i) for i in input("Enter two numbers: \nIf both are even, then a number smaller than both will be output\nIf at least one is odd, then a number greater than both will be output\n").split() ]
    except:
        print("Please enter two numbers with a space between each")
        continue
    else:
        print(f"{numComparison(x, y)}")
        break

# 11.Write a function which takes two strings and returns true if both the strings start with the same letter.
print("\nPart 11")

def ifSameFirstLetter(x, y):
    if x[0] == y[0]:
        return True
    else:
        return False

x, y = [ i for i in input("Enter two strings: ").split() ]
if ifSameFirstLetter(x, y):
    print("Both strings start with the same letter.")
else:
    print("Strings begin with different letters.")


# 12.Given a value,return a value which is twice as far as other side of 7
# SKIPPED
print("\nPart 12: Told to skip in lecture")

# 13.A function that capitalizes first and fourth character of a word in a string.
print("\nPart 13")

def capitalizeCharacters(user_str):
    result = ""
    for idx, char in enumerate(user_str):
        if idx == 0 or idx == 3: # If the first or fourth character, make it uppercase
            result += char[0].upper()
        else:
            result += char[0]
    return result

print(capitalizeCharacters(input("Enter a string to capitalize first and fourth characters: ")))




