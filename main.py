#importig requried package
import json

class Employee:
    '''Employee class for employee details'''
    def __init__(self, name, id, title, department):
        self.name = name
        self.id = id
        self.title = title
        self.department = department      
        
    def display(self):
        '''showing employee full detail'''
        print(f"Name: {self.name} \nID: {self.id} \nTitle: {self.title} \nDepartment: {self.department}")
    
    def __str__(self):
        '''string method for employee'''
        return f"Name is {self.name} & id is {self.id}"


class Department:
    '''Department Management'''
    def __init__(self, dep_name):
        self.name = dep_name
        self.employee = []
        
    def add_emp(self, emp):
        '''adding employee to list'''
        self.employee.append(emp)

    def del_emp(self, emp):
        '''removing employee from list'''
        self.employee.remove(emp)

    def all_emp(self):
        '''displaying all employee'''
        print("List Of employees")
        for e in self.employee:
            print(e)
            
            
class Company:
    '''Company management'''
    def __init__(self):
        self.departments = {}
        
    def add_dep(self, dep_name):
        '''adding departments'''
        self.departments[dep_name] = Department(dep_name)

    def del_dep(self, dep_name):
        '''deleting departments'''
        if dep_name in self.departments:
            del self.departments[dep_name]
            print(f'Department "{dep_name}" is deleted.')

    def all_dep(self):
        '''displaying all departments'''
        print("List Of Department")
        print(self.departments)
        
def save_data(company):
    '''saving data in file'''
    with open("company_data.json","w", encoding= "utf-8") as file:
        json.dump(company, file, default= lambda obj: obj.__dict__)

def read_data():
    '''Reading file data for reload'''
    try:
        with open("company_data.json", "r", encoding= "utf-8") as file:
            data = json.load(file) #converting to dictionary
            company = Company()
            for department_name, department_data in data["departments"].items():
                department = Department(department_name)  #creating department object
                for employee_data in department_data["employee"]:
                    employee = Employee(**employee_data)  #craeting emaployee
                    department.add_emp(employee)
                company.departments[department_name] = department
            return company
    except FileNotFoundError:
        return Company()
    
def menu():
    '''Creating user friendly menu'''
    print("1. Add Employee")
    print("2. Remove Employee")
    print("3. Display Department")
    print("4. Add Department")
    print("5. Remove Department")
    print("6. Display Department")
    print("7. Exit....!")
    
def main():
    '''Entry point for user and control all functions'''
    company = read_data()
    print(company.all_dep())
    while True:
        menu()
        user_input = input("Enter Your Choice: ")
        if user_input == '1':
            name = input("Enter Employee Name: ")
            id = input("Enter Employee ID: ")
            title = input("Enter Employee Title: ")
            department = input("Enter Employee Department: ")
            emp = Employee(name, id, title, department)
            company.all_dep()
            if department in company.departments:
                company.departments[department].add_emp(emp)
                print("Employee added successfully")
            else:
                print("department does not exits")
        elif user_input == '2':
            dep = input("Enter department:")
            if dep in company.departments:
                company.departments[dep].all_emp()
                id = input("Enter employee ID: ")
                print(company.departments[dep].employee)
                print("Enter in loop")
                for emp in company.departments[dep].employee:
                    print("testing...............")
                    if emp.id == id:
                        company.departments[dep].del_emp(emp)
                        print("Employee successfully deleted......!")
                    else:
                        print("Employee does not exits.....!")
            else:
                print("Department does not exits....!")
        elif user_input == "3":
            dep = input("Enter Department Name: ")
            if dep in company.departments:
                company.departments[dep].all_emp()
            else:
                print("No such department exits..")
        elif user_input == "4":
            dep = input("Enter department name: ")
            company.add_dep(dep)
            print("Department succcessfully added....")
        elif user_input == "5":
            dep = input("Enter Department Name: ")
            if dep in company.departments:
                company.del_dep(dep)
                print("Departent successfully deleted")
            print("Department not exits.....!")
        elif user_input == "6":
            company.all_dep()
        elif user_input == "7":
            save_data(company)
            print("Bye...")
            break
        else:
            print("Inavalid choice....")

if __name__=="__main__":
    main()