import music_tag
from PIL import Image
import io

file_path = r'F:\Documents\GitHub\Audio-Library-ETL-Project\src\Catalog\Ambitious Archive - Forward Sweeper\Ash Director.aif'
f = music_tag.load_file(file_path)

# Print metadata
print(f.raw)  # All tags

# Extract and display album art
art = f['artwork']
if art:
    img = art.first  # Assuming single image
    print(f"Album Art: Width: {img.width}, Height: {img.height}, MIME: {img.pic_type}")
    Image.open(io.BytesIO(img.raw)).show()  # Display
else:
    print("No album art found.")