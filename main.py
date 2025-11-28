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
gemma_racdam_story = [5, 5, 4, 3, 4, 4, 5, 5, 4, 5, 4, 5]
gemma_racdam_functional = [5, 5, 5, 4, 5, 5, 5, 5, 5, 4, 4, 5]
gemma_racdam_nonfunctional = [4, 4, 3, 4, 5, 5, 5, 5, 4, 4, 5]

# User Story: Archivespace
gemma_archivespace_story = [5, 4, 4, 5, 5, 4, 5, 5, 4, 5, 5, 3]
gemma_archivespace_functional = [5, 4, 5, 5, 5, 4, 5, 5, 4, 4, 5, 5]
gemma_archivespace_nonfunctional = [4, 4, 4, 3, 4, 3, 3, 4, 4, 4, 4, 5]

# User Story: Duraspace
gemma_duraspace_story = [5, 4, 5, 4, 4, 5, 4, 5, 4, 4, 5, 5]
gemma_duraspace_functional = [5, 5, 4, 3, 4, 4, 5, 5, 4, 5, 3, 5]
gemma_duraspace_nonfunctional = [3, 3, 3, 3, 3, 3, 2, 2, 2, 1, 4, 3]


# Llava Likert Lists
# User Story: Racdam
llava_racdam_story = [5, 5, 5, 1, 5, 5, 4, 5, 4, 5, 4, 5]
llava_racdam_functional = [4, 5, 4, 4, 5, 3, 4, 5, 4, 5, 4, 5]
llava_racdam_nonfunctional = [4, 5, 5, 5, 4, 4, 5, 5, 5, 5, 4, 5]

# User Story: Archivespace
# Provided an Identical Summary as Gemma did for Archivespace
llava_archivespace_story = [5, 4, 4, 5, 5, 4, 5, 5, 4, 5, 5, 3]
llava_archivespace_functional = [5, 3, 4, 4, 3, 4, 3, 4, 4, 4, 4, 5]
llava_archivespace_nonfunctional = [5, 3, 3, 4, 4, 5, 5, 4, 4, 4, 5, 5]

# User Story: Duraspace
llava_duraspace_story = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
llava_duraspace_functional = [5, 2, 2, 1, 1, 3, 1, 4, 1, 1, 1, 1]
llava_durspace_nonfunctional = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


# Granite Likert Lists
# User Story: Racdam
granite_racdam_story = [4, 2, 4, 3, 4, 2, 3, 5, 4, 5, 4, 5]
granite_racdam_functional = [4, 4, 3, 5, 4, 3, 4, 5, 4, 4, 5, 4]
granite_racdam_nonfunctional = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# User Story: Archivespace
granite_archivespace_story = [5, 2, 4, 3, 4, 2, 2, 4, 3, 3, 3, 2]
granite_archivespace_functional = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
granite_archivespace_nonfunctional = [4, 2, 4, 2, 3, 2, 2, 4, 3, 2, 4, 1]

# User Story: Duraspace
granite_duraspace_story = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
granite_duraspace_functional = [3, 1, 4, 2, 2, 2, 2, 3, 2, 3, 2, 1]
granite_duraspace_nonfunctional = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# Extracurriculars
# MISSING = Automatic 1 Rating for All Scale Categories:
# Gemma
# campersplus: Missing Functional & Non-Functional Requirements
# planninggpoker: Missing Non-Functional Requirements
# Llava
# campersplus: Missing High Level Summary
# planningpoker: Missing High Level Summary


# Gemma Likert Lists
# User Story: campersplus
gemma_campersplus_story = [5, 4, 5, 3, 2, 5, 2, 5, 1, 4, 2, 2]
gemma_campersplus_functional = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
gemma_campersplus_nonfunctional = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# User Story: planningpoker
gemma_planningpoker_story = [5, 5, 5, 4, 4, 3, 2, 2, 3, 5, 3, 2]
gemma_planningpoker_functional =  [3, 5, 3, 3, 3, 4, 4, 4, 3, 4, 4, 3]
gemma_planningpoker_nonfunctional = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# User Story: zooniverse
gemma_zooniverse_story = [3, 2, 3, 4, 4, 4, 4, 4, 5, 5, 3, 3]
gemma_zooniverse_functional = [3, 3, 4, 4, 2, 3, 4, 5, 3, 4, 4, 4]
gemma_zooniverse_nonfunctional = [1, 3, 2, 4, 3, 2, 4, 2, 2, 4, 3, 3]


# Llava Likert Lists
# User Story: campersplus
llava_campersplus_story = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
llava_campersplus_functional = [5, 5, 5, 2, 1, 4, 2, 5, 3, 5, 4, 2]
llava_campersplus_nonfunctional = [3, 3, 2, 3, 3, 2, 4, 3, 3, 4, 4, 4]

# User Story: planningpoker
llava_planningpoker_story = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
llava_planningpoker_functional = ['Unambiguity', 'Consistency', 'Completeness', 'Modifiability', 'Feasibility', 'Clarity', 'Testability', 'Traceability', 'Usability', 'Correctness', 'Compatibility', 'Security']
llava_planningpoker_nonfunctional = ['Unambiguity', 'Consistency', 'Completeness', 'Modifiability', 'Feasibility', 'Clarity', 'Testability', 'Traceability', 'Usability', 'Correctness', 'Compatibility', 'Security']

# User Story: zooniverse
llava_zooniverse_story =['Unambiguity', 'Consistency', 'Completeness', 'Modifiability', 'Feasibility', 'Clarity', 'Testability', 'Traceability', 'Usability', 'Correctness', 'Compatibility', 'Security']
llava_zooniverse_functional = ['Unambiguity', 'Consistency', 'Completeness', 'Modifiability', 'Feasibility', 'Clarity', 'Testability', 'Traceability', 'Usability', 'Correctness', 'Compatibility', 'Security']
llava_zooniverse_nonfunctional = ['Unambiguity', 'Consistency', 'Completeness', 'Modifiability', 'Feasibility', 'Clarity', 'Testability', 'Traceability', 'Usability', 'Correctness', 'Compatibility', 'Security']


# Granite Likert Lists
# User Story: campersplus
granite_campersplus_story = ['Unambiguity', 'Consistency', 'Completeness', 'Modifiability', 'Feasibility', 'Clarity', 'Testability', 'Traceability', 'Usability', 'Correctness', 'Compatibility', 'Security']
granite_campersplus_functional = ['Unambiguity', 'Consistency', 'Completeness', 'Modifiability', 'Feasibility', 'Clarity', 'Testability', 'Traceability', 'Usability', 'Correctness', 'Compatibility', 'Security']
granite_campersplus_nonfunctional = ['Unambiguity', 'Consistency', 'Completeness', 'Modifiability', 'Feasibility', 'Clarity', 'Testability', 'Traceability', 'Usability', 'Correctness', 'Compatibility', 'Security']

# User Story: planningpoker
granite_planningpoker_story = ['Unambiguity', 'Consistency', 'Completeness', 'Modifiability', 'Feasibility', 'Clarity', 'Testability', 'Traceability', 'Usability', 'Correctness', 'Compatibility', 'Security']
granite_planningpoker_functional = ['Unambiguity', 'Consistency', 'Completeness', 'Modifiability', 'Feasibility', 'Clarity', 'Testability', 'Traceability', 'Usability', 'Correctness', 'Compatibility', 'Security']
granite_planningpoker_nonfunctional = ['Unambiguity', 'Consistency', 'Completeness', 'Modifiability', 'Feasibility', 'Clarity', 'Testability', 'Traceability', 'Usability', 'Correctness', 'Compatibility', 'Security']

# User Story: zooniverse
granite_zooniverse_story = ['Unambiguity', 'Consistency', 'Completeness', 'Modifiability', 'Feasibility', 'Clarity', 'Testability', 'Traceability', 'Usability', 'Correctness', 'Compatibility', 'Security']
granite_zooniverse_functional = ['Unambiguity', 'Consistency', 'Completeness', 'Modifiability', 'Feasibility', 'Clarity', 'Testability', 'Traceability', 'Usability', 'Correctness', 'Compatibility', 'Security']
granite_zooniverse_nonfunctional = ['Unambiguity', 'Consistency', 'Completeness', 'Modifiability', 'Feasibility', 'Clarity', 'Testability', 'Traceability', 'Usability', 'Correctness', 'Compatibility', 'Security']

#software/research databases
#Missing
#Gemma – openspending and rdadmp nonfunctional
#Llava – culrepo nonfunctional and functional – rdadmp story and nonfunctional – openspending story
#Granite – everything was missing 

# Gemma Likert Lists
# User Story: Openspending
gemma_openspending_story = [5, 5, 3, 4, 5, 5, 5, 5, 4, 4, 4, 4]
gemma_openspending_functional = [5, 5, 3, 4, 5, 5, 5, 5, 4, 5, 3, 4]
gemma_openspending_nonfunctional = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# User Story: Culrepo
gemma_culrepo_story = [5, 5, 3, 5, 5, 5, 5, 5, 4, 4, 3, 4]
gemma_culrepo_functional = [5, 5, 3, 5, 5, 5, 3, 5, 5, 5, 4, 5]
gemma_culrepo_nonfunctional = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# User Story: Rdadmp
gemma_rdadmp_story = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
gemma_rdadmp_functional = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
gemma_rdadmp_nonfunctional = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# Llava Likert Lists
# User Story: Openspending
llava_openspending_story = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
llava_openspending_functional = [5, 3, 5, 4, 5, 5, 3, 3, 5, 4, 3, 4]
llava_openspending_nonfunctional = [5, 3, 5, 4, 5, 4, 3, 3, 5, 4, 3, 4]

# User Story: Culrepo
llava_culrepo_story = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
llava_culrepo_functional = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
llava_culrepo_nonfunctional = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# User Story: Rdadmp
llava_rdadmp_story = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
llava_rdadmp_functional = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
llava_rdadmp_nonfunctional = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# Granite Likert Lists
# User Story: Openspending
granite_openspending_story = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
granite_openspending_functional = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
granite_openspending_nonfunctional = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# User Story: Culrepo
granite_culrepo_story = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
granite_culrepo_functional = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
granite_culrepo_nonfunctional = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# User Story: Rdadmp
granite_rdadmp_story = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
granite_rdadmp_functional = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
granite_rdadmp_nonfunctional = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]








