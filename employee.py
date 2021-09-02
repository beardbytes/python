class Employee:
    
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

# Employee.raise_amt = 1.05           
# Employee.set_raise_amount(1.05) # same as above statement

emp_1 = Employee('Test', 'User', '50000')
emp_2 = Employee('Adi', 'M', '60000')

print(Employee.num_of_emps)
# print(Employee.raise_amt)
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)

