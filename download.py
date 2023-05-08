# In this file, we define download_model
# It runs during container build time to get model weights built into the container

import faster_whisper

def download_model():
    #medium, large-v1, large-v2
    model_name = "large-v2"
    model = faster_whisper.WhisperModel(model_name)

if __name__ == "__main__":
    download_model()