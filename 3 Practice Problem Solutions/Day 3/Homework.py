```python
"""
Topic: Day 3 Homework Solutions
Author: Dineshkumar
"""

# Sum Of List Elements

numbers = [10, 20, 30, 40]

total = 0

for number in numbers:
    total += number

print(total)


# Second Largest Element

numbers = [10, 20, 40, 30]

largest = float("-inf")
second_largest = float("-inf")

for number in numbers:

    if number > largest:

        second_largest = largest
        largest = number

    elif number > second_largest and number != largest:

        second_largest = number

print(second_largest)


# Tuple Practice Set

numbers = (10, 20, 30, 20, 40)

print("Length:", len(numbers))

print("Count Of 20:", numbers.count(20))

print("Maximum:", max(numbers))

print("Minimum:", min(numbers))

list_numbers = [1, 2, 3, 4]

tuple_numbers = tuple(list_numbers)

print(tuple_numbers)


# Search Element

numbers = [10, 20, 30, 40]

target = 30

found = False

for number in numbers:

    if number == target:

        found = True
        break

if found:
    print("Found")
else:
    print("Not Found")


# Frequency Count Using List

numbers = [1, 2, 2, 3, 1, 1]

visited = []

for number in numbers:

    if number in visited:
        continue

    count = 0

    for value in numbers:

        if value == number:
            count += 1

    print(number, "->", count)

    visited.append(number)


# Collection Worksheet

# Problem 1 - Maximum Element
# Refer: Day 3 Hands-On Solutions

# Problem 2 - Minimum Element
# Refer: Day 3 Hands-On Solutions

# Problem 3 - Second Largest Element
# Refer: Above Solution

# Problem 4 - Search Element
# Refer: Above Solution

# Problem 5 - Remove Duplicates
# Refer: Day 3 Hands-On Solutions

# Problem 6 - Rotate Array Left
# Refer: Day 3 Hands-On Solutions

# Problem 7 - Rotate Array Right
# Refer: Day 3 Hands-On Solutions

# Problem 8 - Frequency Count
# Refer: Above Solution

# Problem 9 - Find Common Elements

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

for value in list1:

    if value in list2:
        print(value)

# Problem 10 - Check If List Is Sorted

numbers = [10, 20, 30, 40]

sorted_list = True

for index in range(len(numbers) - 1):

    if numbers[index] > numbers[index + 1]:

        sorted_list = False
        break

print(sorted_list)
```
