import os

def add_metadata(file_path, title, artist, album, genre):
    try:
        audio = EasyID3(file_path)
    except:
        audio = EasyID3()  # Create new if none
        audio.filename = file_path
    audio['title'] = title
    audio['artist'] = artist
    audio['album'] = album
    audio['genre'] = genre

    audio.save()


folder = "Catalog"
folders = [item for item in os.listdir(folder) if os.path.isdir(os.path.join(folder, item))]
for folder in folders:
    files = [item for item in os.listdir(os.path.join('Catalog', folder)) if os.path.isfile(os.path.join('Catalog', folder, item))]
    print(files)
    for file in files:
        if file.endswith('.aif'):
            print(f"Processing {file} in {folder}")
            #prompt the user to enter metadata
            title = input("Enter title: ")
            artist = input("Enter artist: ")
            album = input("Enter album: ")
            genre = input("Enter genre: ")
            #select 

            # Here you would call your metadata function, e.g.:
            # add_metadata(os.path.join('Catalog', folder, file), title, artist, album, genre)
