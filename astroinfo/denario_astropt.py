from denario import Denario
den = Denario(project_dir="/n03data/huertas/python/Denario/astroinfo/project")

data_description = r"""
We have a multimodal dataset combining DESI spectroscopy and EUCLID imaging. The data is stored in a HF dataset in this
local folder:/n03data/huertas/desi_euclid/msiudek___astro_pt_euclid_desi_dataset/default/0.0.0/f01ad07862bebd37408df02a0a38431bbdc7fad9]$ pwd
/n03data/huertas/desi_euclid/msiudek___astro_pt_euclid_desi_dataset/default/0.0.0/f01ad07862bebd37408df02a0a38431bbdc7fad9. 
The keywords were are going to use are ['VIS_image', 'NISP_Y_image', 'NISP_J_image', 'NISP_H_image'] for images and ['spectrum'] for spectra.
"""

den.set_data_description(data_description = data_description)


den.set_idea(idea=r"""
Identify rare or unusual astronomical objects by leveraging the multimodal dataset combining DESI 
spectroscopy and Euclid imaging data. The idea is to test whether multimodal data leads to more interesting
anomalies. The plan is to use the astroPT model (cloned in /n03data/huertas/python/astroPT) to obtain mutlimodal embeddings
and then perform anomaly detection on those embeddings. We will start with the first part of the project first: obtain multimodal embeddings with astroPT and store them safely. We will worry later about anomalies.
IMPORTANT: We will have to train a mulitmodal model from scratch, so you will have to go to the astroPT repo, read the code and understand how to do it. There's a script called scripts/train_multimodal.py in the repo. USE IT and ADAPT IT.
Nomally, the python environemnt is all set up. Use the packages imported there - do not invent new pakages / imports which will fail.
We also have a checkpoint stored here: /n03data/huertas/python/models/astroPT/euclid_Q1/ckpt.pt of a model trained on only Eulcid images, that we can perhaps use for 1. obtaining embeddings on images only for comparison later 
and 2. starting point for the multimodal training. DO NOT INSTALL NEW PYTHON PACKAGES.             
""")

#den.set_idea(idea=r"""
#Identify rare or unusual astronomical objects by leveraging the multimodal dataset combining DESI 
#spectroscopy and Euclid imaging data. The idea is to test whether multimodal data leads to more interesting
#anomalies. The plan is to use the astroPT model (https://github.com/Smith42/astroPT and aleady cloned in /n03data/huertas/python/astroPT) to obtain mutlimodal embeddings
#and then perform anomaly detection on those embeddings. For the anomaly detection we will train a density estimator such
#as a normalzing flow on the the embedding space and identify objects with low likelihood. The process will be also done
#with only Euclid images and we will compare the anomalies. The datasest need to be downloaded to 
#""")

den.get_method(mode='cmbagent')

den.get_results(max_n_steps=3)

