# File to Hold the Non-Functional Data Visualization to Run for the Demo
# Written by Jenna Hines

# Define and Create Arrays for which LLM's contain the Likert rankings, and which category they pertain to
import seaborn as sns
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import main 



# Non Functional Array
non_functional = {
    "Gemma3": {
        "racdam": {"NonFunctional": main.gemma_racdam_nonfunctional},
        "archivespace": {"NonFunctional": main.gemma_archivespace_nonfunctional},
        "duraspace": {"NonFunctional": main.gemma_duraspace_nonfunctional},
        "openspending": {"NonFunctional": main.gemma_openspending_nonfunctional},
        "culrepo": {"NonFunctional": main.gemma_culrepo_nonfunctional},
        "rdadmp": { "NonFunctional": main.gemma_rdadmp_nonfunctional},
        "planningpoker": {"NonFunctional": main.gemma_planningpoker_nonfunctional},
        "zooinverse": {"NonFunctional": main.gemma_zooniverse_nonfunctional},
        "campersplus": {"NonFunctional": main.gemma_campersplus_nonfunctional}
    },
    "Llava": {
        "racdam": {"NonFunctional": main.llava_racdam_nonfunctional},
        "archivespace": {"NonFunctional": main.llava_archivespace_nonfunctional},
        "duraspace": {"NonFunctional": main.llava_duraspace_nonfunctional},
        "openspending": {"NonFunctional": main.llava_openspending_nonfunctional},
        "culrepo": {"NonFunctional": main.llava_culrepo_nonfunctional},
        "rdadmp": {"NonFunctional": main.llava_rdadmp_nonfunctional},
        "planningpoker": {"NonFunctional": main.llava_planningpoker_nonfunctional},
        "zooinverse": {"NonFunctional": main.llava_zooniverse_nonfunctional},
        "campersplus": {"NonFunctional": main.llava_campersplus_nonfunctional}
    },
    "Granite3.2": {
        "racdam": { "NonFunctional": main.granite_racdam_nonfunctional},
        "archivespace": {"NonFunctional": main.granite_archivespace_nonfunctional},
        "duraspace": {"NonFunctional": main.granite_duraspace_nonfunctional},
        "openspending": {"NonFunctional": main.granite_openspending_nonfunctional},
        "culrepo": { "NonFunctional": main.granite_culrepo_nonfunctional},
        "rdadmp": {"NonFunctional": main.granite_rdadmp_nonfunctional},
        "planningpoker": {"NonFunctional": main.granite_planningpoker_nonfunctional},
        "zooinverse": {"NonFunctional": main.granite_zooniverse_nonfunctional},
        "campersplus": {"NonFunctional": main.granite_campersplus_nonfunctional}
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

