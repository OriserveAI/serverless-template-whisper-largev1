from potassium import Potassium, Request, Response
from transformers import pipeline
import torch

app = Potassium("my_app")

# @app.init runs at startup, and initializes the app's context
@app.init
def init():
    model_name = "large-v2"
    model = WhisperModel(model_name)
    
    context = {
        "model": model,
        "hello": "world"
    }

    return context

# @app.handler is an http post handler running for every call
@app.handler("/")
def handler(context: dict, request: Request) -> Response:
    
    prompt = request.json.get("prompt")
    model = context.get("model")
    segments,info = model.transcribe(audio_array, beam_size=5)
    text = []
    for seg in segments:
        text.append(seg['text'])
    
    text = ' '.join(text)

    return Response(
        json = {"outputs": text}, 
        status=200
    )

if __name__ == "__main__":
    app.serve()