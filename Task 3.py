import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789",
)

cursor = connection.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT,
    grade FLOAT
);
"""
cursor.execute(create_table_query)

# Insert new student record
insert_query = """
INSERT INTO students (first_name, last_name, age, grade)
VALUES (%s, %s, %s, %s);
"""
student_data = ("Alice", "Smith", 18, 95.5)
cursor.execute(insert_query, student_data)
connection.commit()

# Update
update_query = """
UPDATE students
SET grade = %s
WHERE first_name = %s;
"""
updated_grade = 97.0
cursor.execute(update_query, (updated_grade, "Alice"))
connection.commit()

# Delete
delete_query = """
DELETE FROM students
WHERE last_name = %s;
"""
cursor.execute(delete_query, ("Smith",))
connection.commit()

# Display all student records
select_query = "SELECT * FROM students;"
cursor.execute(select_query)
students = cursor.fetchall()

print("All Student Records:")
for student in students:
    print(student)

cursor.close()
connection.close()