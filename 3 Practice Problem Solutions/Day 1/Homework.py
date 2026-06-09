"""
Topic: Day 1 Homework Solutions
Author: Dineshkumar
"""

# Simple Interest

principal = 10000
rate = 5
time = 2

simple_interest = (principal * rate * time) / 100

print(simple_interest)


# Area Of Circle

radius = 7

area = 3.14 * radius * radius

print(area)


# Digit Extraction

number = 5824

while number > 0:

    digit = number % 10

    print(digit)

    number //= 10


# Reverse Number

number = 12345

reverse = 0

while number > 0:

    digit = number % 10

    reverse = reverse * 10 + digit

    number //= 10

print(reverse)


# Largest Of Three Numbers

a = 10
b = 80
c = 50

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)


# Grade Calculator

marks = 87

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 50:
    print("C")
else:
    print("Fail")


# Electricity Bill

units = 250

if units <= 100:
    bill = units * 2
elif units <= 200:
    bill = (100 * 2) + ((units - 100) * 3)
else:
    bill = (100 * 2) + (100 * 3) + ((units - 200) * 5)

print(bill)


# Number Classification

number = 24

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

if number > 0:
    print("Positive")