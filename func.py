# File to Hold the Functional Result Comparisons to run and Display Separately During the Dem

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns   # For heatmap

# Likert Data for Each Dataset

data = {
    'Category': ['Unambiguity', 'Consistency', 'Completeness', 'Modifiability', 'Feasibility',
                 'Clarity', 'Testability', 'Traceability', 'Usability', 'Correctness',
                 'Compatibility', 'Security'],

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

df = pd.DataFrame(data)
df_heatmap = df.set_index("Category")  # Better layout for heatmap

# HEATMAP GRAPH

plt.figure(figsize=(14, 10))
sns.heatmap(df_heatmap, annot=True, cmap="YlGnBu", linewidths=0.5)
plt.title("LLM functional Ratings – Heatmap")
plt.xlabel("Dataset")
plt.ylabel("Likert Category")
plt.tight_layout()
plt.show()

# LINE GRAPH

plt.figure(figsize=(18, 10))

for col in df.columns[1:]:
    plt.plot(df["Category"], df[col], marker='o', label=col)

plt.title("LLM Functional Ratings – Line Graph")
plt.xlabel("Likert Category")
plt.ylabel("Rating (1–5)")
plt.xticks(rotation=45)
plt.legend(title="Dataset", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()
o