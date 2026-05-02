from db_connection import get_connection

class Employee:
    def add_employee(self, name, department, email):
        conn = get_connection()
        cursor = conn.cursor()

        query = "insert into employees(name, department, email) values (%s, %s, %s)"
        cursor.execute(query, (name, department, email))

        conn.commit()
        print("employee successfully")
        conn.close()

    def view_employees(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("select * from employees")
        for i in cursor.fetchall():
            print(i)
        conn.close()

    def delete_employee(seld, emp_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("delete from employees where emp_id = %s", (emp_id,))
        conn.commit()
        print("Employee deleted")
        conn.close