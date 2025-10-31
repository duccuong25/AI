class EmployeeIn4:
    def __init__ (self, name= None, id=None):
        self.name = name
        self.id = id
    def inputIn4(self):
        self.name = input(" Enter name: ")
        self.id = int(input("Enter id: "))
    def showIn4(self):
        print(f"Name:{self.name} - ID: {self.id}")
employee= EmployeeIn4()
employee.inputIn4()
employee.showIn4()