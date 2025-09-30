# Q5. 5. Handle division error safely using try-except.
try:
a = int(input("Enter numerator: "))
b = int(input("Enter denominator: "))
print("Result is:", a / b)
except ZeroDivisionError:
print("Cannot divide by zero.")