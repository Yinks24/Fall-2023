# Solomon Falode 2154980
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