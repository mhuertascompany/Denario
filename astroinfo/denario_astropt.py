from denario import Denario
den = Denario()

data_description = r"""
We have a multimodal dataset combining DESI spectroscopy and EUCLID imaging. The data is stored in a HF dataset in this
local folder: /n03data/huertas/desi_euclid/msiudek___astro_pt_euclid_desi_dataset. we also have a euclid only imaging dataset avaialble 
here: /n03data/huertas/desi_euclid/msiudek___astro_pt_euclid_training_dataset.  
"""

den.set_data_description(data_description = data_description)


den.set_idea(idea=r"""
Identify rare or unusual astronomical objects by leveraging the multimodal dataset combining DESI 
spectroscopy and Euclid imaging data. The idea is to test whether multimodal data leads to more interesting
anomalies. The plan is to use the astroPT model (https://github.com/Smith42/astroPT and aleady cloned in /n03data/huertas/python/astroPT) to obtain mutlimodal embeddings
and then perform anomaly detection on those embeddings. For the anomaly detection we will train a density estimator such
as a normalzing flow on the the embedding space and identify objects with low likelihood. The process will be also done
with only Euclid images and we will compare the anomalies. The datasest need to be downloaded to 
""")

den.get_method(mode='cmbagent')

den.get_results()

