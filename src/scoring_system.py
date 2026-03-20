import csv
from pathlib import Path

# Setup paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

def calculate_scores(students):
    """
    Calculates five independent scores (APS, WWS, PTMS, CRS, SRI) using base Python.
    """
    for student in students:
        # Convert numeric fields
        gpa = float(student['gpa'])
        attendance = float(student['attendance'])
        assignments = float(student['assignments_completion'])
        stress = float(student['stress_level'])
        sleep = float(student['sleep_hours'])
        wellbeing = float(student['mental_wellbeing'])
        productivity = float(student['productivity_score'])
        distractions = float(student['distractions'])
        clarity = float(student['career_clarity'])
        readiness = float(student['skill_readiness'])
        engagement = float(student['engagement_score'])

        # 1. Academic Performance Score (APS)
        # Weights: GPA (40%), Attendance (30%), Assignments (30%)
        # gpa is 0-10 -> 0-100
        aps = (gpa * 10 * 0.4) + (attendance * 0.3) + (assignments * 0.3)
        student['APS'] = round(aps, 2)

        # 2. Wellness Score (WWS)
        # Weights: Stress (Negative, 40%), Wellbeing (40%), Sleep (20%)
        # stress (1-10) -> (11-stress)*10
        wws = ((11 - stress) * 10 * 0.4) + (wellbeing * 10 * 0.4) + (sleep * 10 * 0.2)
        student['WWS'] = round(min(100, max(0, wws)), 2)

        # 3. Productivity Score (PTMS)
        # Weights: Productivity (60%), Distractions (Negative, 40%)
        ptms = (productivity * 10 * 0.6) + ((11 - distractions) * 10 * 0.4)
        student['PTMS'] = round(min(100, max(0, ptms)), 2)

        # 4. Career Readiness Score (CRS)
        # Weights: Clarity (40%), Readiness (40%), Engagement (20%)
        crs = (clarity * 10 * 0.4) + (readiness * 10 * 0.4) + (engagement * 0.2)
        student['CRS'] = round(min(100, max(0, crs)), 2)

        # 5. Student Readiness Index (SRI)
        # Weights: APS (40%), WWS (25%), PTMS (20%), CRS (15%)
        sri = (aps * 0.4) + (wws * 0.25) + (ptms * 0.2) + (crs * 0.15)
        student['SRI'] = round(sri, 2)

        # Classification
        if sri >= 80:
            student['category'] = 'Green'
        elif sri >= 60:
            student['category'] = 'Blue'
        elif sri >= 40:
            student['category'] = 'Yellow'
        else:
            student['category'] = 'Red'

    return students

if __name__ == "__main__":
    input_file = DATA_DIR / 'students.csv'
    output_file = DATA_DIR / 'students_scored.csv'

    try:
        with open(input_file, mode='r') as f:
            reader = csv.DictReader(f)
            students = list(reader)

        scored_students = calculate_scores(students)

        if scored_students:
            keys = scored_students[0].keys()
            with open(output_file, mode='w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=keys)
                writer.writeheader()
                writer.writerows(scored_students)
            print(f"Scoring completed. Saved to {output_file}")
            
            # Print sample validation (first 3 students)
            print("\n--- Validation Walkthrough (Sample) ---")
            for i in range(min(3, len(scored_students))):
                s = scored_students[i]
                print(f"Student: {s['student_id']} | GPA: {s['gpa']} | SRI: {s['SRI']} | Category: {s['category']}")

    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
