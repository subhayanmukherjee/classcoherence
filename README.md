# Binary Classification CNN for InSAR Image Coherence

Interferometric Synthetic Aperture Radar (InSAR) imagery based on microwaves reflected off ground targets is becoming increasingly important in remote sensing for ground movement estimation. However, the reflections are contaminated by noise, which distorts the signal's wrapped phase. Demarcation of image regions based on degree of contamination (“coherence”) is an important component of the InSAR processing pipeline. We introduce Convolutional Neural Networks (CNNs) to this problem domain and show their effectiveness in improving coherence-based demarcation and reducing misclassifications in completely incoherent regions through intelligent preprocessing of training data.

Please cite the below [paper](https://doi.org/10.1109/ICSENS.2018.8589742) if you use the code in its original or modified form:

*S. Mukherjee, A. Zimmer, X. Sun, P. Ghuman and I. Cheng, "CNN-Based InSAR Coherence Classification," 2018 IEEE SENSORS, New Delhi, 2018, pp. 1-4.*

## Guidelines

1. This code uses the [PyGCO repo](https://github.com/Borda/pyGCO) which implements a graph cuts based move-making algorithm for optimization in Markov Random Fields.
2. The entire code for generating the training datasets and training our InSAR Coherence Classification CNN is provided in the [train_coh_class.py](https://github.com/subhayanmukherjee/classcoherence/blob/master/train_coh_class.py) script. However, it uses the trained InSAR Denoising CNN from our [cnninsar repo](https://github.com/subhayanmukherjee/cnninsar). Please refer to the relevant guidelines in that repo to train that InSAR Denoising CNN before running any code from this repo.
3. If you want to test the trained InSAR Coherence Classification CNN on a simulated images dataset, please follow the relevant guidelines from our [cnninsar repo](https://github.com/subhayanmukherjee/cnninsar).
