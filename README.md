# Binary Classification CNN for InSAR Image Coherence

Interferometric Synthetic Aperture Radar (InSAR) imagery based on microwaves reflected off ground targets is becoming increasingly important in remote sensing for ground movement estimation. However, the reflections are contaminated by noise, which distorts the signal's wrapped phase. Demarcation of image regions based on degree of contamination (“coherence”) is an important component of the InSAR processing pipeline. We introduce Convolutional Neural Networks (CNNs) to this problem domain and show their effectiveness in improving coherence-based demarcation and reducing misclassifications in completely incoherent regions through intelligent preprocessing of training data.

Please cite the below [paper](https://doi.org/10.1109/ICSENS.2018.8589742) if you use the code in its original or modified form:

*S. Mukherjee, A. Zimmer, X. Sun, P. Ghuman and I. Cheng, "CNN-Based InSAR Coherence Classification," 2018 IEEE SENSORS, New Delhi, 2018, pp. 1-4.*

## Guidelines

1. The entire code for generating the training datasets and training the models is provided in [train_coh.py](https://github.com/subhayanmukherjee/cnninsar/blob/master/train_coh.py).
2. If you want to test the trained model on a simulated images dataset, you can use [buildset_noisy_sim.py](https://github.com/subhayanmukherjee/cnninsar/blob/master/buildset_noisy_sim.py), but you need to first download download the [simulator](https://github.com/Lucklyric/InSAR-Simulator) (master branch) and place it in the same folder as other codes.
