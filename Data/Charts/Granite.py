import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# CREATE DATAFRAME
d = {
    'Category': ['Unambiguity', 'Consistency', 'Completeness', 'Modifiability', 'Feasibility', 'Clarity',
                 'Testability', 'Traceability', 'Usability', 'Correctness', 'Compatibility', 'Security'],
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
df_heat = df.set_index("Category")


# HEATMAP
plt.figure(figsize=(14, 8))
sns.heatmap(df_heat, annot=True, cmap="YlOrRd", linewidths=.5)
plt.title("Heatmap of Likert Ratings Across Systems", fontsize=20)
plt.xlabel("Systems")
plt.ylabel("Likert Category")
plt.tight_layout()
plt.show()

# PIE CHART (Example: Average ratings across all systems)
project = 'racdam'

# Create pie colors from magma colormap
pie_colors = plt.cm.magma(np.linspace(0, 1, 12))

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