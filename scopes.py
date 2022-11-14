class Student:
    schoolName = 'XYZ School' # class attribute

    def __init__(self, name, age, designation, salary):
        self.name=name # instance attribute
        self.age=age # instance attribute
        self._designation=designation
        self.__salary=salary

    @property    
    def designation(self):
        return self.designation

    @designation.setter
    def designation(self, newDesignation):
        self.__designation=newDesignation


    def __display(self):
        print("This is private method")
        return   0  

    
        


obj = Student('vijay', '31', 'fullStack developer', '7.5LPA')
print("+++Public scope+++")
print(obj.name)
obj.age=30
print(obj.age)

print("+++Public scope+++")
print(obj._designation)
obj._designation="python-reactify"
print(obj._designation)
print("+++++++++Private Object++++++++++")
# We can access private object by object._className.__variable
print(obj._Student__salary)
obj._Student__salary = '8.0LPA'
print(obj._Student__salary)
print(obj._Student__display())


