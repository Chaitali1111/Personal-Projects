import flask
import pickle
import numpy as np
from fav import *

app = flask.Flask(__name__)

# model=pickle.load(open('model.pkl','rb'))


@app.route('/')
def hello_world():
    return flask.render_template("singer.html")


# @app.route('/predict',methods=['POST','GET'])
# def predict():
#     int_features=[int(x) for x in flask.request.form.values()]
#     final=[np.array(int_features)]
#     print(int_features)
#     print(final)
#     prediction=model.predict_proba(final)
#     output='{0:.{1}f}'.format(prediction[0][1], 2)

#     if output>str(0.5):
#         return flask.render_template('forest_fire.html', pred='Your Forest is in Danger.\nProbability of fire occuring is {}'.format(output), bhai="kuch karna hain iska ab?")
#     else:
#         return flask.render_template('forest_fire.html', pred='Your Forest is safe.\n Probability of fire occuring is {}'.format(output), bhai="Your Forest is Safe for now")

@app.route('/predict',methods=['POST','GET'])
def predict():
    request_data=flask.request.form.values()
    request_data=[x for x in flask.request.form.values()]
    print('request_data--------------->',request_data)
    print('len request_data--------------->',len(request_data))

    if request_data!='' and len(request_data)>0:
        file_name=request_data[0]
    else:
        file_name=''    

    audio_path=[f'./content/{file_name}']


    for i in audio_path:
        predicted_artist = recognize_song(i, model)
        print(f"Song: {i.split('/')[2]} , Predicted Artist: {predicted_artist}")

        # Play the recognized song
        # audio_data, sr = librosa.load(audio_path, duration=30, sr=None)
        # audio_data, sr = librosa.load('C:/Users/Chaitali/Desktop/Music files/Chale Chalo.mp3', duration=30, sr=None)
        # audio_data, sr = librosa.load('C:/Users/Chaitali/Desktop/Music files/Chale Chalo.mp3')
        # ipd.Audio(audio_data, rate=sr)


    return flask.render_template('singer.html', pred=f'Predicted Singer is: {predicted_artist}',song=file_name,file_name=file_name,predicted_artist=predicted_artist)


if __name__ == '__main__':
    app.run(debug=True)


