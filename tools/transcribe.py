import whisper
import sys
import os

# Load the model
model = whisper.load_model("turbo") # should use a more energy-efficient model
result = model.transcribe("test_data/fr_CA/mp3/sports.mp3")
print(result["text"])

