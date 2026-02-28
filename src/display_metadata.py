from mutagen.aiff import AIFF
from PIL import Image
import io

# Use raw string for the path to avoid escape warnings
file_path = r'F:\Documents\GitHub\Audio-Library-ETL-Project\src\Catalog\Ambitious Archive - Forward Sweeper\Ash Director.aif'

# Load the AIFF file
audio = AIFF(file_path)

# Display basic AIFF audio info
print("Duration (seconds):", audio.info.length)
print("Sample Rate (Hz):", audio.info.sample_rate)
print("Channels:", audio.info.channels)
print("Bits per Sample:", audio.info.bits_per_sample)
print("Bitrate (bps):", audio.info.bitrate)
#print("Compression Type:", audio.info.compression)

# Display native AIFF metadata chunks if present
print("\nNative AIFF Metadata:")
for key in audio:
    if key in ['NAME', 'AUTH', '(c) ', 'ANNO']:  # Common metadata chunks
        print(f"{key}: {audio[key].text}")
    else:
        print(f"{key}: {audio[key]}")  # Other chunks

# Check for embedded ID3 tags (including album art)
id3 = audio.get('ID3 ', None)
if id3:
    print("\nEmbedded ID3 Metadata:")
    print(id3.pprint())
    
    # Extract and display album art from ID3
    apic_frames = id3.getall('APIC')
    if apic_frames:
        for i, pic in enumerate(apic_frames):
            #print(f"Album Art {i+1}: MIME Type: {pic.mime}, Description: {pic.desc}")
            img = Image.open(io.BytesIO(pic.data))
            img.show()  # Opens in default image viewer
            # Optionally save: img.save(f'album_art_{i+1}.jpg')
    else:
        print("No album art found in ID3 tags.")
else:
    print("\nNo embedded ID3 tags found in the file.")