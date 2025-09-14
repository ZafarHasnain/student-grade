"""
Student Grade Calculator with GPA
---------------------------------
This program:
1. Takes student name and marks for 4 subjects.
2. Calculates total, percentage, grade, and GPA.
3. Prints a neat report card.

Author: Zafar's Assistant :)
"""

# List of subjects
SUBJECTS = ["Math", "English", "Science", "History"]

# Max marks for each subject
MAX_MARKS = 100

# Grade bands with GPA points
GRADE_BANDS = [
    ("A+", 90, 4.0),
    ("A", 85, 3.7),
    ("B+", 80, 3.3),
    ("B", 75, 3.0),
    ("C", 65, 2.5),
    ("D", 50, 2.0),
    ("F", 0, 0.0)
]

def get_grade_and_gpa(percentage):
    """
    Takes a percentage and returns the grade and GPA points.
    """
    for grade, min_percent, gpa in GRADE_BANDS:
        if percentage >= min_percent:
            return grade, gpa
    return "F", 0.0  # fallback

def calculate_report(name, marks):
    """
    Calculates total, percentage, grade, GPA for one student.
    """
    total = sum(marks.values())  # add all subject marks
    percentage = (total / (MAX_MARKS * len(SUBJECTS))) * 100  # percentage
    grade, gpa = get_grade_and_gpa(percentage)

    # GPA is average of all subject grade points
    subject_gpas = []
    for score in marks.values():
        _, gp = get_grade_and_gpa((score / MAX_MARKS) * 100)
        subject_gpas.append(gp)
    avg_gpa = sum(subject_gpas) / len(subject_gpas)

    return {
        "name": name,
        "marks": marks,
        "total": total,
        "percentage": round(percentage, 2),
        "grade": grade,
        "gpa": round(avg_gpa, 2)
    }

def print_report(report):
    """
    Prints a formatted report card for the student.
    """
    print("="*40)
    print(f" Report Card for: {report['name']} ")
    print("="*40)
    for subject, score in report["marks"].items():
        print(f"{subject:<10}: {score:>3} / {MAX_MARKS}")
    print("-"*40)
    print(f"Total       : {report['total']}")
    print(f"Percentage  : {report['percentage']}%")
    print(f"Grade       : {report['grade']}")
    print(f"GPA         : {report['gpa']}")
    print("="*40)

# -------- Main Program --------
# if __name__ == "__main__":
    # Example data (you can replace with input() for dynamic use)
    # student_name = "Ali"
    # student_marks = {
    #     "Math": 92,
    #     "English": 85,
    #     "Science": 78,
    #     "History": 88
    # }

    # Calculate report
    # report = calculate_report(student_name, student_marks)

    # Print report
    # print_report(report)


if __name__ == "__main__":
    # Take student name from user
    student_name = input("Enter student name: ")

    # Take subject marks from user
    student_marks = {}
    for subject in SUBJECTS:
        score = float(input(f"Enter marks for {subject} (0-100): "))
        student_marks[subject] = score

    # Calculate report
    report = calculate_report(student_name, student_marks)

    # Print report
    print_report(report)
