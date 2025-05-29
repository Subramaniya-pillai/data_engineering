
FUNCTIONS

# 1. Prime Number Checker
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

print("Prime numbers from 1 to 100:")
for i in range(1, 101):
    if is_prime(i):
        print(i, end=' ')
print()


# 2. Temperature Converter
def convert_temp(value, unit):
    if unit.lower() == 'c':
        return (value * 9/5) + 32  # Celsius to Fahrenheit
    elif unit.lower() == 'f':
        return (value - 32) * 5/9  # Fahrenheit to Celsius
    else:
        return "Invalid unit"

print("Convert 100°C to Fahrenheit:", convert_temp(100, 'c'))
print("Convert 212°F to Celsius:", convert_temp(212, 'f'))


# 3. Recursive Factorial Function
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))

CLASSES

# 4. Rectangle
class Rectangle:
    def _init_(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def is_square(self):
        return self.length == self.width


# 5. BankAccount
class BankAccount:
    def _init_(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount

    def get_balance(self):
        return self.balance


# 6. Book
class Book:
    def _init_(self, title, author, price, in_stock):
        self.title = title
        self.author = author
        self.price = price
        self.in_stock = in_stock

    def sell(self, quantity):
        if quantity > self.in_stock:
            raise ValueError("Not enough stock")
        self.in_stock -= quantity


# 7. Student Grade System
class Student:
    def _init_(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def grade(self):
        avg = self.average()
        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 50:
            return "C"
        else:
            return "F"

INHERITANCE

# 8. Person → Employee
class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def _init_(self, name, age, emp_id, salary):
        super()._init_(name, age)
        self.emp_id = emp_id
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, ID: {self.emp_id}, Salary: {self.salary}")


# 9. Vehicle → Car, Bike
class Vehicle:
    def _init_(self, name, wheels):
        self.name = name
        self.wheels = wheels

    def description(self):
        return f"{self.name} has {self.wheels} wheels."

class Car(Vehicle):
    def _init_(self, name, wheels, fuel_type):
        super()._init_(name, wheels)
        self.fuel_type = fuel_type

    def description(self):
        return f"Car {self.name} with {self.wheels} wheels runs on {self.fuel_type}."

class Bike(Vehicle):
    def _init_(self, name, wheels, is_geared):
        super()._init_(name, wheels)
        self.is_geared = is_geared

    def description(self):
        gear_status = "geared" if self.is_geared else "non-geared"
        return f"Bike {self.name} with {self.wheels} wheels is {gear_status}."


# 10. Polymorphism with Animals
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Cow(Animal):
    def speak(self):
        return "Moo!"

animals = [Dog(), Cat(), Cow()]
for animal in animals:
    print(animal.speak())
