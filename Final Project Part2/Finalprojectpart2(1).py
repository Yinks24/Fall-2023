# Solomon Falode 2154980
import csv# Solomon Falode 2154980

class Student:
    def __init__(self, student_id, last_name, first_name, major, gpa, graduation_date, disciplinary_action):
        self.student_id = student_id
        self.last_name = last_name
        self.first_name = first_name
        self.major = major
        self.gpa = gpa
        self.graduation_date = graduation_date
        self.disciplinary_action = disciplinary_action

def read_csv(file_name):
    data = []
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            data.append(row)
    return data

def create_student_instances(majors_data, gpa_data, graduation_data):
    students = []
    for major_row, gpa_row, graduation_row in zip(majors_data, gpa_data, graduation_data):
        student_id, last_name, first_name, major, disciplinary_action = major_row[:5]
        gpa = float(gpa_row[1])
        graduation_date = graduation_row[1]
        student = Student(student_id, last_name, first_name, major, gpa, graduation_date, disciplinary_action)
        students.append(student)
    return students

def get_student_records():
    majors_data = read_csv('StudentsMajorsList.csv')
    gpa_data = read_csv('GPAList.csv')
    graduation_data = read_csv('GraduationDatesList.csv')
    students = create_student_instances(majors_data, gpa_data, graduation_data)
    return students

def interactive_query(students):
    while True:
        query = input("Enter major and GPA (separated by a space), or 'q' to quit: ")
        if query.lower() == 'q':
            break

        query_parts = query.split()
        if len(query_parts) != 2:
            print("No such student")
            continue

        major, requested_gpa = query_parts
        try:
            requested_gpa = float(requested_gpa)
        except ValueError:
            print("No such student")
            continue

        matching_students = []
        closest_match = None
        closest_match_diff = float('inf')

        for student in students:
            if student.major != major:
                continue
            if student.graduation_date or student.disciplinary_action:
                continue

            gpa_diff = abs(student.gpa - requested_gpa)
            if gpa_diff <= 0.1:
                matching_students.append(student)
            elif gpa_diff <= 0.25 and gpa_diff < closest_match_diff:
                closest_match = student
                closest_match_diff = gpa_diff

        if matching_students:
            print("Your student(s):")
            for student in matching_students:
                print(f"ID: {student.student_id}, Name: {student.first_name} {student.last_name}, GPA: {student.gpa}")
        elif closest_match:
            print("You may also consider:")
            print(f"ID: {closest_match.student_id}, Name: {closest_match.first_name} {closest_match.last_name}, GPA: {closest_match.gpa}")
        else:
            print("No such student")

# Main program
students = get_student_records()
interactive_query(students)
