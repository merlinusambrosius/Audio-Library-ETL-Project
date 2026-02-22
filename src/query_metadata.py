import os
import mutagen  

for key, value in mutagen.File('Fantasy Opus No 1.aif').items():
    if key != 'APIC:':
        print(key)
        print(f"{key}: {value}") #contains too much information, so we will write it to a text file instead
    #Write metadata to a text file
    #with open('metadata.txt', 'a') as f:
    #    f.write(f"{key}: {value}\n")
    
'''
audio = mutagen.File('Myrddin\'s Dream - The Triads- Distant Shores - 03 Distant Shores.mp3')

print(f"Title: {audio.get('TIT2')}")
print(f"Artist: {audio.get('TPE1')}")
print(f"Album: {audio.get('TALB')}")
print(f"Year: {audio.get('TDRC')}")
'''