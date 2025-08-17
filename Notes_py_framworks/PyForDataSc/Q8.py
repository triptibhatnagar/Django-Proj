# Q8. 8. Handle `ZeroDivisionError` and `ValueError` in a calculator program.

try:
    a = float(input("Enter numerator: "))
    b = float(input("Enter denominator: "))
    result = a/b
except ZeroDivisionError:
    print("Error: Division by zero.")
except ValueError:
    print("Error: Invalid input.")
else:
    print("Result: ",result)
finally:
    print("Done!")