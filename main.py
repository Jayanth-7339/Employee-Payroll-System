from employee import Employee
from payroll import Payroll

emp = Employee()
pay = Payroll()

while True:
    print("\n --- Employee Payroll Syatem---")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Delete Employee")
    print("4. Add Salary")
    print("5. Update Salary")
    print("6. Generate Payslip")
    print("7. Add Attendance")
    print("8. Exit")

    choice = int(input("Enter choice: "))
    if choice == 1:
        name = input("Name: ")
        dept = input("Department: ")
        email = input("Email: ")
        emp.add_employee(name, dept, email)
    elif choice == 2:
        emp.view_employees()
    elif choice == 3:
        emp_id = int(input("Employee ID: "))
        emp.dalete_employee(emp_id)
    
    elif choice == 4:
        emp_id = int(input("Employee ID: "))
        salary = float(input("Salary: "))
        pay.add_salary(emp_id, salary)

    elif choice == 5:
        emp_id = int(input("Employee ID: "))
        salary = float(input("New Salary: "))
        pay.update_salary(emp_id, salary)

    elif choice == 6:
        emp_id = int(input("Employee ID: "))
        pay.generate_payslip(emp_id)
    
    elif choice == 7:
        emp_id = int(input("employee ID: "))
        days = int(input("Days Present: "))
        pay.add_attendance(emp_id, days)

    elif choice == 8:
        print("Exited...")
        break
    else:
        print("Invalid choice")