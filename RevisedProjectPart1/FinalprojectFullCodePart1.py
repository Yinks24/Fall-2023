import csv

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

# Function to read CSV files
def read_csv(file_path):
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            return list(reader)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return []

# Read the input files and create a dictionary of students
students = {}

# Update the file reading section
students_majors_data = read_csv('StudentsMajorsList.csv')
gpa_data = read_csv('GPAList.csv')
graduation_dates_data = read_csv('GraduationDatesList.csv')

for row in students_majors_data:
    student_id = row[0]
    last_name = row[1]
    first_name = row[2]
    major = row[3]
    has_disciplinary_action = row[4] if len(row) > 4 else ''
    students[student_id] = Student(student_id, last_name, first_name, major, None, None, has_disciplinary_action)

for row in gpa_data:
    student_id = row[0]
    gpa = float(row[1])
    students[student_id].gpa = gpa

for row in graduation_dates_data:
    student_id = row[0]
    graduation_date = row[1]
    students[student_id].graduation_date = graduation_date

# Create the ScholarshipCandidates.csv file with GPA > 3.8 and no disciplinary action
scholarship_candidates = [s for s in students.values() if s.gpa is not None and s.gpa > 3.8 and  s.has_disciplinary_action.lower() != 'y']

# Print information about scholarship candidates for debugging
print("Scholarship Candidates:")
for student in scholarship_candidates:
    print(f"Student ID: {student.student_id}, GPA: {student.gpa}, Graduation Date: {student.graduation_date}, Disciplinary Action: {student.has_disciplinary_action}")

# Write the scholarship candidates to the existing ScholarshipCandidates.csv file
with open('ScholarshipCandidates.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Student ID', 'Last Name', 'First Name', 'Major', 'GPA'])
    for student in scholarship_candidates:
        writer.writerow([student.student_id, student.last_name, student.first_name, student.major, student.gpa])

# Print a message indicating that ScholarshipCandidates.csv has been processed
print('ScholarshipCandidates.csv has been processed.')
