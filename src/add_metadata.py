import os

folder = "Catalog"
folders = [item for item in os.listdir(folder) if os.path.isdir(os.path.join(folder, item))]
for folder in folders:
    files = [item for item in os.listdir(os.path.join('Catalog', folder)) if os.path.isfile(os.path.join('Catalog', folder, item))]
    print(files)
    for file in files:
        if file.endswith('.aif'):
            print(f"Processing {file} in {folder}")
            # Here you would call your metadata function, e.g.:
            # add_metadata(os.path.join('Catalog', folder, file), title, artist, album, genre)
