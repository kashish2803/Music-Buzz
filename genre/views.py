# Standard Libraries
from django.shortcuts import render
from django.http import Http404
from django.core.files.storage import FileSystemStorage
import json
import pdb
from .ml import *

# DIRECTORIES
BASE_DIR = os.getcwd()
MEDIA_DIR = os.path.join(BASE_DIR, 'media')

# Index Page
def index(request):
    context = {}
    return render(request, 'genre/index.html', context)

# Register View
def register(request):
    pass

# Results Page
def predict(request):
    if request.method == 'POST':
        try:
            # Uploading file to MEDIA DATABASE
            uploaded_file = request.FILES['document']
            fs = FileSystemStorage()
            name = fs.save(uploaded_file.name, uploaded_file)
            song_dir = os.path.join(MEDIA_DIR, name)

            # Predict Song Genre/Class
            predicted_class = predict_song(song_dir)

            # Predicting Song TEMPO
            predicted_tempo = get_bpm(song_dir)

            # Recognizing Song name and title
            song_data = get_song_info(song_dir)

            # Loading to JSON
            song_data_json = json.loads(song_data)
            if song_data_json['status']['code'] == 3000:
                title = "NOT FOUND"
                artist = "NOT FOUND"
            else:
                title = song_data_json['metadata']['music'][0]['title']
                artist = song_data_json['metadata']['music'][0]['artists'][0]['name']

            # Getting Artist Image
            os.chdir(os.path.join(BASE_DIR,'genre/static/genre/images'))
            img_path = download_image(artist)
            img_path = img_path[artist][0].split("downloads\\")[1]
            os.chdir(BASE_DIR)

            context = {
            'img_path': img_path,
            'predict_class': predicted_class[0],
            'tempo': predicted_tempo,
            'artist': artist,
            'title': title
            }
        except:
            raise Http404("Could not Process your Request... Please Try Again")
    else:
        context = {}

    return render(request, 'genre/predict.html', context)