import webbrowser
import tempfile
import os
import base64
from mutagen.aiff import AIFF
from mutagen.id3 import APIC

# ←←← CHANGE THIS TO YOUR FILE (or make it a function later)
file_path = r'F:\Documents\GitHub\Audio-Library-ETL-Project\src\Catalog\Ambitious Archive - Forward Sweeper\Ash Director.aif'

audio = AIFF(file_path)

# Basic info + native metadata
info = audio.info
metadata = {
    "Filename": os.path.basename(file_path),
    "Title": "Unknown",
    "Artist": "Unknown",
    "Duration": f"{info.length:.2f} seconds",
    "Sample Rate": f"{info.sample_rate:,} Hz",
    "Channels": info.channels,
    "Bit Depth": getattr(info, 'bits_per_sample', 'N/A'),
    "Bitrate": f"{info.bitrate // 1000 if info.bitrate else 'N/A'} kbps",
}

# Title / Artist from native chunks
if 'NAME' in audio and audio['NAME']:
    metadata["Title"] = getattr(audio['NAME'][0], 'text', str(audio['NAME'][0]))
if 'AUTH' in audio and audio['AUTH']:
    metadata["Artist"] = getattr(audio['AUTH'][0], 'text', str(audio['AUTH'][0]))

# Extract album art (handles your direct APIC chunk + standard ID3)
image_bytes = None
image_mime = "image/jpeg"

print("\nExtracting metadata & album art...")

for key in list(audio.keys()):
    if key == 'APIC':
        try:
            chunk = audio[key]
            raw = chunk.read() if hasattr(chunk, 'read') else bytes(chunk)
            pic = APIC.parse(raw)
            image_bytes = pic.data
            image_mime = pic.mime or image_mime
            print(f"✅ Album art found (direct APIC chunk – {image_mime})")
        except Exception as e:
            print(f"APIC parse failed: {e} – trying raw bytes")
            try:
                image_bytes = raw
                print("✅ Album art used as raw image bytes")
            except:
                pass
    elif key == 'ID3 ':
        for pic in audio[key].getall('APIC'):
            image_bytes = pic.data
            image_mime = pic.mime or image_mime
            print(f"✅ Album art found inside ID3 chunk ({image_mime})")
            break

# Build the beautiful HTML page
if image_bytes:
    b64 = base64.b64encode(image_bytes).decode('utf-8')
    art_html = f'<img src="data:{image_mime};base64,{b64}" class="w-full rounded-3xl shadow-2xl" alt="Album Art">'
else:
    art_html = '<div class="w-full aspect-square bg-zinc-800 rounded-3xl flex items-center justify-center text-zinc-500 text-xl">No album art</div>'

rows_html = ''.join(
    f'<div class="flex justify-between py-4 border-b border-zinc-700 last:border-none">'
    f'<span class="text-zinc-400">{k}</span>'
    f'<span class="font-medium text-white">{v}</span></div>'
    for k, v in metadata.items()
)

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{metadata["Title"]} — Audio Metadata</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-zinc-950 text-zinc-200 min-h-screen py-12">
    <div class="max-w-5xl mx-auto px-6">
        <div class="bg-zinc-900 rounded-3xl shadow-2xl overflow-hidden">
            <!-- Header -->
            <div class="bg-gradient-to-br from-violet-600 via-fuchsia-600 to-pink-600 p-12">
                <h1 class="text-5xl font-bold tracking-tight">{metadata["Title"]}</h1>
                <p class="text-2xl text-white/90 mt-2">{metadata["Artist"]}</p>
            </div>

            <div class="grid md:grid-cols-12 gap-12 p-12">
                <!-- Album Art -->
                <div class="md:col-span-5 flex justify-center">
                    {art_html}
                </div>

                <!-- Metadata -->
                <div class="md:col-span-7">
                    <h2 class="text-3xl font-semibold mb-6 text-emerald-400">Track Details</h2>
                    <div class="bg-zinc-800/60 rounded-2xl p-8 text-lg">
                        {rows_html}
                    </div>
                </div>
            </div>
        </div>

        <p class="text-center text-zinc-500 text-sm mt-8">Full path: {file_path}</p>
    </div>
</body>
</html>'''

# Save to a temporary file and open in the default browser
with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False, encoding='utf-8') as f:
    f.write(html)
    html_path = f.name

print(f"\n✅ Done! Opening nice browser view...")
webbrowser.open('file://' + os.path.abspath(html_path))