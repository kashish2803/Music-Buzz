# Standard libraries
import os, sys
from keras import backend as K
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from sklearn.externals import joblib
import keras
from keras import models
import librosa
import numpy as np
import subprocess

print(os.getcwd())
# ArcCloud
from ArcCloud.acrcloud.recognizer import ACRCloudRecognizer
from ArcCloud.acrcloud.recognizer import ACRCloudRecognizeType



# Loading our Scaler and Encoder
scaler = joblib.load('Scaler/scaler.save')
encoder = joblib.load('Scaler/encoder.save')


################### GENRE CLASSIFICATION ##################

# Function to extrat features
def extract_features(songname):
    # Extract Features
    y, sr = librosa.load(songname, mono=True, duration=30)
    chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
    spec_cent = librosa.feature.spectral_centroid(y=y, sr=sr)
    spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
    rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
    zcr = librosa.feature.zero_crossing_rate(y)
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    rmse = librosa.feature.rmse(y=y)
    # Append to a list
    feature_list = f'{np.mean(chroma_stft)} {np.mean(rmse)} {np.mean(spec_cent)} {np.mean(spec_bw)} {np.mean(rolloff)} {np.mean(zcr)}'
    for e in mfcc:
        feature_list += f' {np.mean(e)}'
    # Convert to a numpy array
    feature_array = np.array(list(map(float, feature_list.split(' '))))
    # Reshaping the array to a column vector
    feature_array = feature_array.reshape((1,26))
    feature_array = scaler.transform(feature_array)
    return feature_array

# Function to predict song
def predict_song(songname):
    # Loading our Model
    model = keras.models.load_model('Models/music_classifier.h5')
    feature_array = extract_features(songname)
    predicted_label = model.predict_classes(feature_array)
    predicted_class = encoder.inverse_transform(predicted_label)

    # Clearning the tensorflow session
    K.clear_session()

    return predicted_class



################### BPM Identification ##################

def get_bpm(songname):
    x, sr = librosa.load(songname)
    tempo, beat_times = librosa.beat.beat_track(x, sr=sr)
    return ("%.2f" % tempo)


################### GET IMAGE DATA ######################

from google_images_download import google_images_download

def download_image(artist_name):
    response = google_images_download.googleimagesdownload()
    arguments = {"keywords":artist_name,"limit":1,"print_urls":True}
    paths = response.download(arguments)
    return paths


################### Song Information ##################

def get_song_info(songname):
    # configure the api
    config = {
        'host':'identify-ap-southeast-1.acrcloud.com',
        'access_key':'a60eaf89e7a5977686ad563c6d29682b',
        'access_secret':'7uwt74A9AiJ8dx0Yz8Yp79khegLFHACppDbDsznL',
        'recognize_type': ACRCloudRecognizeType.ACR_OPT_REC_AUDIO,
        'debug':False,
        'timeout':10 # seconds
    }

    # Instantiate Recognizer
    re = ACRCloudRecognizer(config)
    json_data = re.recognize_by_file(songname, 0, 10)

    return json_data
