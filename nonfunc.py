# File to Hold the Non-Functional Data Visualization to Run for the Demo
# Written by Jenna Hines

# Define and Create Arrays for which LLM's contain the Likert rankings, and which category they pertain to
import seaborn as sns
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Call Main Code
from main import (
    likert_scale,
    gemma_racdam_nonfunctional,
    gemma_archivespace_nonfunctional,
    gemma_duraspace_nonfunctional,
    llava_racdam_nonfunctional,
    llava_archivespace_nonfunctional,
    llava_duraspace_nonfunctional,
    granite_racdam_nonfunctional,
    granite_archivespace_nonfunctional,
    granite_duraspace_nonfunctional,
    gemma_openspending_nonfunctional, 
    gemma_planningpoker_nonfunctional, 
    gemma_campersplus_nonfunctional, 
    gemma_culrepo_nonfunctional,
    gemma_zooniverse_nonfunctional,
    gemma_rdadmp_nonfunctional,
    llava_openspending_nonfunctional, 
    llava_culrepo_nonfunctional,
    llava_rdadmp_nonfunctional,
    llava_planningpoker_nonfunctional,
     llava_zooniverse_nonfunctional,
    llava_campersplus_nonfunctional,
    granite_openspending_nonfunctional,
     granite_culrepo_nonfunctional,
     granite_rdadmp_nonfunctional,
      granite_planningpoker_nonfunctional,
     granite_zooniverse_nonfunctional,
     granite_campersplus_nonfunctional)



# Non Functional Array
non_functional = {
    "Gemma3": {
        "racdam": {"NonFunctional": gemma_racdam_nonfunctional},
        "archivespace": {"NonFunctional": gemma_archivespace_nonfunctional},
        "duraspace": {"NonFunctional": gemma_duraspace_nonfunctional},
        "openspending": {"NonFunctional": gemma_openspending_nonfunctional},
        "culrepo": {"NonFunctional": gemma_culrepo_nonfunctional},
        "rdadmp": { "NonFunctional": gemma_rdadmp_nonfunctional},
        "planningpoker": {"NonFunctional": gemma_planningpoker_nonfunctional},
        "zooinverse": {"NonFunctional": gemma_zooniverse_nonfunctional},
        "campersplus": {"NonFunctional": gemma_campersplus_nonfunctional}
    },
    "Llava": {
        "racdam": {"NonFunctional": llava_racdam_nonfunctional},
        "archivespace": {"NonFunctional": llava_archivespace_nonfunctional},
        "duraspace": {"NonFunctional": llava_duraspace_nonfunctional},
        "openspending": {"NonFunctional": llava_openspending_nonfunctional},
        "culrepo": {"NonFunctional": llava_culrepo_nonfunctional},
        "rdadmp": {"NonFunctional": llava_rdadmp_nonfunctional},
        "planningpoker": {"NonFunctional": llava_planningpoker_nonfunctional},
        "zooinverse": {"NonFunctional": llava_zooniverse_nonfunctional},
        "campersplus": {"NonFunctional": llava_campersplus_nonfunctional}
    },
    "Granite3.2": {
        "racdam": { "NonFunctional": granite_racdam_nonfunctional},
        "archivespace": {"NonFunctional": granite_archivespace_nonfunctional},
        "duraspace": {"NonFunctional": granite_duraspace_nonfunctional},
        "openspending": {"NonFunctional": granite_openspending_nonfunctional},
        "culrepo": { "NonFunctional": granite_culrepo_nonfunctional},
        "rdadmp": {"NonFunctional": granite_rdadmp_nonfunctional},
        "planningpoker": {"NonFunctional": granite_planningpoker_nonfunctional},
        "zooinverse": {"NonFunctional": granite_zooniverse_nonfunctional},
        "campersplus": {"NonFunctional": granite_campersplus_nonfunctional}
    }
}

import seaborn as sns

# Create Comparison Dataset DF
rows = []
for model, datasets in non_functional.items():
    for ds, data in datasets.items():
        nonfunc_avg = float(np.mean(data["NonFunctional"]))
        rows.append({"Model": model, "Dataset": ds, "NonFunc_Avg": nonfunc_avg})
nonfunc_comparison_df = pd.DataFrame(rows)
nonfunc_comparison_df = nonfunc_comparison_df.sort_values(by=["Model", "Dataset"]).reset_index(drop=True)


# Function for Plotting Model
def plot_nonfunc_heatmap(nonfunc_comparison_df):
    heatmap_df = nonfunc_comparison_df.pivot(index="Model", columns="Dataset", values="NonFunc_Avg")
    plt.figure(figsize=(12, 4 + 0.25 * len(heatmap_df.columns)))
    sns.heatmap(heatmap_df, annot=True, fmt=".2f", cmap="YlOrBr", vmin=1, vmax=5)
    plt.title("Non-Functional Likert Score Heatmap (average across ALL metrics)")


def plot_likert_category_heatmap(non_functional):

    # prepare empty matrix
    datasets = list(next(iter(non_functional.values())).keys())  # 9 datasets
    matrix = pd.DataFrame(0.0, index=likert_scale, columns=datasets)

    # count LLMs contributing to avg
    counts = pd.DataFrame(0, index=likert_scale, columns=datasets)

    # accumulate values from all 3 LLMs
    for model, ds_dict in non_functional.items():
        for ds, scores in ds_dict.items():
            nonfunctional_scores = scores["NonFunctional"]

            for i, category in enumerate(likert_scale):
                matrix.loc[category, ds] += nonfunctional_scores[i]
                counts.loc[category, ds] += 1

    # compute averages
    matrix = matrix / counts

    # plotting heatmap
    plt.figure(figsize=(14, 8))
    sns.heatmap(matrix, annot=True, cmap="YlGnBu", vmin=1, vmax=5)
    plt.title("Average Non-Functional Requirement Likert Scores\nAcross All LLMs (Category vs Dataset)")
    plt.xlabel("Dataset")
    plt.ylabel("Likert Category")


def plot_likert_llm_graph(non_functional, likert_scale):

    results = []

    for model, datasets in non_functional.items():
        # collect all scores for that model across all datasets
        all_scores = np.array([datasets[ds]["NonFunctional"] for ds in datasets])
        avg_per_category = all_scores.mean(axis=0)

        results.append(pd.DataFrame({
            "Model": model,
            "Likert_Category": likert_scale,
            "Avg_Score": avg_per_category
        }))

    line_df = pd.concat(results)

    plt.figure(figsize=(14, 7))
    sns.lineplot(
        data=line_df,
        x="Likert_Category",
        y="Avg_Score",
        hue="Model",
        marker="o"
    )

    plt.title("Average Likert Score of Non-Functional Requirements Across Each Dataset for Each LLM")
    plt.ylabel("Average Score")
    plt.ylim(1, 5)
    plt.xticks(rotation=65)


# Plot Code

# Heatmap LLMs v Datasets, avg Likert Score amongst each for the Summary
plot_nonfunc_heatmap(nonfunc_comparison_df)

# Heatmap Dataset vs Likert Rankings, avg Likert score across all LLM's
plot_likert_category_heatmap(non_functional)

# Average Score across each Likert category
plot_likert_llm_graph(non_functional, likert_scale)


################################# Requirement Comparison Across LLM's ######################################

# Top Level Folder
data_path = 'Data' 

# Non-Functional Requirements to Look for
nfr_list = ['Scalability', 'Reliability', 'Usability', 'Security', 'Performance']


# Get LLM Names from .TXT Files 
def get_llm_name(file_name):
    lower_name = file_name.lower()
    if 'gemma' in lower_name:
        return 'Gemma'
    elif 'granite' in lower_name:
        return 'Granite'
    elif 'llava' in lower_name:
        return 'Llava'
    else:
        return 'Unknown'


# Loop through folders to get Data 
results = []

for subfolder in os.listdir(data_path):
    subfolder_path = os.path.join(data_path, subfolder)
    output_path = os.path.join(subfolder_path, 'Output')  # Output folder

    if os.path.isdir(output_path):

        for file_name in os.listdir(output_path):
         
            if file_name.lower().endswith('.txt'):
                file_path = os.path.join(output_path, file_name)
                 
                # .txt file name 
                llm_raw = file_name


                llm_std = get_llm_name(file_name)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Check Non Functional Requirement presence (1 = present, 0 = absent)
                nfr_presence = {nfr: int(nfr in content) for nfr in nfr_list}
                nfr_presence.update({'Dataset': subfolder, 'LLM': llm_raw, 'LLM_Standard': llm_std})
                results.append(nfr_presence)

#DF
df = pd.DataFrame(results)

# Compute number of missing NFRs per file
df['Missing_NFRs'] = len(nfr_list) - df[nfr_list].sum(axis=1)


# Create HeatMap
heatmap_data = df.pivot_table(index='LLM_Standard', 
                              columns='Dataset', 
                              values='Missing_NFRs', 
                              aggfunc='mean').fillna(0)


# Plot Heatmap 
plt.figure(figsize=(10,6))
sns.heatmap(heatmap_data, annot=True, fmt=".1f", cmap='Reds', cbar_kws={'label':'Avg Missing Non-Functional Requirements'})
plt.title('Average Missing Non-Functional Requirements per LLM and Dataset')
plt.ylabel('LLM')
plt.xlabel('Dataset')
plt.show()
