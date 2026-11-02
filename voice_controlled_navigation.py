import speech_recognition as sr
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import os

print("=== Voice-Controlled 2D Navigation System (SoundDevice Edition) ===")

#Initializes robot starting position on the 2D grid and step counter
robot_x = 0
robot_y = 0
steps = 0

#Audio recording configuration (workaround for hardware audio input limitations)
duration = 4  #Recording duration in seconds
fs = 44100    #Sample rate (in Hz)
print(f"\n🎤 Recording for {duration} seconds... Say 'right', 'left', 'up', or 'down'!")

#Records audio data from microphone into a NumPy array
audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
sd.wait() #Waits until the recording is finished
print("Recording finished! Processing audio...")

#Saves the recorded NumPy array as a temporary WAV file for the speech recognizer
temp_filename = "temp_command.wav"
wav.write(temp_filename, fs, audio_data)

#Initializes the speech recognition engine
recognizer = sr.Recognizer()

#Loads the temporary audio file for processing
with sr.AudioFile(temp_filename) as source:
    audio = recognizer.record(source)

#Performs Speech-to-Text (ASR) using Google's API with error handling
try:
    command = recognizer.recognize_google(audio).lower()
    print(f"You said: '{command}'")
    
except sr.UnknownValueError:
    print("Could not understand the audio. Defaulting to target (3, 4).")
    command = ""
except sr.RequestError as e:
    print(f"Speech service error: {e}. Defaulting to target (3, 4).")
    command = ""

#Clean up: Deletes the temporary audio file to declutter disk space
if os.path.exists(temp_filename): #declutter
    os.remove(temp_filename)

#Intent Parsing: Maps spoken text keywords to target (X, Y) grid coordinates
if "right" in command:
    target_x = robot_x + 3
    target_y = robot_y
elif "up" in command:
    target_x = robot_x
    target_y = robot_y + 4
elif "left" in command:
    target_x = robot_x - 3
    target_y = robot_y
elif "down" in command:
    target_x = robot_x
    target_y = robot_y - 4
    #Fallback default target if command is unrecognized
else:
    target_x = 3
    target_y = 4

print(f"Navigating from ({robot_x}, {robot_y}) to target ({target_x}, {target_y})...")

#Autonomous Navigation Control Loop: Move the agent step-by-step toward the target
while robot_x != target_x or robot_y != target_y:
    steps += 1

#Updates X coordinate step-by-step
    if robot_x < target_x:
        robot_x += 1
    elif robot_x > target_x:
        robot_x -= 1

#Updates Y coordinate step-by-step
    if robot_y < target_y:
        robot_y += 1
    elif robot_y > target_y:
        robot_y -= 1

print(f"Destination reached at ({robot_x}, {robot_y}) in {steps} steps!")