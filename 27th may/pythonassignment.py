def digit_sum_calculator():
    number = input("Enter a number: ")
    
    # Validate input
    if not number.isdigit():
        print("Invalid input! Please enter a positive integer.")
        return

    digit_sum = sum(int(digit) for digit in number)
    
    # Creating the formatted string for display
    formatted_digits = " + ".join(number)
    print(f"{number} → {formatted_digits} = {digit_sum}")

# Run the calculator
digit_sum_calculator()

num = input("Enter a 3-digit number: ")

if num.isdigit() and len(num) == 3:
    reversed_num = num[::-1]
    print("Reversed number:", reversed_num)
else:
    print("Please enter a valid 3-digit number.")


meters = float(input("Enter value in meters: "))

centimeters = meters * 100
feet = meters * 3.28084
inches = meters * 39.3701

print(f"\n{meters} meters is equal to:")
print(f"{centimeters} centimeters")
print(f"{feet:.2f} feet")
print(f"{inches:.2f} inches")

# Input marks for 5 subjects
marks = []
for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

# Calculations
total = sum(marks)
average = total / 5
percentage = (total / 500) * 100

# Grade based on percentage
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

# Display results
print("\n--- Result ---")
print(f"Total Marks: {total}")
print(f"Average Marks: {average}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")

year = int(input("Enter a year: "))

# Check leap year condition
if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

# Perform operation
if operator == '+':
    result = num1 + num2
    print("Result:", result)
elif operator == '-':
    result = num1 - num2
    print("Result:", result)
elif operator == '*':
    result = num1 * num2
    print("Result:", result)
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator!")

a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

# Triangle Inequality Theorem check
if a + b > c and a + c > b and b + c > a:
    print("The sides can form a valid triangle.")
else:
    print("The sides cannot form a valid triangle.")

bill = float(input("Enter total bill amount: ₹"))
people = int(input("Enter number of people: "))
tip_percent = float(input("Enter tip percentage: "))

# Calculate tip and total
tip_amount = bill * (tip_percent / 100)
total_with_tip = bill + tip_amount
amount_per_person = total_with_tip / people

# Output
print(f"\nTip amount: ₹{tip_amount:.2f}")
print(f"Total bill with tip: ₹{total_with_tip:.2f}")
print(f"Amount per person: ₹{amount_per_person:.2f}")

print("Prime numbers between 1 and 100:")

for num in range(2, 101):  # Start from 2 (1 is not prime)
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")

text = input("Enter a string: ")

# Normalize the string (optional: remove spaces and make lowercase)
cleaned_text = text.replace(" ", "").lower()

# Check if palindrome
if cleaned_text == cleaned_text[::-1]:
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")

n = int(input("Enter the number of terms: "))

a, b = 0, 1
print("Fibonacci series:")

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

num = int(input("Enter a number: "))

print(f"\nMultiplication Table of {num}:")

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

import random

# Generate random number between 1 and 100
secret_number = random.randint(1, 100)

print("🎯 Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Too Low! Try again.")
    elif guess > secret_number:
        print("Too High! Try again.")
    else:
        print(f"🎉 Correct! The number was {secret_number}.")
        break

balance = 10000  # Initial balance

print("🏦 Welcome to the ATM Machine")

while True:
    print("\n--- Menu ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        amount = float(input("Enter amount to deposit: ₹"))
        if amount > 0:
            balance += amount
            print(f"✅ ₹{amount} deposited. New balance: ₹{balance}")
        else:
            print("❌ Invalid amount.")

    elif choice == '2':
        amount = float(input("Enter amount to withdraw: ₹"))
        if amount <= balance and amount > 0:
            balance -= amount
            print(f"✅ ₹{amount} withdrawn. Remaining balance: ₹{balance}")
        else:
            print("❌ Insufficient balance or invalid amount.")

    elif choice == '3':
        print(f"💰 Current balance: ₹{balance}")

    elif choice == '4':
        print("👋 Thank you for using the ATM. Goodbye!")
        break

    else:
        print("❌ Invalid choice. Please select from 1 to 4.")

import string

password = input("Enter your password: ")

# Flags
has_upper = any(char.isupper() for char in password)
has_digit = any(char.isdigit() for char in password)
has_symbol = any(char in string.punctuation for char in password)
is_long_enough = len(password) >= 8

# Check all conditions
if is_long_enough and has_upper and has_digit and has_symbol:
    print("✅ Strong password!")
else:
    print("❌ Weak password. Make sure it:")
    if not is_long_enough:
        print("- Has at least 8 characters")
    if not has_upper:
        print("- Contains at least one uppercase letter")
    if not has_digit:
        print("- Contains at least one number")
    if not has_symbol:
        print("- Contains at least one symbol (e.g., !@#$)")

# Input two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Euclidean algorithm
while b != 0:
    a, b = b, a % b

print(f"✅ GCD is: {a}")