#define a class
class Employee:
    #define an attribute
    employee_id = 0
    #create two objects of the employee class
employee1 =Employee()
employee2 = Employee()
#access attributes using employee1
employee1.employeeID = 1001
print(f"Employee ID :{employee1.employeeID}")
# access attributes using emplyee2
employee2.employeeID = 1002
print(f"Employee ID : {employee2.employeeID}")