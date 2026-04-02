class Employee1:
    company = "APPLE"
    
    def __init__(self, salary, name, bond):
        self.salary = salary
        self.name = name
        self.bond = bond 
        

    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"the name of Employee is {self.name}.The salary of employee {self.salary}.the bond of employee is for {self.bond} years {self.company}")
    
e1 = Employee1(34000,"Ronit Kolhe", 4 )
print(e1.get_salary())
print(e1.company)
e1.get_info()