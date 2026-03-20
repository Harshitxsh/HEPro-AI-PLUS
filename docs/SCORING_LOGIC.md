# Task 2: Student Scoring System (HEPro AI+)

This document explains how I've calculated the scores to help mentors understand the student records student.csv. Every score is out of 100.

---

## 1. How the Scores Work

### 📊 Academic Performance Score (APS)

**Formula:** `(GPA * 10 * 0.4) + (Attendance * 0.3) + (Assignments * 0.3)`
I've used GPA as the main factor (40%), with attendance and assignments making up the rest. This shows if a student is consistent with their classes and homework.

### 🧘 Wellness & Wellbeing Score (WWS)

**Formula:** `((11 - Stress) * 10 * 0.4) + (Wellbeing * 10 * 0.4) + (Sleep * 10 * 0.2)`
This score drops if stress is high. It rewards students who are getting enough sleep and feeling mentally stable.

### ⚡ Productivity & Time Management Score (PTMS)

**Formula:** `(Productivity * 10 * 0.6) + ((11 - Distractions) * 10 * 0.4)`
Higher productivity helps the score, while heavy distractions pull it down.

### 🎯 Career Readiness Score (CRS)

**Formula:** `(Clarity * 10 * 0.4) + (Readiness * 10 * 0.4) + (Engagement * 0.2)`
This combines how clear they are about their path, their skill level, and how much they actually use the platform.

---

## 2. Student Readiness Index (SRI)

This is the final score used to rank students. I gave more weight to academics and wellness because those are the biggest success factors.

* **Academics (APS):** 40%
* **Wellness (WWS):** 25%
* **Productivity (PTMS):** 20%
* **Career (CRS):** 15%

---

## 3. Student Categories (Intervention Levels)

I've grouped students into four simple categories based on their final SRI score:

| Category | Range | What it means |
| :--- | :--- | :--- |
| 🟢 **Green** | 80+ | Doing great. No immediate help needed. |
| 🔵 **Blue** | 60 - 79 | Doing okay, but can improve some skills. |
| 🟡 **Yellow** | 40 - 59 | At-risk. Needs to be monitored closely. |
| 🔴 **Red** | Below 40 | High-risk. Needs urgent mentoring. |

### Why I chose these levels

* **80+ (Green)**: These students are showing strong consistency in both academics and wellness. They are on the right track.
* **60-79 (Blue)**: Most students fall here. They are stable but usually have one area (like career clarity or productivity) that needs a little push.
* **40-59 (Yellow)**: This is a warning zone. An SRI below 60 usually means either their wellness is dropping or they are starting to struggle with attendance and assignments.
* **Below 40 (Red)**: This is the danger zone. It indicates a serious dip in multiple areas at once (e.g., extremely high stress combined with low grades), requiring immediate intervention from a mentor.

---
---
**Author:** Harshit Sharma  
**Date:** February 2026
