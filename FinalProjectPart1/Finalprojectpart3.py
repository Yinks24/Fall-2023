# Solomon Falode 2154980
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