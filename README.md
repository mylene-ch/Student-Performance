# Student Performance Analysis Tool

## Introduction

This project is a Python-based tool designed to analyze the performance of students in a school. The program processes report cards stored in JSON files, calculates key metrics, and outputs insights such as the average student mark, hardest and easiest subjects, and the best and worst-performing grades and students. This tool is intended for use by school staff to gain a deeper understanding of student performance.

---

## Features

- **Data Loading:**
  - Reads student report cards from 1,000 JSON files.
  - Each JSON file contains data about a student's grades in five subjects and their grade level.

- **Performance Metrics:**
  - **Average Student Mark:** Calculates the average mark across all students.
  - **Hardest Subject:** Identifies the subject with the lowest average grade.
  - **Easiest Subject:** Identifies the subject with the highest average grade.
  - **Best Performing Grade:** Finds the grade level with the highest average marks.
  - **Worst Performing Grade:** Finds the grade level with the lowest average marks.
  - **Best Student ID:** Identifies the student with the highest average.
  - **Worst Student ID:** Identifies the student with the lowest average.

---

## How It Works

1. **Loading Data:**
   - The program loads all 1,000 student report cards from the `students` folder.
   - Each report card contains a unique student ID, grade level, and marks in five subjects: math, science, history, English, and geography.

2. **Calculations:**
   - Calculates individual student averages by averaging marks across all subjects.
   - Computes the overall average student mark by averaging all student averages.
   - Determines subject averages and identifies the hardest and easiest subjects.
   - Groups students by grade level to calculate grade-wise averages.
   - Identifies the best and worst-performing students and grades.

3. **Output:**
   - Outputs the calculated metrics, including:
     - Average Student Mark.
     - Hardest Subject.
     - Easiest Subject.
     - Best Performing Grade.
     - Worst Performing Grade.
     - Best Student ID.
     - Worst Student ID.

---

## Expected Output

```
Average Student Grade: 50.44
Hardest Subject: geography
Easiest Subject: english
Best Performing Grade: 6
Worst Performing Grade: 5
Best Student ID: 549
Worst Student ID: 637
```

---

## Code Structure

- **`main.py`**:
  - Core script that implements all functionality, including data loading, calculations, and output.

- **Data Files:**
  - JSON files in the `students` folder, each representing a student's report card.

- **Functions:**
  - `load_report_cards`: Loads all student report cards into memory.
  - `add_student_average`: Calculates the average marks for each student.
  - `get_student_average`: Computes the overall average student mark.
  - `get_subject_average`: Calculates averages for each subject and identifies the hardest and easiest subjects.
  - `get_grade_average`: Calculates grade-wise averages to identify the best and worst-performing grades.

---

## Requirements

- Python 3.x
- JSON module (built-in)
- Ensure that the `students` folder with 1,000 JSON files is in the same directory as the script.

---

## Usage

1. Clone or download the project.
2. Ensure the `students` folder is correctly placed.
3. Run the `main.py` script using Python:

   ```bash
   python main.py
   ```

4. View the output in the terminal.

---

## Future Improvements

- Add support for additional metrics, such as standard deviation or median marks.
- Enhance performance for handling larger datasets.
- Include a graphical user interface (GUI) for better usability.
- Allow filtering and exporting of analyzed data.

