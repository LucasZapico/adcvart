import os
import mutagen
from mutagen.id3 import ID3, APIC
from mutagen.mp3 import MP3
import argparse

cover = "assets/old-leather-background-with-golden-floral-decoration.png"

directory = 'raw/princessofmars_2203_librivox'

def add_cover_art(directory: str, cover: str) -> None:
# Iterate over all files in the directory
  for entry in os.scandir(directory):
      if entry.is_file() and entry.name.endswith('.mp3'):
          audio = MP3(entry.path, ID3=ID3)

          # Add ID3 tag if it doesn't exist
          try:
              audio.add_tags()
          except mutagen.id3.error:
              pass

          # Open the image file
          with open(cover, 'rb') as albumart:
              audio.tags.add(
                  APIC(
                      encoding=3,  # 3 is for utf-8
                      mime='image/png',  # image/jpeg or image/png
                      type=3,  # 3 is for the cover image
                      desc=u'Cover',
                      data=albumart.read()  # Read and attach the image
                  )
              )
          audio.save()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Add cover art to MP3 files.')
    parser.add_argument('--path', type=str, required=True, help='The directory of MP3 files.')
    parser.add_argument('--cover-img', type=str, required=True, help='The cover art image file.')
    args = parser.parse_args()

    add_cover_art(args.path, args.cover_img)