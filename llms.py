# File to Hold the Overall LLM Comparisons to Display During the Demo  

# Changed Code to Fit w/Jenna's if Created Arrays Want to be Utilized Outside of This File
# Then Can just Call This File to Use
import seaborn as sns
import matplotlib.ticker as ticker
from matplotlib.patches import PathPatch

# Call to Main
main
nonfunc


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






