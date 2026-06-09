```python
"""
Topic: Day 3 Hands-On Solutions
Author: Dineshkumar
"""

# List Operations Demo

numbers = [10, 20, 30, 40, 50]

print(numbers)

for number in numbers:
    print(number)

print("First Element:", numbers[0])
print("Last Element:", numbers[-1])
print("Middle Element:", numbers[len(numbers) // 2])

print("First Half:", numbers[:len(numbers)//2])
print("Second Half:", numbers[len(numbers)//2:])

for index in range(len(numbers) - 1, -1, -1):
    print(numbers[index])


# Menu Driven List Program

numbers = [10, 20, 30]

print("Before:", numbers)

numbers.append(40)

numbers.remove(20)

numbers[1] = 50

target = 50

if target in numbers:
    print("Found")
else:
    print("Not Found")

print("After:", numbers)


# Packing And Unpacking

student = ("Dinesh", 25, "Python")

name, age, course = student

print(name)
print(age)
print(course)

a = 10
b = 20

a, b = b, a

print(a)
print(b)


# Maximum Element

numbers = [10, 50, 20, 80, 40]

maximum = numbers[0]

for number in numbers:

    if number > maximum:
        maximum = number

print(maximum)


# Minimum Element

numbers = [10, 50, 20, 80, 40]

minimum = numbers[0]

for number in numbers:

    if number < minimum:
        minimum = number

print(minimum)


# Remove Duplicates

numbers = [1, 2, 2, 3, 1, 4]

result = []

for number in numbers:

    if number not in result:
        result.append(number)

print(result)


# Rotate Array Left

numbers = [1, 2, 3, 4]

first = numbers[0]

for index in range(len(numbers) - 1):
    numbers[index] = numbers[index + 1]

numbers[-1] = first

print(numbers)


# Rotate Array Right

numbers = [1, 2, 3, 4]

last = numbers[-1]

for index in range(len(numbers) - 1, 0, -1):
    numbers[index] = numbers[index - 1]

numbers[0] = last

print(numbers)


# Collection Based Coding Challenges

# Common Elements

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

for value in list1:

    if value in list2:
        print(value)


# Separate Even And Odd Numbers

numbers = [1, 2, 3, 4, 5, 6]

even = []
odd = []

for number in numbers:

    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

print(even)
print(odd)


# Check Sorted List

numbers = [10, 20, 30, 40]

sorted_list = True

for index in range(len(numbers) - 1):

    if numbers[index] > numbers[index + 1]:
        sorted_list = False
        break

print(sorted_list)


# Largest And Second Largest

numbers = [10, 20, 40, 30]

largest = float("-inf")
second_largest = float("-inf")

for number in numbers:

    if number > largest:

        second_largest = largest
        largest = number

    elif number > second_largest and number != largest:

        second_largest = number

print(largest)
print(second_largest)
```
