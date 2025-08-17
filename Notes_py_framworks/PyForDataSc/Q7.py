# Q7. 7. Create a class `Employee` with attributes and a method to display salary after tax.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def net_salary(self):
        return self.salary * 0.8 # Assume 20% tax
emp = Employee("John", 50000)
print(emp.net_salary())

# Jab bhi tum class ke andar koi method likhte ho, uska pehla parameter hamesha current object hota hai → aur usse hi self bolte hain.
# self = current object ka reference, jisse tum class ke andar ke attributes aur methods access kar paate ho.

'''
__init__ ko constructor kehte hain Python me.
Ye automatic call hota hai jab bhi hum class ka object banate hain.
Iska kaam hota hai object ko initialize karna (yaani uske attributes ko value dena).
'''