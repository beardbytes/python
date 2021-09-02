class Employee:
    
    raise_amt = 1.04

    def __init__(self, first, last, pay) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self) -> str:
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
    raise_amt = 1.10
    
    def __init__(self, first, last, pay, prog_lang) -> None:
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang
    
class Manager(Employee):

    def __init__(self, first, last, pay, employees=None) -> None:
        super().__init__(first, last, pay)
        if employees is None:
            self.employess = []
        else:
            self.employess = employees
    
    def add_emp(self, emp):
        if emp not in self.employess:
            self.employess.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employess:
            self.employess.remove(emp)

    def print_emps(self):
        for emp in self.employess:
            print('--->', emp.fullname())

dev_1 = Developer('Test', 'User', 50000, 'Java')
dev_2 = Developer('Adi', 'M', 60000, "Python")

mgr_1 = Manager('Sue', 'Susan', 9000, [dev_1])

#print(isinstance(dev_1, Employee))
# print(issubclass(Manager, Employee))


# print(mgr_1.email)

# mgr_1.add_emp(dev_2)
# mgr_1.remove_emp(dev_1)
# mgr_1.print_emps()

# print(dev_1.email)
# print(dev_1.prog_lang)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)