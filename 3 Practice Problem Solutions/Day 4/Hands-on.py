# ==============================
# STRING MANIPULATION EXAMPLES
# ==============================

text = "Python Programming"

print("Original :", text)
print("Upper    :", text.upper())
print("Lower    :", text.lower())
print("Reverse  :", text[::-1])
print("Replace  :", text.replace("Python", "Java"))
print("Length   :", len(text))


# ==============================
# STUDENT MARKS SYSTEM
# ==============================

students = {
    "Arun": [85, 90, 88],
    "Bala": [78, 82, 80],
    "Charan": [92, 95, 91]
}

for name, marks in students.items():
    total = sum(marks)
    avg = total / len(marks)

    print("\nStudent:", name)
    print("Total :", total)
    print("Average :", round(avg, 2))


# ==============================
# DUPLICATE REMOVAL DEMO
# ==============================

numbers = [10, 20, 10, 30, 20, 40, 50, 40]

unique_numbers = list(set(numbers))

print("\nOriginal List :", numbers)
print("Without Duplicates :", unique_numbers)


# ==============================
# PALINDROME CHECK
# ==============================

word = input("\nEnter a word for palindrome check: ")

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


# ==============================
# COUNT VOWELS
# ==============================

text = input("\nEnter a string: ")

count = 0

for ch in text.lower():
    if ch in "aeiou":
        count += 1

print("Vowel Count:", count)


# ==============================
# FREQUENCY COUNTER
# ==============================

text = input("\nEnter a string for frequency count: ")

freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)


# ==============================
# FIRST REPEATING ELEMENT
# ==============================

numbers = [5, 3, 2, 4, 5, 7, 3]

seen = set()

for num in numbers:
    if num in seen:
        print("First Repeating Element:", num)
        break
    seen.add(num)


# ==============================
# STRING + DICTIONARY CHALLENGE 1
# WORD COUNT
# ==============================

sentence = "python is easy and python is powerful"

words = sentence.split()

word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print("\nWord Count")
print(word_count)


# ==============================
# STRING + DICTIONARY CHALLENGE 2
# CHARACTER OCCURRENCE
# ==============================

text = "programming"

result = {}

for ch in text:
    result[ch] = result.get(ch, 0) + 1

print("\nCharacter Frequency")
print(result)
