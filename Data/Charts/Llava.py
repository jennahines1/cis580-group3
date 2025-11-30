
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Likert Data Dictionary
d = {
    'Category': ['Unambiguity', 'Consistency', 'Completeness', 'Modifiability', 'Feasibility',
                 'Clarity', 'Testability', 'Traceability', 'Usability', 'Correctness',
                 'Compatibility', 'Security'],
    'racdam': [5, 5, 5, 4, 5, 5, 5, 5, 5, 4, 4, 5],
    'archivespace': [5, 4, 5, 5, 5, 4, 5, 5, 4, 4, 5, 5],
    'duraspace': [5, 5, 4, 3, 4, 4, 5, 5, 4, 5, 3, 5],
    'campersplus': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'planningpoker': [3, 5, 3, 3, 3, 4, 4, 4, 3, 4, 4, 3],
    'zooinverse': [3, 3, 4, 4, 2, 3, 4, 5, 3, 4, 4, 4],
    'overspending': [5, 5, 3, 4, 5, 5, 5, 5, 4, 5, 3, 4],
    'culrepo': [5, 5, 3, 5, 5, 5, 3, 5, 5, 5, 4, 5],
    'rdadmp': [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
}

df = pd.DataFrame(d)

# HEATMAP of all datasets by category
plt.figure(figsize=(12, 8))
heatmap_data = df.set_index("Category")

sns.heatmap(heatmap_data, annot=True, cmap="coolwarm", linewidths=.5)
plt.title("Heatmap of Likert Ratings Across All User Stories", fontsize=16)
plt.xlabel("Dataset")
plt.ylabel("Requirement Category")
plt.tight_layout()
plt.show()

# PIE CHART — distribution of average scores per dataset
avg_scores = df.drop(columns=["Category"]).mean()

plt.figure(figsize=(10, 7))
plt.pie(avg_scores, labels=avg_scores.index, autopct="%1.1f%%", startangle=140)
plt.title("Average Likert Score Distribution by Dataset", fontsize=16)
plt.axis('equal')
plt.show()