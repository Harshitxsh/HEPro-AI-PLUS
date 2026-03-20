# Cluster Interpretation Document

## Activity 3: Uncovering Student Personas with ML

In this task, I used K-Means clustering to find hidden groups of students that aren't obvious at first glance. Instead of just looking at GPA, I grouped everyone based on their whole story—like their stress, how much they sleep, and if they actually know what they want to do after graduation.

---

## 🔍 The Four Groups I Found

### 1. High-Achievers but Stressed out

* **Who they are**: These students have great GPAs (around 8.14), but they are really struggling with stress (7.29).
* **What I noticed**: They're working really hard but they aren't very efficient because they're so stressed. They have high engagement but low productivity.
* **Risk**: **Medium**. Even though they have good grades, they are on the edge of burning out.

### 2. Lost & Confused (Low Career Clarity)

* **Who they are**: These students are struggling with their grades (GPA 5.66) and they don't really know where they're going yet (Career Clarity is very low).
* **What I noticed**: They actually manage their time okay, but because they have no clear goal, they don't seem motivated to push themselves.
* **Risk**: **High**. They need big-picture career help more than just study tips.

### 3. Balanced & Stable

* **Who they are**: These are the "solid" students. Mid-range grades, but almost zero stress and good sleep.
* **What I noticed**: They are consistent and happy. They don't need much intervention, just routine support.
* **Risk**: **Low**.

### 4. High-Risk / Disengaged

* **Who they are**: These students are in a tough spot. Lowest GPA and highest stress.
* **What I noticed**: They aren't productive at all and seem checked out from the platform.
* **Risk**: **Critical**. These are the students who need help right away.

---

## ⚖️ Why This is Better Than Only Using Rules

While my scoring system from Activity 2 is good, this ML approach showed me that **not every "Stable" student is actually safe**.

For example, I found that some students who look okay on paper are actually "Stressed Toppers" who might crash soon. Also, I realized that "Career Clarity" is a huge reason why some students stay stuck. Using both methods together gives a much clearer picture for mentors.

---
**Author:** Harshit Sharma  
**Date:** February 2026
