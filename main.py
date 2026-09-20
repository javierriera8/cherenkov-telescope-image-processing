# -------------------------
# ------main.py-------
# This document uses the functions gathered at functions.py in order to test the noise reduction methods presented with different intensities and noise-signal ratios to discover which fits better for each range. Please run this code to see the final results.
# Javier Riera Vidal and Helena Villares Santiago
# IPCV 2025-26 Universitat de Barcelona

#------IMPORTS-----
import matplotlib.pyplot as plt
import numpy as np
import functions as f #our own functions created in functions.py

#we will try our four algorithms with a wide range of intensities, varying from 5 to 55 going on steps of 5
possible_intensities = np.arange(5,55,5)

#and we will be saving our background survival and signal retention for each intensity value
#taitlcut, morpho, kmeans, dbscan
sig_retention = [[],[],[],[]]
back_survival = [[],[],[],[]]


for intensity in possible_intensities:

    plt.figure(f"intensity_{intensity}pe")
    plt.suptitle(f"Intensity {intensity} p.e.")
 
    
    #we generate the clean image, noise, noisy image
    image_clean = f.clean_image(intensity)
    noise = f.noise()
    image = image_clean + noise

    n,m = 2,3

    #we plot the clean image
    plt.subplot(n,m,1)
    plt.title("Clean")
    plt.imshow(image_clean)

    #we plot the noisy image
    plt.subplot(n,m,2)
    plt.title("Noisy")
    plt.imshow(image)

    #we will clean it with tailcut and plot the result
    clean_tailcut = f.tailcut_cleaning(image)
    plt.subplot(n,m,3)
    plt.title("Tail-cut")
    plt.imshow(clean_tailcut)
    sig_retention[0].append(f.size_ret(image_clean, noise, clean_tailcut)[0])
    back_survival[0].append(f.size_ret(image_clean, noise, clean_tailcut)[1])

    #we will clean it with morphology and plot the result
    clean_morpho = f.morphological_cleaning(image)
    plt.subplot(n,m,4)
    plt.title("Morphology")
    plt.imshow(clean_morpho)
    sig_retention[1].append(f.size_ret(image_clean, noise, clean_morpho)[0])
    back_survival[1].append(f.size_ret(image_clean, noise, clean_morpho)[1])

    #we will celan it with kmeans and plot the result
    clean_kmeans = f.kmeans_cleaning(image)
    plt.subplot(n,m,5)
    plt.title("K-Means")
    plt.imshow(clean_kmeans)
    sig_retention[2].append(f.size_ret(image_clean, noise, clean_kmeans)[0])
    back_survival[2].append(f.size_ret(image_clean, noise, clean_kmeans)[1])
    #we will clean it with dbscan and plot the result

    #we have to add the time channel
    time = f.time(image_clean)
    image_time = np.stack((image, time), axis=2)

    #and now use dbscan
    clean_dbscan = f.dbscan_cleaning(image_time)
    plt.subplot(n,m,6)
    plt.title("DBSCAN")
    plt.imshow(clean_dbscan)
    sig_retention[3].append(f.size_ret(image_clean, noise, clean_dbscan)[0])
    back_survival[3].append(f.size_ret(image_clean, noise, clean_dbscan)[1])
    

#now we will plot, for instance, the background survival and signal retention for each intensity and method

plt.figure("signal_retention")
plt.suptitle("Signal retention for different methods and intensities")
plt.xlabel("Intensities (p.e.)")
plt.ylabel("Signal retention")


labels = ["Tail-cut", "Morphology", "K-Means", "DBSCAN"]
for method in range(4):
    plt.plot(possible_intensities, sig_retention[method],label=labels[method])
plt.legend()

plt.figure("background_survival")
plt.suptitle("Background survival for different methods and intensities")
plt.xlabel("Intensities (p.e.)")
plt.ylabel("Background survival")
labels = ["Tail-cut", "Morphology", "K-Means", "DBSCAN"]
line_styles = ['-', '--', '-.', ':']
line_widths = [4, 3, 2, 2] # Grosores distintos para que se asomen por debajo

for method in range(4):
    plt.plot(possible_intensities, back_survival[method], 
             label=labels[method], 
             linestyle=line_styles[method],
             linewidth=line_widths[method],
             alpha=0.8)
plt.legend()

plt.show()