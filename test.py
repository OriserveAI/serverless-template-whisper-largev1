# This file is used to verify your http server acts as expected
# Run it with `python3 test.py``

import requests
import librosa

y,sr = librosa.load('test.mp3')
# with open(f'test.mp3','rb') as file:
#     mp3bytes = BytesIO(file.read())
# mp3 = base64.b64encode(mp3bytes.getvalue()).decode("ISO-8859-1")

model_payload = {"audio_array":y}

res = requests.post("http://localhost:8000/",json=model_payload)

print(res.text)

