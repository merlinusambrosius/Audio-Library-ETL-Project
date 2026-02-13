import wave
import struct
import os

def create_empty_wav(file_path, duration_seconds=1, sample_rate=44100):
    """Create an empty WAV audio file of specified duration."""
    num_channels = 1
    sample_width = 2  # bytes per sample
    num_frames = duration_seconds * sample_rate

    with wave.open(file_path, 'w') as wav_file:
        wav_file.setnchannels(num_channels)
        wav_file.setsampwidth(sample_width)
        wav_file.setframerate(sample_rate)
        wav_file.setnframes(num_frames)

        # Write silent frames (zeros)
        silent_frame = struct.pack('<h', 0)  # 16-bit PCM silence
        for _ in range(num_frames):
            wav_file.writeframes(silent_frame)
#Make 5 dummy files
for i in range(5):
    create_empty_wav(f'empty_audio_{i+1}.wav', duration_seconds=2)