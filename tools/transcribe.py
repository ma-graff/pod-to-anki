import whisper
import sys
import os

# Load the model
model = whisper.load_model("turbo")
result = model.transcribe("test_data/fr_CA/mp3/sports.mp3")
print(result["text"])

# Error: UserWarning: FP16 is not supported on CPU; using FP32 instead
# warnings.warn("FP16 is not supported on CPU; using FP32 instead")