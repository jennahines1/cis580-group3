# File to Input Likert Scale Data for Software/Metrics Visualizations (Graphs)
# CIS 580 Final Project, Erika Valle-Baird, Jenna Hines, Sierra Corl
# University of Michigan Dearborn

import string
import numpy as np
import pandas as pd
import os
import math
import matplotlib
import matplotlib.pyplot as plt
import warnings
from sklearn import metrics


# List of LLM Models
llm_models = ['Gemma3', 'Llava', 'Granite3.2']

# List of Types of LLM Output Categories (High-level Summary, Functional Requirements, and Non-functional Requirements)
output_categories = ['Summary', 'Functional', 'Non-Functional']

# List to Hold Time it Takes Each LLM to Begin Once Given the Prompt, Might need to Make Own Lists for Each LLM
llm_times = []

# List of each of the Data Set Categories holding the names of the text files as the items
# Main List to Hold all User Story Files For Comparisons, 9 Total
user_stories = ['Racdam', 'Archivespace', 'Duraspace', 'Openspending', 'Culrepo', 'Rdadmp', 'Planningpoker', 'Zooinverse', 'Campersplus']

# Separating them into the sets of 3 for graphical output readability if we want to chunk it
# Digital Archives
digital_archives = ['racdam', 'archivespace', 'duraspace']
# Software/Research Databases
software_databases = ['openspending', 'culrepo', 'rdadmp']
# Extracurricular Activites
extracurricular_activities = ['planningpoker', 'zooinverse', 'campersplus']

# LIKERT
# List that Holds Likert Scale Categories, 12 total
likert_scale = ['Unambiguity', 'Consistency', 'Completeness', 'Modifiability', 'Feasibility', 'Clarity', 'Testability', 'Traceability', 'Usability', 'Correctness', 'Compatibility', 'Security']

# List that Hold Likert Scale Rating
likert_rating = [1, 2, 3, 4, 5]


# Data for Digital Archives Section-
# Timing of Each LLM, Order: 0: Racdam, 1: Archivespace, 2: Duraspace, 3: Openspending, 4: Culrepo, 5: Rdadmp, 6: Planningpoker, 7: Zooinverse, 8: Campersplus
# 0's in Place of Rest Until Jenna and Sierra Fill Theirs in
# Using Total Number of Seconds for Time
gemma_timing = [107, 51, 112, 0, 0, 0, 14.4,10.5,12.4]
llava_timing = [238, 312, 236, 0, 0, 0, 14, 15.2,15.40]
granite_timing = [125, 43, 83, 0, 0, 0, 20.2, 25.2, 26]

# Digital Archives
# MISSING = Automatic 1 Rating for All Scale Categories:
# Granite3.2:
# durspace: Missing Functional & Non-Functional Requirements
# archivespace: Missing Functional Requirements
# racdam: Missing Non-Functional Requirements

# Gemma Likert Lists
# User Story: Racdam
gemma_racdam_story = []
gemma_racdam_functional = []
gemma_racdam_nonfunctional = []

# User Story: Archivespace
gemma_archivespace_story = []
gemma_archivespace_functional = []
gemma_archivespace_nonfunctional = []

# User Story: Duraspace
gemma_duraspace_story = []
gemma_duraspace_functional = []
gemma_duraspace_nonfunctional = []


# Llava Likert Lists
# User Story: Racdam
llava_racdam_story = []
llava_racdam_functional = []
llava_racdam_nonfunctional = []

# User Story: Archivespace
llava_archivespace_story = []
llava_archivespace_functional = []
llava_archivespace_nonfunctional = []

# User Story: Duraspace
llava_duraspace_story = []
llava_duraspace_functional = []
llava_durspace_nonfunctional = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


# Granite Likert Lists
# User Story: Racdam
granite_racdam_story = []
granite_racdam_functional = []
granite_racdam_nonfunctional = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# User Story: Archivespace
granite_archivespace_story = []
granite_archivespace_functional = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
granite_archivespace_nonfunctional = []

# User Story: Duraspace
granite_duraspace_story = []
granite_duraspace_functional = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
granite_duraspace_nonfunctional = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


# Extracurriculars
# MISSING = Automatic 1 Rating for All Scale Categories:
# Granite3.2:
# campersplus: Missing Functional & Non-Functional Requirements
# planninggpoker: Missing Functional Requirements
# zooniverse: Missing Non-Functional Requirements

# Gemma Likert Lists
# User Story: campersplus
gemma_racdam_story = []
gemma_racdam_functional = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
gemma_racdam_nonfunctional = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# User Story: planningpoker
gemma_archivespace_story = []
gemma_archivespace_functional = []
gemma_archivespace_nonfunctional = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# User Story: zooniverse
gemma_duraspace_story = []
gemma_duraspace_functional = []
gemma_duraspace_nonfunctional = []


# Llava Likert Lists
# User Story: campersplus
llava_racdam_story = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
llava_racdam_functional = []
llava_racdam_nonfunctional = []

# User Story: planningpoker
llava_archivespace_story = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
llava_archivespace_functional = []
llava_archivespace_nonfunctional = []

# User Story: zooniverse
llava_duraspace_story = []
llava_duraspace_functional = []
llava_durspace_nonfunctional = []


# Granite Likert Lists
# User Story: campersplus
granite_racdam_story = []
granite_racdam_functional = []
granite_racdam_nonfunctional = []

# User Story: planningpoker
granite_archivespace_story = []
granite_archivespace_functional = []
granite_archivespace_nonfunctional = []

# User Story: zooniverse
granite_duraspace_story = []
granite_duraspace_functional = []
granite_duraspace_nonfunctional = []







