import requests

# The URL of the Flask endpoint
url = 'http://127.0.0.1:5000/predict'

# Spotify song URI you want to process
spotify_uri = '2y4ZR0BUAVePljHSsZyIgj'

# Data payload in JSON format
data = {'artist':  "Taylor Swift",
        'song_name': "22"}

# Make the POST request to the Flask endpoint
response = requests.post(url, json=data)

# Check the response status and print the result
if response.status_code == 200:
    print('Song features retrieved successfully:')
    print(response.json())  # Print the JSON response containing the song features
else:
    print('Failed to retrieve song features. Status code:', response.status_code)

