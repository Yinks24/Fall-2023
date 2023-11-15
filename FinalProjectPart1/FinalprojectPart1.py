# Solomon Falode 2154980
import csv

# Define a Student class to hold student information
class Student:
    def __init__(self, student_id, last_name, first_name, major, gpa, graduation_date, has_disciplinary_action):
        self.student_id = student_id
        self.last_name = last_name
        self.first_name = first_name
        self.major = major
        self.gpa = gpa
        self.graduation_date = graduation_date
        self.has_disciplinary_action = has_disciplinary_action
    
    def __str__(self):
        return f"{self.student_id},{self.major},{self.first_name},{self.last_name},{self.gpa},{self.graduation_date},{self.has_disciplinary_action}"

# Read the input files and create a dictionary of students
students = {}
with open('StudentsMajorsList.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        student_id = row[0]
        last_name = row[1]
        first_name = row[2]
        major = row[3]
        has_disciplinary_action = row[4] if len(row) > 4 else ''
        students[student_id] = Student(student_id, last_name, first_name, major, None, None, has_disciplinary_action)

with open('GPAList.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        student_id = row[0]
        gpa = float(row[1])
        students[student_id].gpa = gpa

with open('GraduationDatesList.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        student_id = row[0]
        graduation_date = row[1]
        students[student_id].graduation_date = graduation_date