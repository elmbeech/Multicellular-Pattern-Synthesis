#!/usr/bin/env python
# coding: utf-8

# ## IslandDemo
# 
# To analysis the island photos, we used the following script which can be used with the provided sample images:

# ![DAPI_mask](http://localhost:8888/files/image_segmentation_clustering/plots/islands/EBICS_ISLAND_D%20-%208_E_D(cropped)/DAPI_mask.png)
# We masked the DAPI to label the location of the cells.

# ![DAPI_segmentation](http://localhost:8888/files/image_segmentation_clustering/plots/islands/EBICS_ISLAND_D%20-%208_E_D(cropped)/DAPI_segmentation.png)
# The DAPI_mask was them used to segment and identify each colony

# ![ECAD_mask](http://localhost:8888/files/image_segmentation_clustering/plots/islands/EBICS_ISLAND_D%20-%208_E_D(cropped)/ECAD_mask.png)
# 
# We used the presence of the molecule CDH1 (which we name ECAD in this script) to label each population of ECAD+ or ECAD- cells. 

# ![ECAD_DAPI_overlap](http://localhost:8888/files/image_segmentation_clustering/plots/islands/EBICS_ISLAND_D%20-%208_E_D(cropped)/DAPI_segmentation_c02.png)
# 
# We then took the identified ECAD_mask that overlaped with the identified colony from the DAPI segmentation.

# ![DAPI peaks](http://localhost:8888/files/image_segmentation_clustering/plots/islands/EBICS_ISLAND_D%20-%208_E_D(cropped)/DAPI_peaks_c02.png)
# 
# The peak fluorescence from the DAPI image within the segmented colony was used to identify the total cells in the entire colony

# ![island DAPI peaks](http://localhost:8888/files/image_segmentation_clustering/plots/bullseye/EBICS_BULLSEYE_A%20-%205_E_D(cropped)/Island_c02r015.png)
# 
# The peak fluorescence from the DAPI image within the segmented islands from the ECAD mask was used to identify the total cells in each island

# The the final outputs of our analysis were written out to two files. The first, "IslandParameters.csv" contains information about each individual cluster of ECAD+ cells that were identified per cell colony, for example the total cells per island, the area of the island, etc. The second file "TotIslandParameters.csv" contains information at the colony level, for example the total islands in a colony, the average size of clusters in that colony, etc. 


get_ipython().system('python3 Masking_islands.py')

