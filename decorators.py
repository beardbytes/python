class Employee:

    def __init__(self, first, last) -> None:
        self.first = first
        self.last = last

    # the methods can be used as attributes using property decorator
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first = None
        self.last = None

emp_1 = Employee('Test', 'User')

emp_1.fullname = 'Jim Smith' # to apply the full name, fullname setter is defined to reflect the changes

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname