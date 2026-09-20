# Cherenkov Telescope and Image Processing
This repository performs a comparative analysis of different image cleaning processing techniques for Imaging Atmospheric Cherenkov Telescope (IACT) Data. The images are generated and then cleaned by the different methods implemented:
- Tail-cut algorithm.
- Morphological approach
- K-Means Clustering
- DBscan Clustering
Then, two metrics are used to compare the effectiveness of the different techniques.

The code was developed by [Helena Villares](https://github.com/villaresh) and [Javier Riera](https://github.com/javierriera8), in the framework of the IPCV (Image Processing and Computer Vision) course taken at the Bachelor's degree in Physics at the Universitat de Barcelona (UB), during the first half of 2026. 

## Contained Material
The contained material is the following:
- **Main code:** running `main.py` generates the images, applies the methods, calculates the metrics and shows the results.
- **Functions implemented:** includes all the functions used to run `main.py`, including the implementation of the different cleaning techniques.
- **Report:** report of the project. It is highly recommended to read it before running the code. 


## Installation and Usage
To run the code properly, it is highly recommended to set up a virtual environment on the directory of the repository and install the packages requirements with:

`pip install -r requirements.txt`

After this, you can run main.py normally and you will be able to see the figures:

`python main.py`

Please note that the execution will not stop until all of the figures are closed. 