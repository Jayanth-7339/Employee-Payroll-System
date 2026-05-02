from db_connection import get_connection
class Payroll:
    def add_salary(self, emp_id, salary):
        conn = get_connection()
        cursor = conn.cursor()
        query = "insert into salary(emp_id, salary) values(%s,%s)"
        cursor.execute(query, (emp_id,salary))
        conn.commit()
        print("salary added")
        conn.close()

    def update_salary(self,emp_id, salary):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("select * from salary where emp_id = %s", (emp_id,))
        if cursor.fetchone():
            cursor.execute(
                "update salary set salary = %s where emp_id = %s",
                (salary, emp_id)
            )
            conn.commit()
            print("salary is updated")
        else:
            print("salary record is not found")
        conn.close()
    def generate_payslip(self, emp_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            select e.name, s.salary
            from employees e
            join salary s on e.emp_id = s.emp_id
            where e.emp_id = %s
        """, (emp_id,))

        data = cursor.fetchone()

        if data:
            print("\n--PAYSLIP--")
            print(f"Name: {data[0]}")
            print(f"salary: {data[1]}")
        else:
            print("No data found")
        conn.close()
    
    def add_attendance(self,emp_id, days):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "insert into attendance (emp_id, days_present) values (%s, %s)",
            (emp_id, days)
        )
        conn.commit()

        print("attendance added")

        conn.close()