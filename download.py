# In this file, we define download_model
# It runs during container build time to get model weights built into the container

import torch
import faster_whisper_local

def download_model():
    #medium, large-v1, large-v2
    model_name = "large-v2"
    model = faster_whisper_local.WhisperModel(model_name)

if __name__ == "__main__":
    download_model()