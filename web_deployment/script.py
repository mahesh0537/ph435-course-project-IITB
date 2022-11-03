import numpy as np
from flask import Flask, request, jsonify
import torch
import whisper
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
sr = 16000
cs = 30
print(DEVICE)

print('Loding model...')
model = whisper.load_model("base")
options = whisper.DecodingOptions(language="en", without_timestamps=True, fp16 = False)
print('model loaded')
app = Flask(__name__)
@app.route('/api',methods=['GET','POST'])
def predict():
    audio_data = request.files['audio'].read()
    audio_data = np.frombuffer(audio_data, np.int16).flatten().astype(np.float32) / 32768.0
    audio = []
    for i in range(0, int(audio_data.shape[0] / (sr * cs))+1):
        if (i+1) * sr * cs > audio_data.shape[0]:
            audio.append(whisper.log_mel_spectrogram(whisper.pad_or_trim(audio_data[i*sr*cs:(i+1)*sr*cs])))
        else:
            audio.append(whisper.log_mel_spectrogram(whisper.pad_or_trim(audio_data[i*sr*cs:-1])))
    audio = torch.stack(audio).to(DEVICE)
    text = model.decode(audio, options)
    text = ''.join(i.text for i in text)
    return jsonify(text)



if __name__ == '__main__':
    app.run(port=5000, debug=True, host="0.0.0.0")