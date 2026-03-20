# How My HEPro AI+ System Makes Decisions

## Activity 4: Mentor Matching & Intervention Engine

## 1. My Goal for This Task

In this final part of the project, I wanted to turn all the data and clusters I found earlier into real-world help for students. It's one thing to see a student is "High Risk," but I wanted my system to actually *do* something about it—like matching them with the right mentor and picking the best way to help them.

---

## 2. How the Data Flows (End-to-End)

I built this system to work like a relay race. Each part of the project hands off its data to the next:

1. **The Database (Task 1)**: I started with the raw student data.
2. **The Scoring Logic (Task 2)**: I turned that data into scores like APS and SRI.
3. **The ML Clusters (Task 3)**: I used K-Means to find hidden groups like "The Stressed Toppers."
4. **The Matching Engine (Task 4)**: This is where I take everything—the scores and the clusters—and find the perfect mentor for each student.
5. **The Result**: A clear list of who needs what, and immediate alerts for the students I'm really worried about.

---

## 3. My Matching Logic: Who Gets What?

I didn't want the system to just pick mentors randomly. I designed a set of rules that prioritized students based on their biggest "Pain Point."

### A. Finding the Problem (The "What")

I set up a hierarchy of needs in my code:

- **Wellness First**: If I see a student with too much stress or a low wellness score, they get a Wellness mentor immediately. I think mental health should always come first.
- **Direction & Goals**: For students who are "Career-Confused" (which my ML found in Task 3), I send them to a Career coach to find their motivation.
- **Academics & Study**: If the grades (APS) are the main issue, they get an Academic tutor.
- **Efficiency**: If they are just distracted or unorganized, they get a Productivity coach.

### B. Picking the Mentor (The "Who")

I created a dataset of 12 mentors with different specialties.

- **Seniority**: For students in the "Red" (Highest Risk) category, I made sure my system assigns them a **Senior** mentor for extra experience.
- **Fairness (Load Balancing)**: I didn't want to burn out our mentors! My system checks how many students each mentor already has. If two mentors are available, it picks the one who is less busy.

---

## 4. Why This Integrated System Works Better

By combining my **SRI score** (Task 2) with the **ML Clusters** (Task 3), I'm able to see things a simple grade-tracker would miss.

For example, a student might have a "Blue" (Stable) category but my ML cluster says they are "Stressed." My matching engine picks up on this subtle detail and assigns them a wellness check-in before they even realize they're burning out.

---

## 5. Thinking Big (Scalability)

I wrote this code to be modular. Whether we have 50 students or 5,000, the logic stays the same. The system balances the workload and flags the most urgent cases in seconds.

## 6. Closing Thoughts

Building this system showed me that AI isn't just about math; it's about making sure the right help gets to the right person at the right time. By automating the "Matching," we make sure no student falls through the cracks.

---
**Author:** Harshit Sharma
