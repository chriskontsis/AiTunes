from flask import Flask, request, jsonify
from flask_cors import CORS  
# import cors policy
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import SpotifyAPIWrapper
import glob

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes and origins

def getSongFeatures(song_uri):
    file_path = 'Data/Training/Train.csv'

    song_features = pd.read_csv(file_path)
    spotify_wrapper = SpotifyAPIWrapper.SpotifyAPIWrapper()
    test_song_details = {
        'index': [0],
        'name': ['###'],
        'uri': song_uri,
        'genre': [['###']],
        'artit': ['###']
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
    return closest_song, closest_song_index

def getSongURI(song_name):
    file_pattern = 'Data/song-data/*.csv' 
    file_list = glob.glob(file_pattern) 
    combined_df = pd.concat((pd.read_csv(file) for file in file_list), ignore_index=True)
    song_data = combined_df[combined_df['name'] == song_name]
    if not song_data.empty:
        return song_data.iloc[0]['uri']
    else:
        return None
    
def getSongName(index, songFeats1):
    print(index)
    print(songFeats1.columns)
    song_name = songFeats1.at[index, 'name']
    return song_name


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    song_uri = data.get('uri')  
    inputFeats, songFeats = getSongFeatures(song_uri)
    songFeats1 = songFeats.copy()
    inputName, songName = dropNames(inputFeats, songFeats)
    result, index = model(inputName, songName)
    #song_name = getSongName(index, songFeats1)
    song_name = songFeats1.at[index, 'name']
    result = result.to_json()
    song_uri = getSongURI(song_name)
    return jsonify(song_uri)

if __name__ == '__main__':
    app.run(debug=True)