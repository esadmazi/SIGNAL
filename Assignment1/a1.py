import librosa
import numpy as np

# Load the audio file
file_path = 'path_to_esad.wav'  # Replace 'path_to_esad.wav' with the actual path to your esad.wav file
audio_data, sr = librosa.load(file_path, sr=None)

# Define the start and end times for each letter
# These values need to be adjusted based on the analysis of the audio file
start_e = 0  # Example: Start time for letter 'E'
end_e = 10000  # Example: End time for letter 'E'

start_s = 15000  # Example: Start time for letter 's'
end_s = 25000  # Example: End time for letter 's'

start_a = 30000  # Example: Start time for letter 'a'
end_a = 40000  # Example: End time for letter 'a'

start_d = 45000  # Example: Start time for letter 'd'
end_d = 55000  # Example: End time for letter 'd'

# Extract segments for each letter
letter_e = audio_data[start_e:end_e]
letter_s = audio_data[start_s:end_s]
letter_a = audio_data[start_a:end_a]
letter_d = audio_data[start_d:end_d]