import mysql.connector
mydb = mysql.connector.connect(
    host="localhost:3306",
    user="yourusername",
    password="yourpassword",
    database="mydatabase"
)


mycursor = mydb.cursor()


mycursor.execute("""
    CREATE TABLE students (
        student_id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(255),
        last_name VARCHAR(255),
        age INT,
        grade FLOAT
    )
""")


sql_insert = """
    INSERT INTO students (first_name, last_name, age, grade)
    VALUES ('Alice', 'Smith', 18, 95.5)
"""
mycursor.execute(sql_insert)
mydb.commit()


sql_update = """
    UPDATE students
    SET grade = 97.0
    WHERE first_name = 'Alice'
"""
mycursor.execute(sql_update)
mydb.commit()

sql_delete = """
    DELETE FROM students
    WHERE last_name = 'Smith'
"""
mycursor.execute(sql_delete)
mydb.commit()
mycursor.execute("SELECT * FROM students")
all_students = mycursor.fetchall()
for student in all_students:
    print(student)
