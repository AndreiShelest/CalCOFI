## Machine Learning project
authors: Bracha Zofia, Shelest Andrei
University of Warsaw

# CalCOFI 
The CalCOFI data set represents the longest (1949-present) and most complete (more than 50,000 sampling stations) time series of oceanographic and larval fish data in the world. It includes abundance data on the larvae of over 250 species of fish; larval length frequency data and egg abundance data on key commercial species; and oceanographic and plankton data. The physical, chemical, and biological data collected at regular time and space intervals quickly became valuable for documenting climatic cycles in the California Current and a range of biological responses to them. CalCOFI research drew world attention to the biological response to the dramatic Pacific-warming event in 1957-58 and introduced the term “El Niño” into the scientific literature.

The California Cooperative Oceanic Fisheries Investigations (CalCOFI) are a unique partnership of the California Department of Fish & Wildlife, NOAA Fisheries Service and Scripps Institution of Oceanography. The organization was formed in 1949 to study the ecological aspects of the sardine population collapse off California. Today our focus has shifted to the study of the marine environment off the coast of California, the management of its living resources, and monitoring the indicators of El Nino and climate change. CalCOFI conducts quarterly cruises off southern & central California, collecting a suite of hydrographic and biological data on station and underway. Data collected at depths down to 500 m include: temperature, salinity, oxygen, phosphate, silicate, nitrate and nitrite, chlorophyll, transmissometer, PAR, C14 primary productivity, phytoplankton biodiversity, zooplankton biomass, and zooplankton biodiversity.

# The dataset

The dataset consist of two datasets: bottle (contains oceanographic data) and cast (conatins information about sampling stations such as geolocational data).

# The purpose of the project
We want to predict water tempreture.

# Technical details

1. The dataset is quite large, therefore is rejected by github by default. You can download the starting bottle and cast .csv files from kaggle https://www.kaggle.com/datasets/sohier/calcofi/data or use the Google Drive access to which is provided. The files should follow the structure (view from the root folder):

    ./data/bottle/bottle.csv
    ./data/cast/cast.csv

2. The project was mainly developed under conda, therefore requirements.txt file is specific to conda.

3. The notebooks should be run in order 1 to 6, then 7-11 can be executed independendly, and the 12th is the last to run.
