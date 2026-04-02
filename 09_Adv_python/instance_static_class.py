class Employee:
    company = "DELL"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
#instance method in python 
    def print_info(self):

        info = f"the name is {self.name} and the salary is {self.salary}"
        print(info)

    @staticmethod
    def sum(a, b):
     return a+b
    @classmethod
    def print_company(cls):
       print(cls.company)
    @classmethod
    def change_company(cls, new_company):
       cls.company = new_company
          

e1 = Employee("jack",45666) 
e2 = Employee("Jill",54322)
# print(Employee.company)       
# e1.print_info()
# print(e1.sum(2,4))
print(Employee.company)
e1.change_company("acer")
print(Employee.company)