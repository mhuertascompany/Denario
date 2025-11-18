from pathlib import Path

# Using pathlib (modern approach) to define the base directory as the directory that contains this file.
BASE_DIR = Path(__file__).resolve().parent

# REPO_DIR is defined as one directory above the package
REPO_DIR = BASE_DIR.parent
## in colab we need REPO_DIR = "/content/Denario/"

LaTeX_DIR = BASE_DIR / "paper_agents" / "LaTeX"

DEFAUL_PROJECT_NAME = "project"
"""Default name of the project"""

# Constants for defining .md files and folder names
INPUT_FILES = "input_files"
PLOTS_FOLDER = "plots"
PAPER_FOLDER = "paper"

DESCRIPTION_FILE = "data_description.md"
IDEA_FILE = "idea.md"
METHOD_FILE = "methods.md"
RESULTS_FILE = "results.md"
LITERATURE_FILE = "literature.md"
REFEREE_FILE = "referee.md"

# ERC-specific input files
CALL_INFO_FILE = "erc_call_info.md"
VISION_FILE = "erc_vision.md"
OBJECTIVES_FILE = "erc_objectives.md"
WORK_PACKAGES_FILE = "erc_work_packages.md"
IMPLEMENTATION_FILE = "erc_implementation.md"
IMPACT_FILE = "erc_impact.md"
TEAM_FILE = "erc_team.md"
ETHICS_FILE = "erc_ethics.md"
BUDGET_FILE = "erc_budget.md"
PRIOR_RESULTS_FILE = "erc_prior_results.md"

# ERC-specific folders inside input_files
CALL_DOCS_DIR = "erc_call_docs"
APPLICANT_DOCS_DIR = "erc_applicant_docs"
PRIOR_RESULTS_DOCS_DIR = "erc_prior_results_docs"
