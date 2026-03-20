import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
import json
from pathlib import Path

# Setup paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

# Set seed for reproducibility
np.random.seed(42)

def perform_clustering():
    try:
        input_path = DATA_DIR / 'students_scored.csv'
        df = pd.read_csv(input_path)
    except Exception as e:
        print(f"Error loading file: {e}")
        return

    # 1. Feature Selection
    features = [
        'gpa', 'attendance', 'assignments_completion', 
        'stress_level', 'sleep_hours', 'mental_wellbeing', 
        'productivity_score', 'distractions', 
        'career_clarity', 'skill_readiness', 'engagement_score'
    ]
    X = df[features]

    # 2. Scaling
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # 3. Determine K (WCSS / Elbow)
    wcss = []
    for i in range(1, 11):
        kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=42)
        kmeans.fit(X_scaled)
        wcss.append(kmeans.inertia_)

    # We'll use K=3 or 4 based on previous knowledge of student personas
    # For this dataset of 50 students, 3-4 is optimal to avoid over-segmentation.
    k = 4
    kmeans = KMeans(n_clusters=k, init='k-means++', max_iter=300, n_init=10, random_state=42)
    clusters = kmeans.fit_predict(X_scaled)
    df['cluster'] = clusters

    # 4. PCA for visualization
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)
    df['pca1'] = X_pca[:, 0]
    df['pca2'] = X_pca[:, 1]

    # 5. Cluster Interpretation
    cluster_profiles = []
    for i in range(k):
        c_data = df[df['cluster'] == i]
        profile = {
            'cluster_id': i,
            'size': len(c_data),
            'avg_gpa': round(c_data['gpa'].mean(), 2),
            'avg_stress': round(c_data['stress_level'].mean(), 2),
            'avg_sri': round(c_data['SRI'].mean(), 2),
            'avg_engagement': round(c_data['engagement_score'].mean(), 2),
            'avg_clarity': round(c_data['career_clarity'].mean(), 2),
            'avg_productivity': round(c_data['productivity_score'].mean(), 2)
        }
        
        # Refined Labeling Logic (Based on Centroids)
        if profile['avg_gpa'] > 7.5 and profile['avg_stress'] > 6:
            profile['label'] = "High-Achieving but Stressed"
        elif profile['avg_clarity'] < 4:
            profile['label'] = "Career-Confused Underperformers"
        elif profile['avg_stress'] < 4:
            profile['label'] = "Stable & Balanced Students"
        else:
            profile['label'] = "High-Risk Disengaged Students"
        
        cluster_profiles.append(profile)

    # Label the dataframe
    cluster_map = {p['cluster_id']: p['label'] for p in cluster_profiles}
    df['cluster_label'] = df['cluster'].map(cluster_map)

    # 6. Export results
    output_csv = DATA_DIR / 'students_clustered.csv'
    df.to_csv(output_csv, index=False)
    
    # Save profiles for documentation
    output_profiles = DATA_DIR / 'cluster_profiles.json'
    with open(output_profiles, 'w') as f:
        json.dump(cluster_profiles, f, indent=4)

    print("Clustering completed successfully.")
    print("Clusters found:", [p['label'] for p in cluster_profiles])

if __name__ == "__main__":
    perform_clustering()
