import os
from mutagen.aiff import AIFF
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TCON, APIC

# Define global variables for metadata
dir = 'Catalog'
artist = ''
album = ''
genre = ''

# Function to add metadata to AIFF files, including cover art
def add_metadata(file_path, title, artist, album, genre, cover_image_path):
    audio = AIFF(file_path)
    if audio.tags is None:
        audio.add_tags()
    audio.tags.add(TIT2(encoding=3, text=title))
    audio.tags.add(TPE1(encoding=3, text=artist))
    audio.tags.add(TALB(encoding=3, text=album))
    audio.tags.add(TCON(encoding=3, text=genre))
    if cover_image_path and os.path.exists(cover_image_path):
        with open(cover_image_path, 'rb') as f:
            image_data = f.read()
        audio.tags.add(APIC(encoding=3, mime='image/jpeg', type=3, desc='Cover', data=image_data))
    audio.save()
    print(f"Metadata added to {file_path}")

# Create folders list
folders = [item for item in os.listdir(dir) if os.path.isdir(os.path.join(dir, item))]

# Extract artist and album from folder names
# Naming convention: Artist - Album
for folder_name in folders:
    parts = folder_name.split(' - ')
    if len(parts) == 2:
        artist = parts[0].strip()
        album = parts[1].strip()
        print(f"Artist: {artist}, Album: {album}")
    else:
        print(f"Folder '{folder_name}' does not match the expected format 'Artist - Album'. Skipping.")
        continue  # Skip to next folder
    
    # Enter the genre
    genre = input(f"Enter genre for '{artist} - {album}': ")
    
    # Find cover image first (assuming one .jpg per folder)
    cover_image_path = None
    for item in os.listdir(os.path.join(dir, folder_name)):
        if item.endswith('.jpg'):
            cover_image_path = os.path.join(dir, folder_name, item)
            print(f"Found cover image: {cover_image_path}")
            break  # Stop after finding the first one
    
    # Process audio files
    for item in os.listdir(os.path.join(dir, folder_name)):
        if item.endswith('.aif'):
            file_path = os.path.join(dir, folder_name, item)
            title = os.path.splitext(item)[0]  # Strip extension for title
            print(f"Processing file: {item}")
            add_metadata(file_path, title, artist, album, genre, cover_image_path)