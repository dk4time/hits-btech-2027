"""
Topic: Day 1 Hands-On Solutions
Author: Dineshkumar
"""

# Sum Of Two Numbers

num1 = 10
num2 = 20

result = num1 + num2

print(result)


# Swap Two Numbers

a = 10
b = 20

a, b = b, a

print(a)
print(b)


# Largest Of Three Numbers

a = 10
b = 50
c = 30

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)


# Leap Year

year = 2024

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not Leap Year")


# Positive Negative Zero

number = -10

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")