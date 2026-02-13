#Create empty .aif files using torchaudio
import os
import torchaudio
import torch
import randomname
#Parameters
sample_rate = 44100
duration_seconds = 5
num_channels = 2
bits_per_sample = 24  # Specify the bit depth (e.g., 16, 24, 32)
def create_empty_aif(file_path, sample_rate, num_channels, bits_per_sample):
    # Create an empty waveform with zeros
    duration_samples = int(sample_rate * duration_seconds)
    waveform = torch.zeros(num_channels, duration_samples)
    # Save the empty waveform as an .aif file
    torchaudio.save(file_path, waveform, sample_rate, bits_per_sample=bits_per_sample)

for i in range(9): #change to number of folders you want to create

    # Generate folder name as "Band - Album"
    band_name = randomname.get_name().replace('-', ' ').title()
    album_name = randomname.get_name().replace('-', ' ').title()
    subfolder_name = f"{band_name} - {album_name}"

    #Set ouptut directory inside the existing "Catalog" folder
    output_directory = os.path.join("Catalog", subfolder_name)

    os.makedirs(output_directory, exist_ok=True)

    for i in range(10):
        file_name = randomname.get_name().replace('-', ' ').title()
        file_path = os.path.join(output_directory, f"{file_name}.aif")
        create_empty_aif(file_path, sample_rate, num_channels, bits_per_sample)

    print(f"Created 10 empty .aif files in directory: {output_directory}")
