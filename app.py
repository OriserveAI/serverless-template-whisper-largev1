import faster_whisper_local

# Init is ran on server startup
# Load your model to GPU as a global variable here using the variable name "model"
def init():
    global model
    #medium, large-v1, large-v2
    model_name = "large-v2"
    model = faster_whisper_local.WhisperModel(model_name)

# Inference is ran for every server call
# Reference your preloaded global model variable here.
def inference(model_inputs:dict) -> dict:
    global model

    # Parse out your arguments
    audio_array = model_inputs.get('audio_array', None)
    if audio_array == None:
        return {'message': "No input provided"}
    
    # Run the model
    result = model.transcribe(audio_array, beam_size=5)
    output = {"text":result["text"]}
    # os.remove("input.mp3")
    # Return the results as a dictionary
    return output
