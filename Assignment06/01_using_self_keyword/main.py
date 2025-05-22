#Assignment:
#Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor.
#Add a method display() that prints stude

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name of Student is: {self.name}")
        print(f"The Marks of Student is: {self.marks}")

student1 = Student("mohit",34)
student1.display()

