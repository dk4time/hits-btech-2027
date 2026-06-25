# ==============================
# REVERSE STRING
# ==============================

text = input("Enter a string: ")

print("Reversed String:", text[::-1])


# ==============================
# WORD FREQUENCY COUNTER
# ==============================

sentence = input("\nEnter a sentence: ")

words = sentence.lower().split()

freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)


# ==============================
# SET OPERATIONS WORKSHEET
# ==============================

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("\nUnion:", A | B)
print("Intersection:", A & B)
print("Difference A-B:", A - B)
print("Difference B-A:", B - A)
print("Symmetric Difference:", A ^ B)


# ==============================
# CHARACTER FREQUENCY
# ==============================

text = input("\nEnter a string: ")

frequency = {}

for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1

print(frequency)


# ==============================
# UNIQUE CHARACTER PROBLEM
# ==============================

text = input("\nEnter a string: ")

unique = True

for ch in text:
    if text.count(ch) > 1:
        unique = False
        break

if unique:
    print("All characters are unique")
else:
    print("Duplicate characters found")


# ==============================
# COLLECTION REVISION SET
# ==============================

numbers = [10, 20, 30, 40, 50, 20, 30]

print("\nList:", numbers)

print("Tuple:", tuple(numbers))

print("Set:", set(numbers))

data = {}

for num in numbers:
    data[num] = numbers.count(num)

print("Dictionary Frequency:")
print(data)


# EXTRA 1
# SECOND MOST FREQUENT CHARACTER
# ==============================

text = input("\nEnter a string: ")

freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

sorted_items = sorted(freq.items(),
                      key=lambda x: x[1],
                      reverse=True)

if len(sorted_items) >= 2:
    print("Second Most Frequent Character:",
          sorted_items[1][0])
else:
    print("Not enough characters")


# ==============================
# EXTRA 2
# REMOVE DUPLICATE CHARACTERS
# ==============================

text = input("\nEnter a string: ")

result = ""

for ch in text:
    if ch not in result:
        result += ch

print("After Removing Duplicates:", result)
