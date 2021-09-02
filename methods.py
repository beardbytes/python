import datetime

class Employee:

    def __init__(self, first, last, pay) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str): # methods starting with 'from' are constructors
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # Static methods don't take self and cls as first arguments
    @staticmethod
    def is_worday(day) -> bool:
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_str_1 = 'John-Doe-40000'

new_emp = Employee.from_string(emp_str_1)
print(new_emp.email)
print(new_emp.pay)

# static methods
my_date = datetime.date(2021, 6, 24)
print(Employee.is_worday(my_date))