class Employee:

    # class variables
    company_name = 'NASA'

    # constructor to initialize the object
    def __init__(self, name, salary):
        # instance variables
        self.name = name
        self.salary = salary

    # __str__ method
    def __str__(self):
        """vs .show()"""
        return f"Employee: {self.name}, {self.salary}, working @ {self.company_name}"

    # instance method
    def show(self):
        """vs __str__"""
        print('Employee:', self.name, self.salary, "working @", self.company_name)

    # class method
    @classmethod
    def modify_company_name(cls, newName):
        # modify class variable
        cls.company_name = newName    
    
    # TODO: static method
    def staticmethod():
        pass
    
if __name__ == "__main__":

    # create first object
    emp1 = Employee("Harry", 12000)
    print(emp1)
    emp1.show()
    
    # create second object
    emp2 = Employee("Emma", 10000)
    print(emp2)
    emp2.show() 
       
    emp2.company_name = "SPACEX"
    print(emp1)
    print(emp2)
    
    Employee.modify_company_name("Roscosmos")
    print(emp1)
    print(emp2)
    emp3 = Employee("Vasili", 10000)    
    print(emp3)    