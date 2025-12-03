# File to Hold the Overall LLM Comparisons to Display During the Demo  

# Changed Code to Fit w/Jenna's if Created Arrays Want to be Utilized Outside of This File
# Then Can just Call This File to Use
import string
import numpy as np
import pandas as pd
import os
import math
import matplotlib
import matplotlib.pyplot as plt
import warnings
from sklearn import metrics
import seaborn as sns
import matplotlib.ticker as ticker
from matplotlib.patches import PathPatch

# Call to Main
#import main
# Call to Jenna's Nonfunctional File for Arrays
#import nonfunc
# Call to Jenna's Story File for Arrays
#import story
#

from main import *

likert_scale = ['Unambiguity', 'Consistency', 'Completeness', 'Modifiability', 'Feasibility', 'Clarity', 'Testability', 'Traceability', 'Usability', 'Correctness', 'Compatibility', 'Security']

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



functional = {
    "Gemma3": {
        "racdam": {"Functional": gemma_racdam_functional},
        "archivespace": {"Functional": gemma_archivespace_functional},
        "duraspace": {"Functional": gemma_duraspace_functional},
        "openspending": {"Functional": gemma_openspending_functional},
        "culrepo": {"Functional": gemma_culrepo_functional},
        "rdadmp": { "Functional": gemma_rdadmp_functional},
        "planningpoker": {"Functional": gemma_planningpoker_functional},
        "zooinverse": {"Functional": gemma_zooniverse_functional},
        "campersplus": {"Functional": gemma_campersplus_functional}
    },
    "Llava": {
        "racdam": {"Functional": llava_racdam_functional},
        "archivespace": {"Functional": llava_archivespace_functional},
        "duraspace": {"Functional": llava_duraspace_functional},
        "openspending": {"Functional": llava_openspending_functional},
        "culrepo": {"Functional": llava_culrepo_functional},
        "rdadmp": {"Functional": llava_rdadmp_functional},
        "planningpoker": {"Functional": llava_planningpoker_functional},
        "zooinverse": {"Functional": llava_zooniverse_functional},
        "campersplus": {"Functional": llava_campersplus_functional}
    },
    "Granite3.2": {
        "racdam": { "Functional": granite_racdam_functional},
        "archivespace": {"Functional": granite_archivespace_functional},
        "duraspace": {"Functional": granite_duraspace_functional},
        "openspending": {"Functional": granite_openspending_functional},
        "culrepo": { "Functional": granite_culrepo_functional},
        "rdadmp": {"Functional": granite_rdadmp_functional},
        "planningpoker": {"Functional": granite_planningpoker_functional},
        "zooinverse": {"Functional": granite_zooniverse_functional},
        "campersplus": {"Functional": granite_campersplus_functional}
    }
}


# Gemma Array
gemma_llm = {
    "Stories": {
        "racdam": {"gemma": gemma_racdam_story},
        "archivespace": {"gemma": gemma_archivespace_story},
        "duraspace": {"gemma": gemma_duraspace_story},
        "openspending": {"gemma": gemma_openspending_story},
        "culrepo": {"gemma": gemma_culrepo_story},
        "rdadmp": {"gemma": gemma_rdadmp_story},
        "planningpoker": {"gemma": gemma_planningpoker_story},
        "zooinverse": {"gemma": gemma_zooniverse_story},
        "campersplus": {"gemma": gemma_campersplus_story}
    },
    "Functional": {
        "racdam": {"gemma": gemma_racdam_functional},
        "archivespace": {"gemma": gemma_archivespace_functional},
        "duraspace": {"gemma": gemma_duraspace_functional},
        "openspending": {"gemma": gemma_openspending_functional},
        "culrepo": {"gemma": gemma_culrepo_functional},
        "rdadmp": { "gemma": gemma_rdadmp_functional},
        "planningpoker": {"gemma": gemma_planningpoker_functional},
        "zooinverse": {"gemma": gemma_zooniverse_functional},
        "campersplus": {"gemma": gemma_campersplus_functional}
    },
    "NonFunctional": {
        "racdam": {"gemma": gemma_racdam_nonfunctional},
        "archivespace": {"gemma": gemma_archivespace_nonfunctional},
        "duraspace": {"gemma": gemma_duraspace_nonfunctional},
        "openspending": {"gemma": gemma_openspending_nonfunctional},
        "culrepo": {"gemma": gemma_culrepo_nonfunctional},
        "rdadmp": { "gemma": gemma_rdadmp_nonfunctional},
        "planningpoker": {"gemma": gemma_planningpoker_nonfunctional},
        "zooinverse": {"gemma": gemma_zooniverse_nonfunctional},
        "campersplus": {"gemma": gemma_campersplus_nonfunctional}
    }
}


# Llava Array
llava_llm = {
    "Stories": {
        "racdam": {"llava": llava_racdam_story},
        "archivespace": {"llava": llava_archivespace_story},
        "duraspace": {"llava": llava_duraspace_story},
        "openspending": {"llava": llava_openspending_story},
        "culrepo": {"llava": llava_culrepo_story},
        "rdadmp": {"llava": llava_rdadmp_story},
        "planningpoker": {"llava": llava_planningpoker_story},
        "zooinverse": {"llava": llava_zooniverse_story},
        "campersplus": {"llava": llava_campersplus_story}
    },
    "Functional": {
        "racdam": {"llava": llava_racdam_functional},
        "archivespace": {"llava": llava_archivespace_functional},
        "duraspace": {"llava": llava_duraspace_functional},
        "openspending": {"llava": llava_openspending_functional},
        "culrepo": {"llava": llava_culrepo_functional},
        "rdadmp": {"llava": llava_rdadmp_functional},
        "planningpoker": {"llava": llava_planningpoker_functional},
        "zooinverse": {"llava": llava_zooniverse_functional},
        "campersplus": {"llava": llava_campersplus_functional}
    },
    "NonFunctional": {
        "racdam": {"llava": llava_racdam_nonfunctional},
        "archivespace": {"llava": llava_archivespace_nonfunctional},
        "duraspace": {"llava": llava_duraspace_nonfunctional},
        "openspending": {"llava": llava_openspending_nonfunctional},
        "culrepo": {"llava": llava_culrepo_nonfunctional},
        "rdadmp": {"llava": llava_rdadmp_nonfunctional},
        "planningpoker": {"llava": llava_planningpoker_nonfunctional},
        "zooinverse": {"llava": llava_zooniverse_nonfunctional},
        "campersplus": {"llava": llava_campersplus_nonfunctional}
    }
}


# Granite Array
granite_llm = {
    "Stories": {
        "racdam": {"granite": granite_racdam_story},
        "archivespace": {"granite": granite_archivespace_story},
        "duraspace": {"granite": granite_duraspace_story},
        "openspending": {"granite": granite_openspending_story},
        "culrepo": {"granite": granite_culrepo_story},
        "rdadmp": {"granite": granite_rdadmp_story},
        "planningpoker": {"granite": granite_planningpoker_story},
        "zooinverse": {"granite": granite_zooniverse_story},
        "campersplus": {"granite": granite_campersplus_story}
    },
    "Functional": {
        "racdam": { "granite": granite_racdam_functional},
        "archivespace": {"granite": granite_archivespace_functional},
        "duraspace": {"granite": granite_duraspace_functional},
        "openspending": {"granite": granite_openspending_functional},
        "culrepo": { "granite": granite_culrepo_functional},
        "rdadmp": {"granite": granite_rdadmp_functional},
        "planningpoker": {"granite": granite_planningpoker_functional},
        "zooinverse": {"granite": granite_zooniverse_functional},
        "campersplus": {"granite": granite_campersplus_functional}
    },
    "NonFunctional": {
        "racdam": { "granite": granite_racdam_nonfunctional},
        "archivespace": {"granite": granite_archivespace_nonfunctional},
        "duraspace": {"granite": granite_duraspace_nonfunctional},
        "openspending": {"granite": granite_openspending_nonfunctional},
        "culrepo": { "granite": granite_culrepo_nonfunctional},
        "rdadmp": {"granite": granite_rdadmp_nonfunctional},
        "planningpoker": {"granite": granite_planningpoker_nonfunctional},
        "zooinverse": {"granite": granite_zooniverse_nonfunctional},
        "campersplus": {"granite": granite_campersplus_nonfunctional}
    }
}


llm = {
    "Gemma": {
        "racdam": {"all_llm": gemma_racdam_story},
        "archivespace": {"all_llm": gemma_archivespace_story},
        "duraspace": {"all_llm": gemma_duraspace_story},
        "openspending": {"all_llm": gemma_openspending_story},
        "culrepo": {"all_llm": gemma_culrepo_story},
        "rdadmp": {"all_llm": gemma_rdadmp_story},
        "planningpoker": {"all_llm": gemma_planningpoker_story},
        "zooinverse": {"all_llm": gemma_zooniverse_story},
        "campersplus": {"all_llm": gemma_campersplus_story},
        "racdam": {"all_llm": gemma_racdam_functional},
        "archivespace": {"all_llm": gemma_archivespace_functional},
        "duraspace": {"all_llm": gemma_duraspace_functional},
        "openspending": {"all_llm": gemma_openspending_functional},
        "culrepo": {"all_llm": gemma_culrepo_functional},
        "rdadmp": { "all_llm": gemma_rdadmp_functional},
        "planningpoker": {"all_llm": gemma_planningpoker_functional},
        "zooinverse": {"all_llm": gemma_zooniverse_functional},
        "campersplus": {"all_llm": gemma_campersplus_functional},
        "racdam": {"all_llm": gemma_racdam_nonfunctional},
        "archivespace": {"all_llm": gemma_archivespace_nonfunctional},
        "duraspace": {"all_llm": gemma_duraspace_nonfunctional},
        "openspending": {"all_llm": gemma_openspending_nonfunctional},
        "culrepo": {"all_llm": gemma_culrepo_nonfunctional},
        "rdadmp": { "all_llm": gemma_rdadmp_nonfunctional},
        "planningpoker": {"all_llm": gemma_planningpoker_nonfunctional},
        "zooinverse": {"all_llm": gemma_zooniverse_nonfunctional},
        "campersplus": {"all_llm": gemma_campersplus_nonfunctional}
    },
    "Llava": {
        "racdam": {"all_llm": llava_racdam_story},
        "archivespace": {"all_llm": llava_archivespace_story},
        "duraspace": {"all_llm": llava_duraspace_story},
        "openspending": {"all_llm": llava_openspending_story},
        "culrepo": {"all_llm": llava_culrepo_story},
        "rdadmp": {"all_llm": llava_rdadmp_story},
        "planningpoker": {"all_llm": llava_planningpoker_story},
        "zooinverse": {"all_llm": llava_zooniverse_story},
        "campersplus": {"all_llm": llava_campersplus_story},
        "racdam": {"all_llm": llava_racdam_functional},
        "archivespace": {"all_llm": llava_archivespace_functional},
        "duraspace": {"all_llm": llava_duraspace_functional},
        "openspending": {"all_llm": llava_openspending_functional},
        "culrepo": {"all_llm": llava_culrepo_functional},
        "rdadmp": {"all_llm": llava_rdadmp_functional},
        "planningpoker": {"all_llm": llava_planningpoker_functional},
        "zooinverse": {"all_llm": llava_zooniverse_functional},
        "campersplus": {"all_llm": llava_campersplus_functional},
        "racdam": {"all_llm": llava_racdam_nonfunctional},
        "archivespace": {"all_llm": llava_archivespace_nonfunctional},
        "duraspace": {"all_llm": llava_duraspace_nonfunctional},
        "openspending": {"all_llm": llava_openspending_nonfunctional},
        "culrepo": {"all_llm": llava_culrepo_nonfunctional},
        "rdadmp": {"all_llm": llava_rdadmp_nonfunctional},
        "planningpoker": {"all_llm": llava_planningpoker_nonfunctional},
        "zooinverse": {"all_llm": llava_zooniverse_nonfunctional},
        "campersplus": {"all_llm": llava_campersplus_nonfunctional}
    },
    "Granite": {
        "racdam": {"all_llm": granite_racdam_story},
        "archivespace": {"all_llm": granite_archivespace_story},
        "duraspace": {"all_llm": granite_duraspace_story},
        "openspending": {"all_llm": granite_openspending_story},
        "culrepo": {"all_llm": granite_culrepo_story},
        "rdadmp": {"all_llm": granite_rdadmp_story},
        "planningpoker": {"all_llm": granite_planningpoker_story},
        "zooinverse": {"all_llm": granite_zooniverse_story},
        "campersplus": {"all_llm": granite_campersplus_story},
        "racdam": { "all_llm": granite_racdam_functional},
        "archivespace": {"all_llm": granite_archivespace_functional},
        "duraspace": {"all_llm": granite_duraspace_functional},
        "openspending": {"all_llm": granite_openspending_functional},
        "culrepo": { "all_llm": granite_culrepo_functional},
        "rdadmp": {"all_llm": granite_rdadmp_functional},
        "planningpoker": {"all_llm": granite_planningpoker_functional},
        "zooinverse": {"all_llm": granite_zooniverse_functional},
        "campersplus": {"all_llm": granite_campersplus_functional},
        "racdam": { "all_llm": granite_racdam_nonfunctional},
        "archivespace": {"all_llm": granite_archivespace_nonfunctional},
        "duraspace": {"all_llm": granite_duraspace_nonfunctional},
        "openspending": {"all_llm": granite_openspending_nonfunctional},
        "culrepo": { "all_llm": granite_culrepo_nonfunctional},
        "rdadmp": {"all_llm": granite_rdadmp_nonfunctional},
        "planningpoker": {"all_llm": granite_planningpoker_nonfunctional},
        "zooinverse": {"all_llm": granite_zooniverse_nonfunctional},
        "campersplus": {"all_llm": granite_campersplus_nonfunctional}
    }
}



# Changed the Code to be Utilized Outside of File, so Changed Graph Codes to Match Array Calls
# Line Graph Showing Average of All LLM Rating's Against One Another
llm_rows = []
for model, datasets in llm.items():
    for ds, data in datasets.items():
        all_avg = float(np.mean(data["all_llm"]))
        llm_rows.append({"Model": model, "Dataset": ds, "All_Avg": all_avg})
all_comparison_df = pd.DataFrame(llm_rows)
all_comparison_df = all_comparison_df.sort_values(by=["Model", "Dataset"]).reset_index(drop=True)

def plot_all_graph(llm, likert_scale):
    results = []
    for model, datasets in llm.items():
        all_scores = np.array([datasets[ds]["all_llm"] for ds in datasets])
        avg_per_category = all_scores.mean(axis=0)
        results.append(pd.DataFrame({
            "Model": model,
            "Likert Category": likert_scale,
            "Avg_Score": avg_per_category
        }))
    line_df = pd.concat(results)
    plt.figure(figsize=(11, 7))
    sns.lineplot(
        data=line_df,
        x="Likert Category",
        y="Avg_Score",
        hue="Model",
        palette="gnuplot2",
        marker="8"
    )
    plt.title("LLM Averages")
    plt.ylabel("Average Score")
    plt.ylim(1, 5)
    plt.xticks(fontsize = 7, rotation = 65)
    plt.show()

plot_all_graph(llm, likert_scale)


# Line Graphs for Each of the LLMs Displaying their Trends


gemma_rows = []
for model, datasets in gemma_llm.items():
    for ds, data in datasets.items():
        gemma_avg = float(np.mean(data["gemma"]))
        gemma_rows.append({"Output Category": model, "Dataset": ds, "Gemma_Avg": gemma_avg})
gemma_comparison_df = pd.DataFrame(gemma_rows)
gemma_comparison_df = gemma_comparison_df.sort_values(by=["Output Category", "Dataset"]).reset_index(drop=True)

def plot_gemma(gemma_llm, likert_scale):
    results = []
    for model, datasets in gemma_llm.items():
        all_scores = np.array([datasets[ds]["gemma"] for ds in datasets])
        avg_per_category = all_scores.mean(axis=0)
        results.append(pd.DataFrame({
            "Output Category": model,
            "Likert Category": likert_scale,
            "Avg_Score": avg_per_category
        }))
    line_df = pd.concat(results)
    plt.figure(figsize=(11, 7))
    sns.lineplot(
        data=line_df,
        x="Likert Category",
        y="Avg_Score",
        hue="Output Category",
        palette="gnuplot2",
        marker="8"
    )
    plt.title("Gemma Average Scores")
    plt.ylabel("Average Score")
    plt.ylim(1, 5)
    plt.xticks(fontsize = 7, rotation = 65)
    plt.show()


plot_gemma(gemma_llm, likert_scale)



llava_rows = []
for model, datasets in llava_llm.items():
    for ds, data in datasets.items():
        llava_avg = float(np.mean(data["llava"]))
        llava_rows.append({"Output Category": model, "Dataset": ds, "Llava_Avg": llava_avg})
llava_comparison_df = pd.DataFrame(llava_rows)
llava_comparison_df = llava_comparison_df.sort_values(by=["Output Category", "Dataset"]).reset_index(drop=True)

def plot_llava(llava_llm, likert_scale):
    results = []
    for model, datasets in llava_llm.items():
        all_scores = np.array([datasets[ds]["llava"] for ds in datasets])
        avg_per_category = all_scores.mean(axis=0)
        results.append(pd.DataFrame({
            "Output Category": model,
            "Likert Category": likert_scale,
            "Avg_Score": avg_per_category
        }))
    line_df = pd.concat(results)
    plt.figure(figsize=(11, 7))
    sns.lineplot(
        data=line_df,
        x="Likert Category",
        y="Avg_Score",
        hue="Output Category",
        palette="gnuplot2",
        marker="8"
    )
    plt.title("Llava Average Scores")
    plt.ylabel("Average Score")
    plt.ylim(1, 5)
    plt.xticks(fontsize = 7, rotation = 65)
    plt.show()


plot_llava(llava_llm, likert_scale)




rows_granite = []
for model, datasets in granite_llm.items():
    for ds, data in datasets.items():
        granite_avg = float(np.mean(data["granite"]))
        rows_granite.append({"Output Category": model, "Dataset": ds, "granite_Avg": granite_avg})
granite_comparison_df = pd.DataFrame(rows_granite)
granite_comparison_df = granite_comparison_df.sort_values(by=["Output Category", "Dataset"]).reset_index(drop=True)




def plot_granite(granite_llm, likert_scale):
    results = []
    for model, datasets in granite_llm.items():
        all_scores = np.array([datasets[ds]["granite"] for ds in datasets])
        avg_per_category = all_scores.mean(axis=0)
        results.append(pd.DataFrame({
            "Output Category": model,
            "Likert Category": likert_scale,
            "Avg_Score": avg_per_category
        }))
    line_df = pd.concat(results)
    #plt.figure(figsize=(14, 7))
    plt.figure(figsize=(11, 7))
    sns.lineplot(
        data=line_df,
        x="Likert Category",
        y="Avg_Score",
        hue="Output Category",
        palette="gnuplot2",
        marker="8"
    )
    plt.title("Granite Average Scores")
    plt.ylabel("Average Score")
    plt.ylim(1, 5)
    plt.xticks(fontsize = 7, rotation = 65)
    plt.show()


plot_granite(granite_llm, likert_scale)



# Box Plots for Each of the LLMS to Display Distributions


# GEMMA:
gemma_boxPlots = pd.DataFrame({
    'Stories': [5, 5, 4, 3, 4, 4, 5, 5, 4, 5, 4, 5, 5, 4, 4, 5, 5, 4, 5, 5, 4, 5, 5, 3, 5, 4, 5, 4, 4, 5, 4, 5, 4, 4, 5, 5, 5, 4, 5, 3, 2, 5, 2, 5, 1, 4, 2, 2, 5, 5, 5, 4, 4, 3, 2, 2, 3, 5, 3, 2, 3, 2, 3, 4, 4, 4, 4, 4, 5, 5, 3, 3, 5, 5, 3, 4, 5, 5, 5, 5, 4, 4, 4, 4, 5, 5, 3, 5, 5, 5, 5, 5, 4, 4, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
    'Functional': [5, 5, 5, 4, 5, 5, 5, 5, 5, 4, 4, 5, 5, 4, 5, 5, 5, 4, 5, 5, 4, 4, 5, 5, 5, 5, 4, 3, 4, 4, 5, 5, 4, 5, 3, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 5, 3, 3, 3, 4, 4, 4, 3, 4, 4, 3, 3, 3, 4, 4, 2, 3, 4, 5, 3, 4, 4, 4, 5, 5, 3, 4, 5, 5, 5, 5, 4, 5, 3, 4, 5, 5, 3, 5, 5, 5, 3, 5, 5, 5, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
    'NonFunctional': [5, 4, 4, 3, 4, 5, 5, 5, 5, 4, 4, 5, 4, 4, 4, 3, 4, 3, 3, 4, 4, 4, 4, 5, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1, 4, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 2, 4, 3, 2, 4, 2, 2, 4, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
})



gemma_labels = list(gemma_boxPlots)
gemma_boxPlots = np.array(gemma_boxPlots)


plt.boxplot(gemma_boxPlots, labels=gemma_labels)
plt.title("Gemma Box Plot")
plt.ylabel('Scores')
plt.xlabel('Categories')


plt.show()




# LLAVA:
llava_boxPlots = pd.DataFrame({
    'Stories': [5, 5, 5, 1, 5, 5, 4, 5, 4, 5, 4, 5, 5, 4, 4, 5, 5, 4, 5, 5, 4, 5, 5, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 5, 4, 3, 4, 4, 5, 5, 5, 3, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'Functional': [4, 5, 4, 4, 5, 3, 4, 5, 4, 5, 4, 5, 5, 3, 4, 4, 3, 4, 3, 4, 4, 4, 4, 5, 5, 2, 2, 1, 1, 3, 1, 4, 1, 1, 1, 1, 5, 5, 5, 2, 1, 4, 2, 5, 3, 5, 4, 2, 3, 4, 4, 4, 3, 3, 3, 2, 3, 4, 5, 2, 2, 2, 3, 3, 4, 4, 2, 3, 4, 4, 4, 4, 5, 3, 5, 4, 5, 5, 3, 3, 5, 4, 3, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'NonFunctional': [4, 5, 5, 5, 4, 4, 5, 5, 5, 5, 4, 5, 5, 3, 3, 4, 4, 5, 5, 4, 4, 4, 5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 2, 3, 3, 2, 4, 3, 3, 4, 4, 4, 3, 3, 2, 4, 3, 2, 2, 1, 3, 2, 2, 2, 2, 5, 1, 4, 3, 2, 3, 3, 1 ,2, 4, 4, 5, 3, 5, 4, 5, 4, 3, 3, 5, 4, 3, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
})


llava_labels = list(llava_boxPlots)
llava_boxPlots = np.array(llava_boxPlots)

plt.boxplot(llava_boxPlots, labels=llava_labels)
plt.title("Llava Box Plot")
plt.ylabel('Scores')
plt.xlabel('Categories')
plt.show()

# GRANITE
granite_boxPlots = pd.DataFrame({
    'Stories': [4, 2, 4, 3, 4, 2, 3, 5, 4, 5, 4, 5, 5, 2, 4, 3, 4, 2, 2, 4, 3, 3, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 5, 4, 4, 3, 4, 5, 5, 5, 5, 2, 5, 5, 5, 4, 5, 5, 4, 4, 3, 4, 4, 3, 5, 5, 5, 5, 5, 5, 4, 5, 5, 5, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'Functional': [4, 4, 3, 5, 4, 3, 4, 5, 4, 4, 5, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 4, 2, 2, 2, 2, 3, 2, 3, 2, 1, 5, 5, 5, 4, 4, 5, 4, 5, 5, 5, 3, 3, 5, 5, 5, 4, 3, 3, 3, 3, 4, 4, 4, 2, 5, 5, 5, 4, 5, 5, 3, 4, 5, 4, 5, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'NonFunctional': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 2, 4, 2, 3, 2, 2, 4, 3, 2, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 5, 4, 4, 4, 4, 4, 5, 5, 4, 4, 4, 4, 3, 4, 3, 2, 3, 2, 3, 2, 4, 2, 5, 5, 4, 3, 3, 4, 4, 5, 5, 5, 3, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
})


granite_labels = list(granite_boxPlots)
granite_boxPlots = np.array(granite_boxPlots)

plt.boxplot(granite_boxPlots, labels=granite_labels)
plt.title("Granite Box Plot")
plt.ylabel('Scores')
plt.xlabel('Categories')
plt.show()



# BY LLM-
all_llm = pd.DataFrame({
    'Gemma': [5, 5, 4, 3, 4, 4, 5, 5, 4, 5, 4, 5, 5, 4, 4, 5, 5, 4, 5, 5, 4, 5, 5, 3, 5, 4, 5, 4, 4, 5, 4, 5, 4, 4, 5, 5, 5, 4, 5, 3, 2, 5, 2, 5, 1, 4, 2, 2, 5, 5, 5, 4, 4, 3, 2, 2, 3, 5, 3, 2, 3, 2, 3, 4, 4, 4, 4, 4, 5, 5, 3, 3, 5, 5, 3, 4, 5, 5, 5, 5, 4, 4, 4, 4, 5, 5, 3, 5, 5, 5, 5, 5, 4, 4, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 5, 5, 5, 5, 5, 4, 4, 5, 5, 4, 5, 5, 5, 4, 5, 5, 4, 4, 5, 5, 5, 5, 4, 3, 4, 4, 5, 5, 4, 5, 3, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 5, 3, 3, 3, 4, 4, 4, 3, 4, 4, 3, 3, 3, 4, 4, 2, 3, 4, 5, 3, 4, 4, 4, 5, 5, 3, 4, 5, 5, 5, 5, 4, 5, 3, 4, 5, 5, 3, 5, 5, 5, 3, 5, 5, 5, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 3, 4, 5, 5, 5, 5, 4, 4, 5, 4, 4, 4, 3, 4, 3, 3, 4, 4, 4, 4, 5, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1, 4, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 2, 4, 3, 2, 4, 2, 2, 4, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'Llava': [5, 5, 5, 1, 5, 5, 4, 5, 4, 5, 4, 5, 5, 4, 4, 5, 5, 4, 5, 5, 4, 5, 5, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 5, 4, 3, 4, 4, 5, 5, 5, 3, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 5, 4, 4, 5, 3, 4, 5, 4, 5, 4, 5, 5, 3, 4, 4, 3, 4, 3, 4, 4, 4, 4, 5, 5, 2, 2, 1, 1, 3, 1, 4, 1, 1, 1, 1, 5, 5, 5, 2, 1, 4, 2, 5, 3, 5, 4, 2, 3, 4, 4, 4, 3, 3, 3, 2, 3, 4, 5, 2, 2, 2, 3, 3, 4, 4, 2, 3, 4, 4, 4, 4, 5, 3, 5, 4, 5, 5, 3, 3, 5, 4, 3, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 5, 5, 5, 4, 4, 5, 5, 5, 5, 4, 5, 5, 3, 3, 4, 4, 5, 5, 4, 4, 4, 5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 2, 3, 3, 2, 4, 3, 3, 4, 4, 4, 3, 3, 2, 4, 3, 2, 2, 1, 3, 2, 2, 2, 2, 5, 1, 4, 3, 2, 3, 3, 1 ,2, 4, 4, 5, 3, 5, 4, 5, 4, 3, 3, 5, 4, 3, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'Granite': [4, 2, 4, 3, 4, 2, 3, 5, 4, 5, 4, 5, 5, 2, 4, 3, 4, 2, 2, 4, 3, 3, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 5, 4, 4, 3, 4, 5, 5, 5, 5, 2, 5, 5, 5, 4, 5, 5, 4, 4, 3, 4, 4, 3, 5, 5, 5, 5, 5, 5, 4, 5, 5, 5, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 3, 5, 4, 3, 4, 5, 4, 4, 5, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 4, 2, 2, 2, 2, 3, 2, 3, 2, 1, 5, 5, 5, 4, 4, 5, 4, 5, 5, 5, 3, 3, 5, 5, 5, 4, 3, 3, 3, 3, 4, 4, 4, 2, 5, 5, 5, 4, 5, 5, 3, 4, 5, 4, 5, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 2, 4, 2, 3, 2, 2, 4, 3, 2, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 5, 4, 4, 4, 4, 4, 5, 5, 4, 4, 4, 4, 3, 4, 3, 2, 3, 2, 3, 2, 4, 2, 5, 5, 4, 3, 3, 4, 4, 5, 5, 5, 3, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
})


all_llm_labels = list(all_llm)
all_llm = np.array(all_llm)

plt.boxplot(all_llm, labels=all_llm_labels)
plt.title("Each LLM BoxPlot")
plt.ylabel('Scores')
plt.xlabel('LLM')
plt.show()


# Confirming DataFrame Created and Correct Values
#all_comparison_df
#gemma_comparison_df
#llava_comparison_df
#granite_comparison_df


# Scatter Plot 

def scatter_all(llm, likert_scale):
    results = []
    for model, datasets in llm.items():
        all_scores = np.array([datasets[ds]["all_llm"] for ds in datasets])
        avg_per_category = all_scores.mean(axis=0)
        results.append(pd.DataFrame({
            "Model": model,
            "Likert Category": likert_scale,
            "Avg_Score": avg_per_category
        }))
    scatter_df = pd.concat(results)
    plt.figure(figsize=(11, 7))
    sns.scatterplot(
        data= scatter_df,
        x="Likert Category",
        y="Avg_Score",
        hue="Model",
        palette="gnuplot2",
        marker="8"
    )
    plt.title("LLM Scatter Plot")
    plt.ylabel("Average Score")
    plt.ylim(1, 5)
    plt.xticks(fontsize = 7, rotation=65)
    plt.show()

scatter_all(llm, likert_scale)

# Bar Plot to See how the Different LLMS Compared to One ANother

def bar_all(llm, likert_scale):
    results = []
    for model, datasets in llm.items():
        all_scores = np.array([datasets[ds]["all_llm"] for ds in datasets])
        avg_per_category = all_scores.mean(axis=0)
        results.append(pd.DataFrame({
            "Model": model,
            "Likert Category": likert_scale,
            "Avg_Score": avg_per_category
        }))
    bar_df = pd.concat(results)
    plt.figure(figsize=(11, 7))
    sns.barplot(
        x="Likert Category",
        y="Avg_Score",
        data = bar_df, 
        hue="Model",
        palette= 'gnuplot2'
    )
    plt.title("LLM Bar Chart")
    plt.ylabel("Average Score")
    plt.ylim(1, 5)
    plt.xticks(fontsize = 7, rotation = 65)
    plt.show()



bar_all(llm, likert_scale)



# Time Data
# This really just proved that the LLM Performance Was Machine Dependent
time_data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

plt.plot(time_data, gemma_timing, color = 'blue', marker="8", label='Gemma')
plt.plot(time_data, llava_timing, color = 'magenta', marker="8", label='Llava')
plt.plot(time_data, granite_timing, color = 'orange', marker="8", label='Granite')

plt.xlabel('Seconds')
plt.ylabel('Value')
plt.title('LLM Timing Performance')

plt.legend()
plt.show()




