class Person:
    """  Parent Class """
    def __init__(self, first_name, last_name):
        self.firstname = first_name
        self.lastname = last_name

    def display(self):
        print(self.firstname, self.lastname)


class Student(Person):
    """  Child Class """
    def __init__(self, first_name, last_name, roll_no, percentage):
        Person.__init__(self, first_name, last_name)
        self.roll_no = roll_no
        self.percentage = percentage

    def display(self):
        Person.display(self)
        print(self.roll_no, self.percentage)


x = Student("John", "Doe", '12', '80%')
x.display()
