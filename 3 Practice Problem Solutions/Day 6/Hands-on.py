# ======================================
# FUNCTIONAL PROGRAMMING - MAP
# ======================================

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x * x, numbers))

print("Squares:", squares)


# ======================================
# FUNCTIONAL PROGRAMMING - FILTER
# ======================================

numbers = [10, 15, 20, 25, 30]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Even Numbers:", even_numbers)


# ======================================
# FUNCTIONAL PROGRAMMING - SORT
# ======================================

students = [
    ("Arun", 85),
    ("Bala", 92),
    ("Charan", 78)
]

sorted_students = sorted(
    students,
    key=lambda student: student[1],
    reverse=True
)

print("Sorted Students:")
print(sorted_students)


# ======================================
# STUDENT CLASS EXAMPLE
# ======================================

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Average:", round(self.average(), 2))


s1 = Student("Arun", [85, 90, 88])

s1.display()


# ======================================
# BANK ACCOUNT SYSTEM
# ======================================

class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient Balance")

    def display(self):
        print(self.name, "Balance:", self.balance)


account = BankAccount("Dinesh", 10000)

account.deposit(2000)
account.withdraw(1500)

account.display()


# ======================================
# LAMBDA PROBLEMS
# ======================================

add = lambda a, b: a + b

maximum = lambda a, b: a if a > b else b

print("Addition:", add(10, 20))
print("Maximum:", maximum(50, 30))


# ======================================
# STUDENT MANAGEMENT SYSTEM
# ======================================

students = []

students.append({"id": 101, "name": "Arun", "mark": 85})
students.append({"id": 102, "name": "Bala", "mark": 91})
students.append({"id": 103, "name": "Charan", "mark": 78})

for student in students:
    print(student)


# ======================================
# EMPLOYEE MANAGEMENT SYSTEM
# ======================================

employees = [
    {"id": 1, "name": "Raj", "salary": 50000},
    {"id": 2, "name": "Kumar", "salary": 65000},
    {"id": 3, "name": "Priya", "salary": 45000}
]

highest_salary = max(
    employees,
    key=lambda employee: employee["salary"]
)

print("Highest Salary Employee:")
print(highest_salary)


# ======================================
# MINI INVENTORY SYSTEM
# ======================================

inventory = {
    "Laptop": 10,
    "Mouse": 25,
    "Keyboard": 15
}

inventory["Mouse"] += 5
inventory["Laptop"] -= 2

print("Inventory Details")

for item, quantity in inventory.items():
    print(item, quantity)


# ======================================
# STUDENT MARKS ANALYZER
# ======================================

marks = [85, 92, 78, 95, 88, 70]

print("Highest:", max(marks))
print("Lowest :", min(marks))
print("Average:", sum(marks) / len(marks))

above_80 = list(
    filter(lambda mark: mark > 80, marks)
)

print("Above 80:", above_80)
