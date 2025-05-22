class Employee:
    def __init__(self,name):
        self.name = name

class Department:
    def __init__(self,employee):
        self.employee = employee

if __name__ == "__main__":
    
    emp = Employee("Mohit")
    dept = Department(emp)
    print(dept.employee.name)