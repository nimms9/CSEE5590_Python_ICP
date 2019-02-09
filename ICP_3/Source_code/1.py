class Employee:
    emp_count=0
    salary=0

    #Default Constructor with arguments name,family,salary,department
    def __init__(self, name, family, salary, dept):
        self.name=name
        self.family=family
        Employee.salary+=salary
        self.dept=dept
        Employee.emp_count+=1

    #Total no of employees
    def display_emp_count(self):
        print("Total number of employees:",Employee.emp_count)

    #Calculate Average Salary of all employees
    def avg_salary(self):
        avg_sal=Employee.salary/Employee.emp_count
        print("Average salary:",avg_sal)

    #Demo function in parent class
    def demo_func(self):
        print('calling Demo member function of parent')
        
class Full_time_employee(Employee):
    #Default constructor in subclass
    def __init__(self):
        print('This is the subclass- Full time employee')

e=Employee('sudheer','Nimmagadda',6000,'CS')
Employee('Ram',"krishna",7000,"EE")
Employee('jyo','chowdary',8000,'EC')
c=Full_time_employee()
c.display_emp_count()  
c.avg_salary()
e.demo_func()
