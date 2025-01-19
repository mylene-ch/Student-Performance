import json
import os


NUM_STUDENTS = 1000
SUBJECTS = ["math", "science", "history", "english", "geography"]


def load_report_card(directory, student_number):
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(directory, f"{student_number}.json")
    path = os.path.join(base_path, file_path)

    try:
        with open(path, "r") as file:
            report_card = json.load(file)
    except FileNotFoundError:
        return {}

    return report_card

# my code is the following part


def load_report_cards(directory, num_students):
    report_cards = []
    for student_number in range(num_students):
        report_card = load_report_card(directory, student_number)
        report_cards.append(report_card)
    return report_cards


def add_student_average(report_cards, subjects):
    for report_card in report_cards:
        sum_marks = 0
        num_sub = 0
        for key, value in report_card.items():
            if key not in subjects:
                continue
            sum_marks += value
            num_sub += 1
        average = sum_marks / len(subjects)
        report_card["average"] = average


def get_student_average(report_cards):
    sum_average = 0
    for report_card in report_cards:
        sum_average += report_card["average"]
    return sum_average / len(report_cards)
# finished for Average student mark


def get_subject_average(report_cards, subjects):
    subject_averages = {"math": 0, "science": 0,
                        "history": 0, "english": 0, "geography": 0}
    for report_card in report_cards:
        for suject in subjects:
            subject_averages[suject] += report_card[suject]

    for subject in subjects:
        subject_averages[subject] = int(
            subject_averages[subject] / len(report_cards))

    return subject_averages


def get_grade_average(report_cards):
    grade_averages = {grade: [] for grade in range(1, 9)}
    for report_card in report_cards:
        grade = report_card["grade"]
        average = report_card["average"]
        grade_averages[grade].append(average)

    for grade in grade_averages:
        grade_averages[grade] = [sum(
            grade_averages[grade]) / len(grade_averages[grade])]
    return grade_averages


report_cards = load_report_cards("students", NUM_STUDENTS)
add_student_average(report_cards, SUBJECTS)

average_student_mark = get_student_average(report_cards)
# print(round(average_student_mark, 2))

subject_averages = get_subject_average(report_cards, SUBJECTS)
# print(subject_averages)
sorted_subject_averages = sorted(subject_averages.items(), key=lambda x: x[1])
# print(sorted_subject_averages)
hardest_suject = sorted_subject_averages[0][0]
easiest_subject = sorted_subject_averages[-1][0]
# print(hardest_suject)
# print(easiest_subject)

grade_averages = get_grade_average(report_cards)
# print(grade_averages)
sorted_grade_averages = sorted(
    grade_averages.items(), key=lambda x: x[1])
# print(sorted_grade_averages)
best_performing_grade = sorted_grade_averages[-1][0]
worst_performing_grade = sorted_grade_averages[0][0]
# print(best_performing_grade)
# print(worst_performing_grade)

sorted_student_average = sorted(report_cards, key=lambda x: x["average"])
# print(sorted_student_average)
best_student_ID = sorted_student_average[-1]["id"]
worst_student_ID = sorted_student_average[0]["id"]
# print(best_student_ID)
# print(worst_student_ID)

print("Average Student Grade:", round(average_student_mark, 2))
print("Hardest Subject:", hardest_suject)
print("Easiest Subject:", easiest_subject)
print("Best Performing Grade:", best_performing_grade)
print("Worst Performing Grade:", worst_performing_grade)
print("Best Student ID:", best_student_ID)
print("Worst Student ID:", worst_student_ID)
