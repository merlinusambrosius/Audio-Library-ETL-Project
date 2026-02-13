# Audio Library Python ETL Project
The purpose of this python project is to create a managed audio library, where audio files will be uploaded and stored.  The library will also enable the user to easily manage metadata by adding, deleting, or copying metadata.  The library will also enable the user to easily search for specific audio files by filtering keywords embedded in metadata.

Parameters of the project:
- The project audio files will be in the following format:
  - .aiff, which is the industry standard for professional asset delivery to music libraries for high quality uncompressed audio, detailed and consistent storage for metadata, portability.
  - 24/48k
  - 2 channel
  - 5 second length
- In keeping with workflow similar to DISCO metadata management
  - Audio files will be created offline on the client side.
  - Uploaded to server with bulk upload process.
  - Metadata will be managed (added, copied, deleted) by the user.  This includes song and artist name, album, album art, keyword descriptors, etc.
-Display of metadata
  - tiered display, depending on view
  - View of all albums, artists, etc. will display limited information relevant to a cursory view:
    - Artist
    - Album
    - Album art
  - Viewing a specific album may list the same, but also:
    - track names
    - length
- Query and filter by name, keywords, lyrics, etc.

Goals include:
- Create a client
- Create a bucket or connect to existing S3 bucket
- Query for contents of bucket (the bucket itself, name, contents by folder), and clean up the output
- Create/upload .wav/.mp3 files to S3 bucket by folder.
- Create, copy, edit, delete metadata on audio files.
- Display metadata in a clean, useful way, including album art Attached PICture (APIC)