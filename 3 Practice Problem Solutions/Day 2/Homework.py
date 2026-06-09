"""
Topic: Day 2 Homework Solutions
Author: Dineshkumar
"""

# Prime Number Check

number = 17

is_prime = True

for i in range(2, number):

    if number % i == 0:
        is_prime = False
        break

print(is_prime)


# Prime Numbers In Range

start = 1
end = 50

for number in range(start, end + 1):

    if number < 2:
        continue

    is_prime = True

    for divisor in range(2, number):

        if number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        print(number)


# Number Utility Functions

def is_even(number):
    return number % 2 == 0


def is_positive(number):
    return number > 0


def square(number):
    return number * number


print(is_even(10))
print(is_positive(-5))
print(square(7))