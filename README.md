
# Complete Music Information Retrieval System
## Abstract

The automatic classification system to the most widely used music dataset; the GTZAN Music Genre Dataset was implemented. The system was implemented with a set of low-level features and several supervised classification methods.

## Introduction

Music Genre Classification to the most widely used dataset; GTZAN was implemented with a set of several low-level feature extraction and machine learning methods. 10 features are extracted from audio files and classified with 3 classifiers, k-NN, multilayer perceptron and convolutional neural network.

## Major Libraries Used:-
1. Tensorflow (Along with KERAS API) - Used for building the classifier
2. Librosa - Used for Audio Preprocessing and Feature extraction
3. ACRCloud - Audio Fingerprinting Database API by AcrCloud
4. Google Search API - For getting the images for the predicted result

## The Dataset
The GTZAN Music Genre Dataset, which is a collection of 1000 songs in 10 genres, is the most widely used dataset. 

Although many studies have been conducted using GTZAN, several faults have been pointed out. Sturm[1], for example, identified and analysed the contents of GTZAN and provided a catalogue of its faults. As it is the most used dataset, however, the system performance of MGC in this project should first be evaluated with GTZAN in order to compare against other systems used in other studies.

Details on the GTZAN Music Genre Dataset are presented in the table below. In GTZAN, each song is recorded at a sampling rate of 22.05 kHz and mono 16-bit audio files in .wav format.

## Pre-processing

First, the input signal is sent to a high pass filter. The pre-emphasis increases the relative energy of the high-frequency spectrum 
The importance of pre-emphasis is often noted in speech processing, especially if the extracted features are MFCC, and 0.97 is usually chosen as the pre-emphasis coefficient. The pre-emphasis compensates for the high-frequency formants which were suppressed during the sound production by instruments or the human voice.

Second, the emphasised input audio signal is segmented into analysis windows of 46ms length with an overlap of half size of an analysis window. The number of samples in an analysis window is usually the equal power of two to facilitate the use of FFT. For the system, 2048 samples are framed for an analysis window.

Finally, the framed signals are inputted into a matrix and the silence removal is applied to each analysis frame. As the silence in the audio signal can affect the FFT computation in the reproduction of the system produced by Chang et al. and Sturm, an appropriate silence removal method was considered. For each analysis frame, the number of non-zero samples are counted and compared to the number of zeros. The silence removal only validates frames which have non-zero samples that are more than the half of an analysis window (1024). Hence, frames containing zeros more than 1024 samples are invalidated.

## Feature Extraction
Ten types of low-level feature—six short-term and four long-term features—noted are extracted from the analysis windows and texture windows, respectively. In order to characterise the temporal evaluation of the audio signal, long-term features are computed by aggregating the short-term features.

Over a texture window which consists of 64 analysis windows, short-term features are integrated with mean values.
Also, extracted features from audio files were plotted in a figure like below. These featuremaps are saved in a drive (See installation).

## Classifier
Multilayer Perceptron

The multilayer Perceptron to this project consists of 3 layers with relu function. The training data is splitted into 10% for the validation and 90% for the training. It loads the data from "Data.csv".

## Results
Accuracy: 74.6%

### Dependency
Python 3.6.5

numpy  version 1.14.2

pandas version 0.22.0

scipy  version 1.0.1

keras  version 2.1.3

PIL    version 5.0.0

librosa verion 0.6.3


## References
[1] B. L.Sturm, "The GTZAN dataset: Its contents, its faults, their effects on evaluation, and its
future use," arXiv preprint arXiv:1306.1461, 2013.

[2] E.Loweimi, S. M. Ahadi, T. Drugman and S. Loveymi, "On the importance of pre-emphasis
and window shape in phase-based speech recognition," in International Conference on
Nonlinear Speech Processing(pp. 160-167). Springer, Berlin, Heidelberg, June, 2013.

[3] K. K. Chang, J. S. R. Jang and C. S. Iliopoulos, "Music Genre Classification via Compressive
Sampling," in ISMIR, pp. 387-392, August, 2010.
E), 2013 IEEE International Conference on (pp. 1-6). IEEE, July, 2013.


## Author
Kashish Nagpal
