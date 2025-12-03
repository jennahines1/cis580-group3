# File to Hold the Story Comparisons Graphs to Display During the Demo
# Written by Jenna Hines

# Define and Create Arrays for which LLM's contain the Likert rankings, and which category they pertain to
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Import entire main module to access story variables
import main

likert_scale = main.likert_scale


# Story Array
story = {
    "Gemma3": {
        "racdam": {"Story": main.gemma_racdam_story},
        "archivespace": {"Story": main.gemma_archivespace_story},
        "duraspace": {"Story": main.gemma_duraspace_story},
        "openspending": {"Story": main.gemma_openspending_story},
        "culrepo": {"Story": main.gemma_culrepo_story},
        "rdadmp": {"Story": main.gemma_rdadmp_story},
        "planningpoker": {"Story": main.gemma_planningpoker_story},
        "zooinverse": {"Story": main.gemma_zooniverse_story},
        "campersplus": {"Story": main.gemma_campersplus_story}
    },
    "Llava": {
        "racdam": {"Story": main.llava_racdam_story},
        "archivespace": {"Story": main.llava_archivespace_story},
        "duraspace": {"Story": main.llava_duraspace_story},
        "openspending": {"Story": main.llava_openspending_story},
        "culrepo": {"Story": main.llava_culrepo_story},
        "rdadmp": {"Story": main.llava_rdadmp_story},
        "planningpoker": {"Story": main.llava_planningpoker_story},
        "zooinverse": {"Story": main.llava_zooniverse_story},
        "campersplus": {"Story": main.llava_campersplus_story}
    },
    "Granite3.2": {
        "racdam": {"Story": main.granite_racdam_story},
        "archivespace": {"Story": main.granite_archivespace_story},
        "duraspace": {"Story": main.granite_duraspace_story},
        "openspending": {"Story": main.granite_openspending_story},
        "culrepo": {"Story": main.granite_culrepo_story},
        "rdadmp": {"Story": main.granite_rdadmp_story},
        "planningpoker": {"Story": main.granite_planningpoker_story},
        "zooinverse": {"Story": main.granite_zooniverse_story},
        "campersplus": {"Story": main.granite_campersplus_story}
    }
}


# Create Comparison Dataset DF
rows = []
for model, datasets in story.items():
    for ds, data in datasets.items():
        # Create Averages for Each Likert Ranking
        story_avg = float(np.mean(data["Story"]))
        rows.append({"Model": model, "Dataset": ds, "Story_Avg": story_avg})
# DF across all LLMS, and Datasets for Each Likert Category 
story_comparison_df = pd.DataFrame(rows)
story_comparison_df = story_comparison_df.sort_values(by=["Model", "Dataset"]).reset_index(drop=True)


# Function for Plotting Models
def plot_summary_heatmap(story_comparison_df):
    # Create Heatmap 
    heatmap_df = story_comparison_df.pivot(index="Model", columns="Dataset", values="Story_Avg")
    plt.figure(figsize=(12, 4 + 0.25 * len(heatmap_df.columns)))
    sns.heatmap(heatmap_df, annot=True, fmt=".2f", cmap="YlOrBr", vmin=1, vmax=5)
    plt.title("Summary Likert Score Heatmap (average across ALL metrics)")
   # plt.show()

   
def plot_likert_category_heatmap(story):

    # prepare empty matrix
    datasets = list(next(iter(story.values())).keys())  # 9 datasets
    matrix = pd.DataFrame(0.0, index=likert_scale, columns=datasets)

    # count LLMs contributing to avg
    counts = pd.DataFrame(0, index=likert_scale, columns=datasets)

    # accumulate values from all 3 LLMs
    for model, ds_dict in story.items():
        for ds, scores in ds_dict.items():
            story_scores = scores["Story"]

            for i, category in enumerate(likert_scale):
                matrix.loc[category, ds] += story_scores[i]
                counts.loc[category, ds] += 1

    # compute averages
    matrix = matrix / counts

    # plotting heatmap
    plt.figure(figsize=(14, 8))
    sns.heatmap(matrix, annot=True, cmap="YlGnBu", vmin=1, vmax=5)
    plt.title("Average Summary Likert Scores\nAcross All LLMs (Category vs Dataset)")
    plt.xlabel("Dataset")
    plt.ylabel("Likert Category")
    #plt.show()
    
def plot_likert_llm_graph(story, likert_scale):
    
    results = []

    for model, datasets in story.items():
        # collect all scores for that model across all datasets
        all_scores = np.array([datasets[ds]["Story"] for ds in datasets])
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

    plt.title("Average Likert Score of Summaries Across Each Dataset for Each LLM")
    plt.ylabel("Average Score")
    plt.ylim(1, 5)
   # plt.show()


# Plot Code

# Heatmap LLMs v Datasets, avg Likert Score amongst each for the Summary
plot_summary_heatmap(story_comparison_df)

# Heatmap Dataset vs Likert Rankings, avg Likert score across all LLM's 
plot_likert_category_heatmap(story)

# Average Score across each Likert category
plot_likert_llm_graph(story, likert_scale)

plt.show()
