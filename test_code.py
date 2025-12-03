################################# Test Code ####################################### 
# 
# Written by Jenna Hines

# Define and Create Arrays for which LLM's contain the Likert rankings, and which category they pertain to
import seaborn as sns
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import main 
import seaborn as sns

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
