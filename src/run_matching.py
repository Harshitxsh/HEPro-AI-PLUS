import pandas as pd
import numpy as np
import os
from pathlib import Path

# Setup paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "outputs"

# Create directories if they don't exist
DATA_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

def get_student_needs(row):
    # Mapping based on identifying the student's weakest areas
    # Order of priority: Wellness > Academics > Career > Productivity
    
    # 1. Critical Wellness Intervention (Stress > 7 or WWS < 40)
    if row['stress_level'] > 7 or row['WWS'] < 40:
        return 'Wellness', 'Stress Counseling', 'High' if row['SRI'] < 60 else 'Medium'
    
    # 2. Career Intervention (Based on Cluster or low CRS)
    if 'Career-Confused' in str(row['cluster_label']) or row['CRS'] < 40:
        return 'Career', 'Career Coaching', 'Medium'
        
    # 3. Academic Intervention (Low APS)
    if row['APS'] < 50:
        return 'Academic', 'Academic Tutoring', 'High'
        
    # 4. Productivity Intervention (Low PTMS)
    if row['PTMS'] < 50:
        return 'Productivity', 'Productivity Coaching', 'Medium'
    
    # 5. Growth Opportunity (High SRI)
    if row['SRI'] >= 80:
        return 'Productivity', 'Leadership & Growth', 'Low'
        
    # Default: Minimum score area matches the mentor type
    scores = {
        'Academic': row['APS'],
        'Wellness': row['WWS'],
        'Productivity': row['PTMS'],
        'Career': row['CRS']
    }
    min_area = min(scores, key=scores.get)
    interventions = {
        'Academic': 'Academic Review',
        'Wellness': 'Wellness Check-in',
        'Productivity': 'Efficiency Coaching',
        'Career': 'Goal Setting'
    }
    return min_area, interventions[min_area], 'Low'

def match_mentor(need_area, mentors_df, student_category):
    # Filter mentors matching expertise and available capacity
    candidates = mentors_df[
        (mentors_df['expertise_area'] == need_area) & 
        (mentors_df['current_load'] < mentors_df['max_students'])
    ]
    
    if candidates.empty:
        # Fallback to any mentor with capacity
        candidates = mentors_df[mentors_df['current_load'] < mentors_df['max_students']]
    
    if candidates.empty:
        return "TBD (Waitlist)"
        
    # Prefer Senior mentors for critical risk students
    if student_category in ['Red', 'High-Risk']:
        seniors = candidates[candidates['experience_level'] == 'Senior']
        if not seniors.empty:
            candidates = seniors
            
    # Load balancing: assign to mentor with lowest current load
    best_mentor = candidates.sort_values(by='current_load').iloc[0]
    return best_mentor['mentor_id']

def run_matching_engine():
    # Load datasets
    students_path = DATA_DIR / 'students_clustered.csv'
    mentors_path = DATA_DIR / 'mentors.csv'
    
    students = pd.read_csv(students_path)
    mentors = pd.read_csv(mentors_path)
    
    results = []
    log_entries = []
    
    for _, student in students.iterrows():
        # Determine primary mentoring need
        mentor_type, intervention, priority = get_student_needs(student)
        
        # Assign available mentor
        mentor_id = match_mentor(mentor_type, mentors, student['category'])
        
        # Update mentor's assigned load record
        if mentor_id != "TBD (Waitlist)":
            mentors.loc[mentors['mentor_id'] == mentor_id, 'current_load'] += 1
            
        # Alert logical conditions
        alert_flag = False
        alert_reason = ""
        if student['SRI'] < 40 or student['category'] == 'Red':
            alert_flag = True
            alert_reason = f"SRI ({student['SRI']}) below threshold / Red Category"
        elif student['stress_level'] > 8:
            alert_flag = True
            alert_reason = f"Extreme Stress ({student['stress_level']}) Detected"
            
        if alert_flag:
            priority = 'Immediate'
            log_entries.append(f"ALERT: Student {student['student_id']} – High Risk\nReason: {alert_reason}\nAssigned Mentor: {mentor_id}\nPriority: Immediate\n" + "-"*30)
            
        results.append({
            'student_id': student['student_id'],
            'cluster': student['cluster_label'],
            'SRI': student['SRI'],
            'category': student['category'],
            'assigned_mentor_id': mentor_id,
            'mentor_type': mentor_type,
            'intervention_type': intervention,
            'priority': priority,
            'alert_flag': alert_flag
        })
        
    # Generate Outputs
    recommendations_df = pd.DataFrame(results)
    
    output_recommendations = OUTPUT_DIR / 'final_recommendations.csv'
    output_mentors = DATA_DIR / 'mentors_assigned.csv'
    
    recommendations_df.to_csv(output_recommendations, index=False)
    mentors.to_csv(output_mentors, index=False)
    
    # Save Alert Log
    output_log = OUTPUT_DIR / 'alert_log.txt'
    with open(output_log, 'w') as f:
        f.write("HEPro AI+ HIGH-RISK ALERT LOG\n")
        f.write("="*30 + "\n")
        for entry in log_entries:
            f.write(entry + "\n")
            
    print(f"Successfully generated final_recommendations.csv")
    print(f"Successfully generated alert_log.txt with {len(log_entries)} alerts.")

if __name__ == "__main__":
    run_matching_engine()
