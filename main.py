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
        self.employee.append(emp)

    def del_emp(self, emp):
        self.employee.remove(emp)

    def all_emp(self):
        print("List Of employees")
        for e in self.employee:
            print(e)            
            
class Company:
    '''Company management'''
    def __init__(self):
        self.departments = {}
        
    def add_dep(self, dep_name):
        self.departments[dep_name] = Department(dep_name)

    def del_dep(self, dep_name):
        if dep_name in self.departments:
            del self.departments[dep_name]
            print(f'Department "{dep_name}" is deleted.')

    def all_dep(self):
        print("List Of Department")
        print(self.departments)
        
def main():
    company = Company()

    while True:
        print("1. Add Employee")     
        print("2. Remove Employee")     
        print("3. Display Department")
        print("4. Add Department")
        print("5. Remove Department")
        print("6. Display Department")
        
        user_input = input("Enter Your Choice: ")
        if user_input == '1':
            Name = input("Enter Employee Name: ")
            ID = input("Enter Employee ID: ")
            Title = input("Enter Employee Title: ")
            department = input("Enter Employee Department: ")
            emp = Employee(Name, ID, Title, department)
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
        else:
            print("Inavalid choice....")

if __name__=="__main__":
    main()