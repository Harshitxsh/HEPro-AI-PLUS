import csv
import random
from pathlib import Path

# Setup paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

# Constants for programs
PROGRAMS = ["B.Tech", "MBA", "B.Sc", "BCA", "M.Tech"]

def generate_student_data(num_students=50):
    students = []
    for i in range(1, num_students + 1):
        # Basic Info
        student_id = f"S{1000 + i:04}"
        age = random.randint(18, 25)
        program = random.choice(PROGRAMS)
        semester = random.randint(1, 8) if "B." in program or "BCA" == program else random.randint(1, 4)
        
        # Behavioral Logic
        # 1. Academic Performance (GPA, Attendance, Assignments)
        # Attendance and Assignments completion generally correlate with GPA
        base_performance = random.uniform(5, 10)
        attendance = min(100, max(0, int(base_performance * 10 + random.uniform(-10, 5))))
        assignments_completion = min(100, max(0, int(base_performance * 10 + random.uniform(-15, 5))))
        
        # GPA is calculated based on attendance, assignments, and some talent/luck
        gpa = round(min(10.0, max(0.0, (attendance / 10 * 0.4) + (assignments_completion / 10 * 0.4) + random.uniform(0.5, 2.0))), 2)
        
        # 2. Wellness (Stress, Sleep, Mental Wellbeing)
        # Higher stress usually correlates with lower sleep and wellbeing
        stress_level = random.randint(1, 10)
        sleep_hours = max(4, min(10, int(10 - (stress_level * 0.5) + random.uniform(-1, 1))))
        mental_wellbeing = max(1, min(10, int(11 - stress_level + random.uniform(-1, 1))))
        
        # 3. Productivity & Engagement
        distractions = random.randint(1, 10)
        # Productivity is lower if distractions are high OR if stress is extremely high
        base_productivity = 11 - distractions
        if stress_level > 8:
            base_productivity -= random.randint(2, 4)
        
        productivity_score = max(1, min(10, int(base_productivity + random.uniform(-1, 1))))
        
        # Engagement score: some students with lower GPA might still be highly engaged
        if gpa < 6.0:
            engagement_score = random.randint(60, 95) # Struggling but motivated
        else:
            engagement_score = min(100, max(0, int(attendance * 0.8 + random.uniform(0, 20))))
            
        # 4. Career Readiness
        # Sometimes high GPA students are directionless
        if gpa > 9.0 and random.random() < 0.3:
            career_clarity = random.randint(1, 4) # Academically strong but directionless
        else:
            career_clarity = random.randint(5, 10) if gpa > 7.0 else random.randint(1, 7)
            
        skill_readiness = max(1, min(10, int((gpa + career_clarity) / 2 + random.uniform(-1, 1))))

        students.append({
            "student_id": student_id,
            "age": age,
            "program": program,
            "semester": semester,
            "gpa": gpa,
            "attendance": attendance,
            "assignments_completion": assignments_completion,
            "stress_level": stress_level,
            "sleep_hours": sleep_hours,
            "mental_wellbeing": mental_wellbeing,
            "productivity_score": productivity_score,
            "distractions": distractions,
            "career_clarity": career_clarity,
            "skill_readiness": skill_readiness,
            "engagement_score": engagement_score
        })
    return students

def save_to_csv(data, filename):
    keys = data[0].keys()
    with open(filename, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)

if __name__ == "__main__":
    data = generate_student_data(50)
    output_path = DATA_DIR / "students.csv"
    save_to_csv(data, output_path)
    print(f"Dataset generated successfully: {output_path}")
