# Unit 1 – Python Basics & Libraries (30 Questions)

# One-Word / Objective (5 Questions)
# 1. Keyword used to define a function in Python.
# def
# 2. Output of len("Python").
# 6
# 3. Default file extension for Python scripts.
# .py
# 4. Which library is used for numerical computing in Python?
# numpy
# 5. Which function is used to take user input from the keyboard?
# input()

# Short Answer (5 Questions)
# 6. Write a Python program to print even numbers from 1 to 20.
# for loop with range
# for i in range(2, 21, 2):
#     print(i, end=" ")
# print()

# for loop with if condition
# for i in range(1, 21):
#     if(i%2 == 0):
#         print(i, end=" ")
# print()

# while loop
# i = 2
# while(i <= 20):
#     print(i, end=" ")
#     i = i+2
# print()

# Using while loop with if condition
# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print(i, end=" ")
#     i += 1
# print()

# # 7. Write a function is_palindrome() to check if a number is palindrome.
# def is_palindrome(n):
#     orig_n = str(n)
#     rev_n = orig_n[::-1]
#     return orig_n == rev_n
# print(is_palindrome(211))
# print(is_palindrome(212))

# def is_palindrome(n):
#     rev = ""
#     n = str(n)
#     for char in n:
#         rev = char + rev # prepend, not append
#     return(rev == n)
# print(is_palindrome(7))

# def is_palindrome(n):
#     n = str(n)
#     i = 0
#     j = len(n)-1
#     while(i <= j):
#         if(n[i] != n[j]):
#             return False
#         i = i+1
#         j = j-1
#     return True
# print(is_palindrome(211))
# print(is_palindrome(212))

# def is_palindrome(n):
#     num_str = str(n)
#     length = len(num_str)
    
#     for i in range(length // 2):
#         if num_str[i] != num_str[length - 1 - i]:
#             return False
#     return True
# print(is_palindrome(211))
# print(is_palindrome(212))


# 8. Write code to reverse a string 'Python'.
# def reverseStr(s):
#     return s[::-1]
# print(reverseStr("tripti"))

# 9. Write a Python program using list comprehension to generate squares of numbers 1–10.
# A list comprehension lets you generate a list by writing what you want in the list, all in one line. The general syntax is:
# [expression for item in iterable if condition]
# print([x**2 for x in range(1,11)])

# 10. Write a program to handle ZeroDivisionError using try-except.
# try:
#     a = 10
#     b = 0
#     div = a/b
#     print(div)
# except ZeroDivisionError:
    # print("cannot div by zero")

# Long Coding (20 Questions)


# 11. Write a Python program to count vowels in a user-input string.
# cnt = 0
# str = input("Enter a string: ")
# vowels = "aeiouAEIOU"
# for i in str:
#     if i in vowels:
#         cnt = cnt+1
# print(cnt)


# 12. Write a program to generate Fibonacci series up to 10 terms.
# a = 0
# b = 1
# n = 10
# for i in range(0, n):
#     print(a, end=" ")
#     temp = a+b
#     a = b
#     b = temp


# 13. Write a program to read and write data into a text file.
# with open("file1.txt", 'w') as f:
#     f.write("content")
# with open("file1.txt", 'r') as f:
#     print(f.read())


# 14. Write a program to implement bubble sort in Python.
# arr = [3,9,2,0,1]
# n = len(arr)
# for i in range(0, n):
#     for j in range(0, n-i-1):
#         if(arr[j] > arr[j+1]):
#             arr[j], arr[j+1] = arr[j+1], arr[j]
# print(arr)


# 15. Write a Python script to count frequency of each word in a paragraph.
# para = "Python is easy. Python is powerful. Python is easy and powerful."
# words = para.lower().split()
# freq = {}
# # key = word, value = count
# for word in words:
#     word = word.strip('.')
#     freq[word] = freq.get(word, 0)+1
# print(freq)


# 16. Write a Python program to store student names and marks in a dictionary and display those who scored above 75.
# records = {}
# students = ["a", "b", "c", "d"]
# marks = [67, 89, 45, 90]
# records = dict(zip(students, marks))
# print(records)

# for student, mark in records.items():
#     if(mark > 75):
#         print(student, mark)


# 17. Implement a Python class Student with attributes name and roll number, and a method to display details.
# class Student:
#     def __init__(self, name, rollNo):
#         self.name = name
#         self.rollNo = rollNo
#     def display(self):
#         print(self.name)
#         print(self.rollNo)
# s1 = Student("raj", 78)
# s1.display()


# 18. Write a program to demonstrate the use of inheritance in Python.
# class Vehicle:
#     def __init__(self, color):
#         self.color = color
#     def tellColor(self):
#         print(self.color)

# class Car(Vehicle):
#     def __init__(self, color, wheels):
#         super().__init__(color)
#         self.wheels = wheels
#     def noOfWheels(self):
#         print(self.wheels)

# c1 = Car("red", 4)
# c1.tellColor()
# c1.noOfWheels()


# 19. Write Python code to implement binary search algorithm.
# arr = [6, 9, 12, 76, 90]
# target = 76
# def binarySearch(arr, target):
#     low = 0
#     high = len(arr)-1
#     while(low <= high):
#         mid = low+(high-low)//2
#         if(arr[mid] == target):
#             return mid
#         if(arr[mid] < target):
#             low = mid+1
#         else:
#             high = mid-1
#     return -1

# print(binarySearch(arr, target))


# 20. Write a program to demonstrate lambda, map, filter, and reduce.
# map() applies a function to every item in an iterable and returns a new iterable with the results.
# filter() applies a function to each item and returns only those items for which the function returns True.
# reduce() (from functools) applies a function cumulatively to the items, reducing the iterable to a single value.
# from functools import reduce
# add = lambda x: x ** 2
# print(add(4))

# nums = [1,3,2,7,6]
# print(list(map(lambda x: x*10, nums)))
# print(list(filter(lambda x: x%2 == 0, nums)))
# print(reduce(lambda x,y: x+y, nums))


# 21. Write a program to generate a multiplication table of a given number.
# num = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(f"{num}*{i} = {num*i}")


# 22. Write a Python script to sort a dictionary by keys and by values.
# d = {'b': 2, 'a': 3, 'c': 1}
# # Sort by keys
# print(dict(sorted(d.items())))
# # Sort by values
# print(dict(sorted(d.items(), key=lambda x: x[1])))


# 23. Write a program to demonstrate command-line arguments using sys.argv.
# import sys
# sys.argv[0] -> file/script name
# sys.argv[1:] -> arguments
# print("Script name:", sys.argv[0])
# print("Arguments passed:", sys.argv[1:])


# 24. Write a program to find factorial using recursion.
# def fact_rec(n):
#     if(n <= 1):
#         return 1
#     return n*fact_rec(n-1)

# print(fact_rec(5))


# 25. Write a Python script to display a bar chart of student marks using matplotlib.
# import matplotlib.pyplot as plt

# students = ['A', 'B', 'C', 'D', 'E']
# marks = [85, 90, 78, 92, 88]

# plt.bar(students, marks)
# plt.xlabel("Students")
# plt.ylabel("Marks")
# plt.title("Student Marks")
# plt.show()


# 26. Write a program to perform element-wise multiplication using NumPy arrays.
# import numpy as np

# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# result = a * b
# print("Element-wise multiplication:", result)

# 27. Write a program to plot a pie chart using matplotlib.
# import matplotlib.pyplot as plt

# activities = ['Study', 'Sports', 'Sleep', 'Entertainment']
# hours = [6, 2, 8, 4]

# plt.pie(hours, labels=activities, autopct='%1.1f%%', startangle=90)
# plt.title("Daily Activities")
# plt.show()


# 28. Write a Python script to read a CSV file using pandas and display the first 5 rows.
import pandas as pd

data = pd.read_csv("students.csv")   # CSV file path
print(data.head())  # first 5 rows


# 29. Create a simple calculator with add, subtract, multiply, and divide functions.
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Error! Division by zero."

print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Multiplication:", multiply(10, 5))
print("Division:", divide(10, 5))


# 30. Write a program to demonstrate usage of nested loops to print a pyramid pattern.
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))

rows = 5
for i in range(1, rows + 1):
    # Print spaces
    for j in range(rows - i):
        print(" ", end="")
    # Print stars
    for k in range(2 * i - 1):
        print("*", end="")
    print()
