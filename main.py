import librosa
import tensorflow as tf
import numpy as np
from flask import Flask,jsonify,request
import io
import soundfile as sf

def predict(recordingFileBytes):
    data,samplerate = sf.read(recordingFileBytes)
    print(data)
    print(samplerate)
    # model = tf.keras.models.load_model("model_0/")
    # y, sr = librosa.load(recording, duration=3)
    # print(sr)
    # mfcc = librosa.feature.melspectrogram(y=y) # consider mfcc the best from your audio, the best that your audio is representing.
    # mfcc_log_mel = librosa.power_to_db(mfcc, ref=np.max)
    # mfcc_delta = librosa.feature.delta(mfcc)
    # mfcc_delta2 = librosa.feature.delta(mfcc, order=2)
    return


def convertAudioToImage():
    pass

app = Flask(__name__)
@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        print("in request...")
        recordingFile = request.files.get('recording')

        if recordingFile is not None and recordingFile.filename == "":
            return jsonify({"error":"no recording file provided"})

        try:
            if recordingFile is not None:
                fileBytes = io.BytesIO(recordingFile.read())
                sf.read(fileBytes)
                #predict(fileBytes)
                return "200 OK"
        except Exception as e:
            return jsonify({"error" : str(e)})
    return "Could not start operation"

if __name__ == '__main__':
    app.run(port=8081)
