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

# Create the FullRoster.csv file
with open('FullRoster.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['Student ID', 'Major', 'First Name', 'Last Name', 'GPA', 'Graduation Date', 'Disciplinary Action'])
    for student in sorted(students.values(), key=lambda s: s.last_name):
        writer.writerow([student.student_id, student.major, student.first_name, student.last_name, student.gpa, student.graduation_date, student.has_disciplinary_action])

# Create the List per major files
for major in set(s.major for s in students.values()):
    major_file_name = f"{major.replace(' ', '')}Students.csv"
    with open(major_file_name, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['Student ID', 'Last Name', 'First Name', 'Graduation Date', 'Disciplinary Action'])
        for student in sorted(filter(lambda s: s.major == major, students.values()), key=lambda s: s.student_id):
            writer.writerow([student.student_id, student.last_name, student.first_name, student.graduation_date, student.has_disciplinary_action])

# Create the ScholarshipCandidates.csv file
eligible_students = sorted([s for s in students.values() if s.gpa is not None and s.gpa > 3.8 and s.graduation_date is None and not s.has_disciplinary_action], key=lambda s: s.gpa, reverse=True)

with open('ScholarshipCandidates.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Student ID', 'Last Name', 'First Name', 'Major', 'GPA'])
    for student in eligible_students:
        writer.writerow([student.student_id, student.last_name, student.first_name, student.major, student.gpa])

# Create the DisciplinedStudents.csv file
disciplined_students = sorted([s for s in students.values() if s.has_disciplinary_action], key=lambda s: s.graduation_date)

with open('DisciplinedStudents.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Student ID', 'Last Name', 'First Name', 'Graduation Date'])
    for student in disciplined_students:
        writer.writerow([student.student_id, student.last_name, student.first_name, student.graduation_date]) 

print('All inventory reports have been processed.')