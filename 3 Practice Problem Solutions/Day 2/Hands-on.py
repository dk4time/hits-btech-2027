"""
Topic: Day 2 Hands-On Solutions
Author: Dineshkumar
"""

# Multiplication Table

number = 7

for i in range(1, 11):
    print(number, "x", i, "=", number * i)


# Inverted Triangle Pattern

rows = 5

for i in range(rows, 0, -1):
    print("*" * i)


# Calculator Using Functions

def calculate(a, b, operation):

    if operation == "+":
        return a + b

    if operation == "-":
        return a - b

    if operation == "*":
        return a * b

    if operation == "/":
        return a / b


print(calculate(10, 20, "+"))


# Factorial

def factorial(number):

    result = 1

    for i in range(1, number + 1):
        result *= i

    return result


print(factorial(5))


# Sum Of Digits

number = 5824

total = 0

while number > 0:

    total += number % 10

    number //= 10

print(total)


# Armstrong Number

number = 153

temp = number

total = 0

while temp > 0:

    digit = temp % 10

    total += digit ** 3

    temp //= 10

print(total == number)


# Reverse Number Using Function

def reverse_number(number):

    reverse = 0

    while number > 0:

        digit = number % 10

        reverse = reverse * 10 + digit

        number //= 10

    return reverse


print(reverse_number(12345))