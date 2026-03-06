# 1. Create a class Student with attributes name and marks. 
# Add a method is_passed() that returns True if the marks are greater than 40, otherwise False. 
# Create two instances of the Student class and check if they have passed or failed.

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def is_passed(self):
        if self.marks>40:
            return True
s1=Student("Geetha",37)
s2=Student("Jyothi",90)
if s1.is_passed():
    print(s1.name,"has passed")
else:
    print(s1.name,"has failed")
if s2.is_passed():
    print(s2.name,"has passed")
else:
    print(s2.name,"has failed")

# 2. Create a class Employee with attributes name and company_name = "TechCorp".
# Add a class method change_company(cls, new_name) to update the company name for all employees.
# Demonstrate how this change affects all instances.

class Employee:
    company_name="TechCorp"
    def __init__(self,name):
        self.name=name
    @classmethod
    def change_company(cls,new_name):
        cls.company_name=new_name
e1=Employee("Geetha")
e2=Employee("ammu")
Employee.change_company("Cvcorp")
print(e1.name,"works at",e1.company_name)
print(e2.name,"works at",e2.company_name)

# 3. Create a class MathOps with a static method is_even(num) that returns True if the number is even.
# Then call it both from the class and an instance.

class MathOps:
    @staticmethod
    def is_even(num):
        if num%2==0:
            return True
print(MathOps.is_even(24))
obj=MathOps()
print(obj.is_even(12))

# 4. Create a class Car with:
# •	instance attribute mileage
# •	class attribute wheels = 4
# Add an instance method display_specs() that prints mileage and wheels.
# Then change wheels using a class method, and print again.

class Car:
    wheels=4
    def __init__(self,mileage):
        self.mileage=mileage
    @classmethod
    def change_wheels(self):
        Car.wheels=6
    def display_specs(self):
        print("mileage:",self.mileage)
        print("wheels:",Car.wheels)
Car1=Car(8)
Car1.change_wheels()
Car1.display_specs()

# 5. Create a class Temperature with:
# •	instance attribute celsius
# •	a static method to_fahrenheit(celsius)
# •	an instance method show_conversion() that uses the static method to print both values.

class Temperature:
    def __init__(self,celsius):
        self.celsius=celsius
    @staticmethod
    def to_fahrenheit(celsius):
        return (celsius*9/5)+32
    def show_conversion(self):
        fahrenheit = Temperature.to_fahrenheit(self.celsius)
        print("celsius",self.celsius)
        print("fahrenheit",fahrenheit)
t1=Temperature(25)
t1.show_conversion()

# 6. Create a class Book with:
# •	instance attributes title, author
# •	a class variable total_books
# •	a class method from_string(cls, book_str) that creates an object from "title-author" format
# •	a static method is_valid_title(title) that checks if title has at least 3 characters
# •	increment total_books for every book created
# Demonstrate:
# •	Creating books using both the constructor and the class method
# •	Validating titles before creation


class book:
    total_books=0
    def __init__(self,title,author):
        self.title=title
        self.author=author
        book.total_books+=1
    @classmethod
    def from_string(cls,book_str):
        t,a=book_str.split("-")
        return cls(t,a)
    @staticmethod
    def validate(title):
        if len(title)<3:
            return False
        return True
b1=book.from_string("python-john")
b2=book("Ai","Sam")
print(b1.validate(b2.title))

# 7. Create a class Employee with:
# •	instance attributes: name, base_salary
# •	class variable: bonus_rate = 0.1
# •	instance method: final_salary() → base_salary + (base_salary × bonus_rate)
# •	class method: update_bonus(cls, new_rate) → updates bonus for all employees
# •	static method: is_valid_salary(sal) → checks if salary > 0
# Create two employees, show final salaries, update bonus rate, and show again.

class Employee:
    bonus_rate=0.1
    def __init__(self,name,base_salary):
        self.name=name
        self.base_salary=base_salary
    def final_salary(self):
        return self.base_salary+(self.base_salary*Employee.bonus_rate)
    @classmethod
    def update_bonus(cls,new_rate):
        cls.bonus_rate=new_rate
    @staticmethod
    def is_valid_salary(sal):
        return sal>0
e1=Employee("Geetha",5000)
e2=Employee("pavani",4000)
Employee.update_bonus(0.2)
print(e1.name, e1.final_salary())
print(e2.name, e1.final_salary())

# 8. Create a class Course with:
# •	class variable total_students
# •	instance variable student_name
# •	instance method enroll() → increments total_students
# •	class method show_total(cls) → prints total students
# •	static method is_eligible(age) → returns True if age ≥ 18
# Demonstrate enrolling multiple students and show total count.

class course:
    total_student=0
    def __init__(self,student_name):
        self.student_name=student_name
    def enroll(self):
        course.total_student+=1
    @classmethod
    def show_total(cls):
        print("total_student:",cls.total_student)
    @staticmethod
    def is_eligible(age):
        return age>=18
s1=course("pavani")
s2=course("mounika")
s1.enroll()
s2.enroll()
course.show_total()
print("Is age 20 eligibele?",course.is_eligible(20))
print("Is age 16 eligibele?",course.is_eligible(16))

# 9. Create a class BankAccount with:
# •	class variable bank_name
# •	instance variables holder and balance
# •	instance method deposit(amount)
# •	class method change_bank_name(cls, new_name)
# •	static method validate_amount(amount) → returns True if amount > 0
# Show transactions and how static + class methods work together.

class bankaccount:
    bank_name="mahindra"
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    @classmethod
    def change_bank_name(cls,new_name):
        cls.bank_name=new_name
    def deposit(self,amount):
        self.balance=amount
    @staticmethod
    def validate_amount(amount):
        if amount>0:
            return True
b1=bankaccount("Geetha",50000)
b2=bankaccount("pavani",balance=70000)
b1.deposit(100000)
b2.deposit(30000000)
bankaccount.change_bank_name("sbi")
print("bank name",bankaccount.bank_name)

# 10. Create a class Student with:
# •	class variable passing_marks = 40
# •	instance attributes name, marks
# •	instance method result() → prints pass/fail using class variable
# •	class method update_passing_marks(cls, new_marks)
# •	static method grade_category(marks) → returns "A", "B", "C" based on score ranges
# Use all three in a program that:
# 1.	Creates students
# 2.	Updates the passing criteria
# 3.	Displays grade category and result

class student:
    passing_marks=40
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    @classmethod
    def update_passing_marks(cls,new_marks):
        cls.new_marks=new_marks

    def result(self):
        if self.marks>=student.passing_marks:
            print(self.name,"pass")
        else:
            print(self.name, "fail")
    @staticmethod
    def grade_category(marks):
        if marks>=75:
            return "A"
        elif marks>=50:
            return "B"
        else:
            return "C"

s1=student("ammu",56)
s2=student("janu",39)
student.update_passing_marks(40)
print(s1.name,"Grade",student.grade_category(s1.marks))
print(s2.name,"Grade",student.grade_category(s2.marks))
