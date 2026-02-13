from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TCON  # For more control

def add_fake_metadata(file_path, title, artist, album, genre):
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

# Example usage after creating files
add_fake_metadata('empty_audio_1.wav', "So Empty", "Empty Man", "Silence", "Lo-Silence")
add_fake_metadata('empty_audio_2.wav', "Hush", "Empty Man", "Silence", "Lo-Silence")
add_fake_metadata('empty_audio_3.wav', "White Noise", "Empty Man", "Silence", "Lo-Silence")
add_fake_metadata('empty_audio_4.wav', "Flatline", "Empty Man", "Silence", "Lo-Silence")
add_fake_metadata('empty_audio_5.wav', "Ambient Night", "Empty Man", "Silence", "Lo-Silence")