from flask import Flask, request, jsonify
from flask_cors import CORS  
# import cors policy
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import SpotifyAPIWrapper

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes and origins

##NEEDS TO BE CHANGES TO TAKE URI AND GET SONG DETAILS
def getSongFeatures():
    file_path = 'Data/Training/Train.csv'

    song_features = pd.read_csv(file_path)
    spotify_wrapper = SpotifyAPIWrapper.SpotifyAPIWrapper()
    test_song_details = {
        'index': [0],
        'name': ['Pound Town 2 (feat. Nicki Minaj & Tay Keith)'],
        'uri': ['6IEXjer2qbXhRLFv99NQQv'],
        'genre': [['trap queen']],
        'artit': ['Sexyy Red']
    }
    test_song_df = pd.DataFrame(test_song_details)

    input_song_features = spotify_wrapper.getFeatures(test_song_df)

    return input_song_features, song_features

def dropNames(input_song_features, song_features):
    input_song_features.drop(columns='name', inplace=True)
    song_features.drop(columns='name', inplace=True)
    return input_song_features, song_features

def model(input_song_features, song_features):
    # Compute cosine similarity between the new song and all songs in the dataset

    similarities = cosine_similarity(input_song_features, song_features)

    # Find the index of the closest song
    closest_song_index = np.argmax(similarities)

    # Find the most similar song from the original dataset
    closest_song = song_features.iloc[closest_song_index]

    return closest_song

@app.route('/predict', methods=['POST'])
def predict():
    inputFeats, songFeats = getSongFeatures()
    inputName, songName = dropNames(inputFeats, songFeats)
    result = model(inputName, songName)
    result = result.to_json()
    return result

if __name__ == '__main__':
    app.run(debug=True)