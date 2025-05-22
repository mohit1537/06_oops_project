class Employee:
    def __init__(self,name,salary,ssn):
        self.name = name
        self._salary = salary #protect variable
        self.__ssn = ssn  #private variable 

if __name__ == "__main__":
        emp = Employee("Mohit",23000,"123-456-789")
        #Access public variable
        print("Public Variable:",emp.name)       

        #Access protected variable
        print("Protected variable:",emp._salary)

        #Access private variable
        try:
         print("Private variable:", emp.__ssn)
        except AttributeError:
            print("Cannot access private variable __ssn")