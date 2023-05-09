from flask import Flask,request
from faster_whisper import WhisperModel

app = Flask(__name__)

# Init is ran on server startup
# Load your model to GPU as a global variable here using the variable name "model"
#def init():
model_name = "large-v2"
model = WhisperModel(model_name)
# global model
#medium, large-v1, large-v2


# Inference is ran for every server call
# Reference your preloaded global model variable here.

@app.route('/infer')
def inference():
    global model
    data = request.get_json(force=True)
    # Parse out your arguments
    audio_array = data['audio_array']
    # audio_array = model_inputs.get('audio_array', None)
    if audio_array == None:
        return {'message': "No input provided"}
    
    # Run the model
    segments,info = model.transcribe(audio_array, beam_size=5)
    text = []
    for seg in segments:
        text.append(seg['text'])
    
    text = ' '.join(text)
    
    output = {"text":text}
    # os.remove("input.mp3")
    # Return the results as a dictionary
    return output

if __name__=='__main__':
    app.run()