
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from sklearn.model_selection import cross_val_predict
from sklearn import metrics
from sklearn import svm
import pandas_profiling 
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import IPython.display as ipd
import librosa
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
import soundfile as sf
from pydub import AudioSegment
from pydub.playback import play

# Spotify API credentials
client_id = 'ec84de53afe14549a9cb6b02d723bc8f'
client_secret = '84b9a7fe97314ec985068f541d221a0f'

# Set up Spotify API client
client_credentials_manager = SpotifyClientCredentials(client_id='ec84de53afe14549a9cb6b02d723bc8f', client_secret='84b9a7fe97314ec985068f541d221a0f')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Function to extract audio features using Librosa

def extract_audio_features(audio_path):
    audio, sr = librosa.load(audio_path, duration=30)
    # print('audio=======',audio)
    # print('sr=======',sr)
    chroma_stft = librosa.feature.chroma_stft(y=audio, sr=sr)
    mfcc = librosa.feature.mfcc(y=audio, sr=sr)
    features = np.concatenate((chroma_stft.mean(axis=1), mfcc.mean(axis=1)))
    return features
    

# Function to recognize song using audio features
def recognize_song(audio_path, model):
    try:
        features = extract_audio_features(audio_path)
        predicted_label = model.predict([features])[0]
        return label_encoder.inverse_transform([predicted_label])[0]
    except Exception as e:
        print(e)


# Import pandas library
import pandas as pd
  
# initialize list of lists


data = [['./content/Aathma Rama.mp3', 'Brodha V'],['./content/Anhad.mp3', 'Agam Aggarwal'], ['./content/Bajrangbali.mp3', 'Unknown'], ['./content/Bhor Bhai Din.mp3', 'Agam Aggarwal'],
        ['./content/Chale Chalo.mp3', 'A R Rahman'],['./content/Desh Mere Desh.mp3','Sukhvinder Singh'],['./content/Devon ke Dev Mahadev.mp3', 'Akki']]



# Create the pandas DataFrame
song_data = pd.DataFrame(data, columns=['audio_path', 'label'])
  
# print dataframe.
song_data

# Extract audio features from labeled songs
X = []
y = []
for _, row in song_data.iterrows():
    audio_path = row['audio_path']
    label = row['label']
    features = extract_audio_features(audio_path)
    X.append(features)
    y.append(label)

# Encode labels
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Train a k-nearest neighbors classifier
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y_encoded)

# Example usage: recognize a song
audio_path=['./content/Anhad.mp3']


for i in audio_path:
 predicted_artist = recognize_song(i, model)
 #print(f"Song: {i.split('/')[2]} , Predicted Artist: {predicted_artist}")
 print(f"Song: {i.split('/')[2] if len(i.split('/')) > 2 else 'Invalid input format'}, Predicted Artist: {predicted_artist}")



# Play the recognized song
#audio_data, sr = librosa.load(audio_path, duration=30, sr=None)
#ipd.Audio(audio_data, rate=sr)
















