# ======================================
# FUNCTIONAL PRACTICE SHEET
# ======================================

numbers = [1, 2, 3, 4, 5]

double_values = list(
    map(lambda x: x * 2, numbers)
)

print("Doubled Values:", double_values)

odd_numbers = list(
    filter(lambda x: x % 2 != 0, numbers)
)

print("Odd Numbers:", odd_numbers)


# ======================================
# EMPLOYEE CLASS
# ======================================

class Employee:

    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

    def display(self):
        print("ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Annual Salary:", self.annual_salary())


employee = Employee(
    101,
    "Kumar",
    50000
)

employee.display()


# ======================================
# SHOPPING CART MODEL
# ======================================

class ShoppingCart:

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def display(self):
        print("Cart Items:")
        for item in self.items:
            print(item)


cart = ShoppingCart()

cart.add_item("Laptop")
cart.add_item("Mouse")
cart.add_item("Keyboard")

cart.display()


# ======================================
# FUNCTIONAL REVISION PROBLEMS
# ======================================

numbers = [5, 10, 15, 20, 25]

cube_values = list(
    map(lambda x: x ** 3, numbers)
)

print("Cube Values:", cube_values)

greater_than_15 = list(
    filter(lambda x: x > 15, numbers)
)

print("Greater Than 15:", greater_than_15)


# ======================================
# CLASS DESIGN EXERCISE
# ======================================

class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print("Title :", self.title)
        print("Author:", self.author)


book = Book(
    "Python Programming",
    "John"
)

book.display()


# ======================================
# COMPLETE PYTHON REVISION
# ======================================

numbers = [10, 20, 30, 40, 50]

print("List:", numbers)

print("Tuple:", tuple(numbers))

print("Set:", set(numbers))

frequency = {}

for number in numbers:
    frequency[number] = frequency.get(number, 0) + 1

print("Dictionary:")
print(frequency)


# ======================================
# EXTRA 1
# PRODUCT PRICE ANALYZER
# ======================================

products = {
    "Laptop": 65000,
    "Mouse": 500,
    "Keyboard": 1500,
    "Monitor": 12000
}

highest_price = max(
    products,
    key=products.get
)

print("Costliest Product:", highest_price)


# ======================================
# EXTRA 2
# STUDENT RESULT ANALYZER
# ======================================

students = {
    "Arun": 85,
    "Bala": 45,
    "Charan": 92,
    "David": 38
}

passed_students = dict(
    filter(
        lambda item: item[1] >= 50,
        students.items()
    )
)

print("Passed Students:")
print(passed_students)


# ======================================
# EXTRA 3
# INVENTORY VALUE CALCULATOR
# ======================================

inventory = {
    "Laptop": (5, 60000),
    "Mouse": (20, 500),
    "Keyboard": (15, 1500)
}

total_value = 0

for quantity, price in inventory.values():
    total_value += quantity * price

print("Total Inventory Value:", total_value)
