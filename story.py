# File to Hold the Story Comparisons Graphs to Display During the Demo
# Written by Jenna Hines

# Define and Create Arrays for which LLM's contain the Likert rankings, and which category they pertain to
import seaborn as sns

# Call Main Code
main


# Story Array
story = {
    "Gemma3": {
        "racdam": {"Story": gemma_racdam_story},
        "archivespace": {"Story": gemma_archivespace_story},
        "duraspace": {"Story": gemma_duraspace_story},
        "openspending": {"Story": gemma_openspending_story},
        "culrepo": {"Story": gemma_culrepo_story},
        "rdadmp": {"Story": gemma_rdadmp_story},
        "planningpoker": {"Story": gemma_planningpoker_story},
        "zooinverse": {"Story": gemma_zooniverse_story},
        "campersplus": {"Story": gemma_campersplus_story}
    },
    "Llava": {
        "racdam": {"Story": llava_racdam_story},
        "archivespace": {"Story": llava_archivespace_story},
        "duraspace": {"Story": llava_duraspace_story},
        "openspending": {"Story": llava_openspending_story},
        "culrepo": {"Story": llava_culrepo_story},
        "rdadmp": {"Story": llava_rdadmp_story},
        "planningpoker": {"Story": llava_planningpoker_story},
        "zooinverse": {"Story": llava_zooniverse_story},
        "campersplus": {"Story": llava_campersplus_story}
    },
    "Granite3.2": {
        "racdam": {"Story": granite_racdam_story},
        "archivespace": {"Story": granite_archivespace_story},
        "duraspace": {"Story": granite_duraspace_story},
        "openspending": {"Story": granite_openspending_story},
        "culrepo": {"Story": granite_culrepo_story},
        "rdadmp": {"Story": granite_rdadmp_story},
        "planningpoker": {"Story": granite_planningpoker_story},
        "zooinverse": {"Story": granite_zooniverse_story},
        "campersplus": {"Story": granite_campersplus_story}
    }
}


# Create Comparison Dataset DF
rows = []
for model, datasets in story.items():
    for ds, data in datasets.items():
        story_avg = float(np.mean(data["Story"]))
        rows.append({"Model": model, "Dataset": ds, "Story_Avg": story_avg})
story_comparison_df = pd.DataFrame(rows)
story_comparison_df = story_comparison_df.sort_values(by=["Model", "Dataset"]).reset_index(drop=True)


# Function for Plotting Model v 
def plot_story_heatmap(story_comparison_df):
    heatmap_df = story_comparison_df.pivot(index="Model", columns="Dataset", values="Story_Avg")
    plt.figure(figsize=(12, 4 + 0.25 * len(heatmap_df.columns)))
    sns.heatmap(heatmap_df, annot=True, fmt=".2f", cmap="YlOrBr", vmin=1, vmax=5)
    plt.title("StoryLikert Score Heatmap (average across 12 metrics)")
    plt.tight_layout()
    plt.show()

   
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
    plt.title("Average Story Likert Scores\nAcross All LLMs (Category vs Dataset)")
    plt.xlabel("Dataset")
    plt.ylabel("Likert Category")
    plt.tight_layout()
    plt.show()

    return matrix

# Plot Code

# Heatmap LLMs v Datasets, avg Likert Score amongst each for the Summary
plot_story_heatmap(story_comparison_df)

# Heatmap Dataset vs Likert Rankings, avg Likert score across all LLM's 
plot_likert_category_heatmap(story)
