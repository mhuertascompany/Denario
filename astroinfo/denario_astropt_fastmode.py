from denario import Denario
from denario import Journal

den = Denario(project_dir="/n03data/huertas/python/Denario/astroinfo/project_fastmode")

data_description = r"""
We have a multimodal dataset combining DESI spectroscopy and EUCLID imaging. The data is stored in a HuggingFace dataset in this
local folder:/n03data/huertas/desi_euclid/msiudek___astro_pt_euclid_desi_dataset/default/0.0.0/f01ad07862bebd37408df02a0a38431bbdc7fad9. 
The keywords were are going to use are ['VIS_image', 'NISP_Y_image', 'NISP_J_image', 'NISP_H_image'] for images and ['spectrum'] for spectra.
There is no other metadata available - only data. The spectra are all rest-framed and calibrated. The images are properly reduced and centered around objects.
the dataset contains both images and corresponding spectrum, no need to cross-match.
"""

den.set_data_description(data_description = data_description)

den.set_idea(idea=r"""
Identify rare or unusual astronomical objects by leveraging the multimodal dataset combining DESI 
spectroscopy and Euclid imaging data. The idea is to test whether multimodal data leads to more interesting
anomalies than only images. Use torch, NOT Tensorflow. Do not install any new package.             
""")

# Generate a research idea from the input text
#den.get_idea_fast(llm='gemini-2.5-flash', verbose=False)

# Check if idea is novel or not
#den.check_idea(llm='gemini-2.5-flash')

# Generate a research plan to carry out the idea
#den.get_method_fast(llm="gemini-2.5-pro", verbose=False)

# Follow the research plan, write and execute code, make plots, and summarize the results
#den.get_results(engineer_model='gemini-2.5-pro', researcher_model='gemini-2.5-pro')
# Follow the research plan, write and execute code, make plots, and summarize the results
#den.get_results(engineer_model='gemini-2.5-pro',
        #researcher_model='gemini-2.5-pro',
        #restart_at_step=1)

# Write a paper with [APS (Physical Review Journals)](https://journals.aps.org/) style
den.get_paper(journal=Journal.AAS, llm='gemini-2.5-flash', add_citations=False)