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

def getSongUriFromData(data):
    track_name = data.get('song_name')
    artist_name = data.get('artist')

    spotify_wrapper = SpotifyAPIWrapper.SpotifyAPIWrapper()
    results = spotify_wrapper.spotify.search(q=f"track:{track_name} artist:{artist_name}", type='track')
    track = results['tracks']['items'][0]
    track_uri = track['id']
    return track_uri


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        if not data or 'song_name' not in data or 'artist' not in data:
            return jsonify({'error': 'No URI provided'}), 400

        song_uri = getSongUriFromData(data)
        print(song_uri)
        
        if not song_uri:
            return jsonify({'error': 'URI is empty'}), 400

        inputFeats, songFeats = getSongFeatures(song_uri)
        if inputFeats.empty or songFeats.empty:
            return jsonify({'error': 'Song features not found'}), 404

        songFeats1 = songFeats.copy()
        inputName, songName = dropNames(inputFeats, songFeats)
        result, index = model(inputName, songName)

        if result is None or index is None:
            return jsonify({'error': 'Song matching failed'}), 500

        song_name = songFeats1.at[index, 'name']
        song_uri = getSongURI(song_name)
        if not song_uri:
            return jsonify({'error': 'Song URI not found'}), 404

        result = result.to_json()

        # Create the response and add CORS headers
        response = jsonify({'song_uri': song_uri, 'details': result})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    except Exception as e:
        # Log the exception to the server's log
        app.logger.error(f'Error in predict: {e}')
        return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    app.run(debug=True)