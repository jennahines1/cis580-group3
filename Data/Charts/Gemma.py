import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns   # Heatmap library

# Likert Dataset

d = {
    'Category': ['Unambiguity', 'Consistency', 'Completeness', 'Modifiability', 'Feasibility', 'Clarity',
                 'Testability', 'Traceability', 'Usability', 'Correctness', 'Compatibility', 'Security'],
    
    'racdam': [5, 5, 5, 4, 5, 5, 5, 5, 5, 4, 4, 5],
    'archivespace': [5, 4, 5, 5, 5, 4, 5, 5, 4, 4, 5, 5],
    'duraspace': [5, 5, 4, 3, 4, 4, 5, 5, 4, 5, 3, 5],
    'campersplus': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'planningpoker': [3, 5, 3, 3, 3, 4, 4, 4, 3, 4, 4, 3],
    'zooniverse': [3, 3, 4, 4, 2, 3, 4, 5, 3, 4, 4, 4],
    'openspending': [5, 5, 3, 4, 5, 5, 5, 5, 4, 5, 3, 4],
    'culrepo': [5, 5, 3, 5, 5, 5, 3, 5, 5, 5, 4, 5],
    'rdadmp': [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
}

df = pd.DataFrame(d)

# HEATMAP of all Likert values

plt.figure(figsize=(12, 8))
sns.heatmap(df.set_index('Category'), annot=True, cmap='Pastel1', linewidths=.5)
plt.title("Likert Scale Heatmap Across All Projects")
plt.tight_layout()
plt.show()


# PIE CHART for one project

project = 'racdam'  # <-- Change to any of: racdam, archivespace, duraspace, campersplus, etc.
pie_colors = plt.cm.Set3(np.linspace(0, 1, 12))

plt.figure(figsize=(8, 8))
plt.pie(
    df[project],
    labels=df['Category'],
    autopct='%1.1f%%',
    startangle=140,
    colors=pie_colors
)
plt.title(f"Distribution of Likert Ratings for {project.capitalize()}")
plt.tight_layout()
plt.show()
