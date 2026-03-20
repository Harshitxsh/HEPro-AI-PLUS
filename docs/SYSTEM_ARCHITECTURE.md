# HEPro AI+ System Architecture

## Technical Framework and Data Pipeline

This document describes the design of the **Mentor Matching & Intervention Engine**, the final intelligence layer of the HEPro AI+ platform. it converts student analytics (scores and clusters) into operational mentoring actions.

---

## 1. Data Flow Overview

The system operates as a sequential pipeline:

1. **Input Consumption**: Reads `Data/students_clustered.csv` and `Data/mentors.csv`.
2. **Needs Assessment**: Analyzes scores (APS, WWS, PTMS, CRS) and ML Cluster labels to identify the primary "Pain Point."
3. **Mentor Selection**: Identifies available mentors with matching expertise and calculates capacity.
4. **Alert Generation**: Flags critical risks (Low SRI or Red Category) for immediate intervention.
5. **Output Generation**: Produces `4_Outputs/final_recommendations.csv` and `4_Outputs/alert_log.txt`.

## 2. Matching Logic (Decision Intelligence)

The engine follows a tiered rule-based logic to ensure explainability:

* **Tier 1: Crisis (Wellness)**: If `stress_level > 7` or `WWS < 40`, the student is prioritized for **Wellness** mentoring (Stress Counseling).
* **Tier 2: Direction (Career)**: If the ML cluster is "Career-Confused" or `CRS < 40`, a **Career** specialist is assigned.
* **Tier 3: Capability (Academic)**: If `APS < 50`, an **Academic** mentor is assigned for tutoring.
* **Tier 4: Efficiency (Productivity)**: If `PTMS < 50`, a **Productivity** coach is assigned.
* **Tier 5: Growth (High Performer)**: Students with `SRI > 80` are assigned to **Leadership & Growth** tracks.

### Capacity & Load Balancing

* Every mentor has a `max_students` limit.
* The system checks `current_load` before assignment.
* If multiple mentors are available, the one with the **lowest current load** is chosen to ensure a balanced workload.

## 3. Risk & Alert Mechanism

The internal alert system triggers an **Immediate Priority** flag if:

* **SRI < 40**: The overall readiness is critical.
* **Category = "Red"**: The rule-based engine flagged a severe risk.
* **Extreme Stress**: Self-reported stress levels are at the burnout limit.

## 4. Scalability Considerations

* **Modular Design**: The `get_student_needs` and `match_mentor` functions are decoupled, allowing new rules or mentor types to be added easily.
* **Capacity Aware**: Prevents mentor burnout by strictly respecting load limits.
* **Unified Analytics**: Combines rule-based math (SRI) with behavioral patterns (ML Clusters) to provide a 360-degree view.

---
**Author:** Harshit Sharma  
**Date:** February 2026
