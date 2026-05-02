import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        database="employee_management",
        password="Jayanth@7339"
    )
conn = get_connection()
cur_obj = conn.cursor()

print("db connected successfully...")

cur_obj.execute("""
CREATE TABLE IF NOT EXISTS employees (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    department VARCHAR(50),
    email VARCHAR(100)
)
""")

cur_obj.execute("""
CREATE TABLE if not exists salary (
    emp_id INT,
    salary FLOAT,
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id)
);
""")

cur_obj.execute("""
CREATE TABLE if not exists attendance (
    emp_id INT,
    days_present INT,
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id)
);
""")

print("tables created successfully")