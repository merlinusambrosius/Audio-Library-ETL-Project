#Verify metadata on audio files
from mutagen.easyid3 import EasyID3

def print_metadata(file_path):
    try:
        audio = EasyID3(file_path)
        print(f"Metadata for {file_path}:")
        for key, value in audio.items():
            print(f"{key}: {value[0]}")
    except Exception as e:
        print(f"Error reading metadata from {file_path}: {e}")

#Read and print metadata from all wave files in the current directory
import os   
for filename in os.listdir('.'):
    if filename.endswith(('.mp3', '.flac', '.m4a', '.wav', '.ogg', '.aac', '.wma', '.aif', '.aiff')):
        print_metadata(filename)