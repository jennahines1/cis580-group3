import string
import numpy as np
import pandas as pd
import os
import matplotlib





# File to Input Likert Scale Data for Software/Metrics Visualizations (Graphs)

# List of Types of LLM Output Categories (High-level Summary, Functional Requirements, and Non-functional Requirements)
output_categories = ['Summary', 'Functional', 'Non-Functional']


# List of each of the Data Set Categories holding the names of the text files as the items
# Separating them into the sets of 3 for graphical output readability

# Digital Archives
digital_archives = ['racdam', 'archivespace', 'duraspace']

# Software/Research Databases
software_databases = ['openspending', 'culrepo', 'rdadmp']

# Extracurricular Activites
extracurricular_activities = ['planningpoker', 'zooinverse', 'campersplus']

# List that Holds Likert Scale Categories
likert_scale = ['Unambiguity', 'Consistency', 'Completeness', 'Modifiability', 'Feasability', 'Clarity', 'Testability', 'Traceability', 'Usability', 'Correctness', 'Compatibility', 'Security']




# List that Hold Likert Scale Rating
likert_rating = [1, 2, 3, 4, 5]



# List of LLM Models
llm_models = ['Gemma3', 'Llava', 'Granite3.2']