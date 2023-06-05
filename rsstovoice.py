import feedparser
from gtts import gTTS
from pydub import AudioSegment
from pydub.generators import Sine

url = "https://feeds.leparisien.fr/leparisien/rss"
feed = feedparser.parse(url)

fichier = open("test.txt", "w")

for entry in feed.entries:
    # Titre
    title = entry.title
    print(title)
    fichier.write(title)
    fichier.write('\n')

fichier.close()

# Read text file
f = open('test.txt', 'r')
titles = f.readlines()
f.close()

# Create blank audio segment
silence = AudioSegment.silent(duration=1000)

# Create audio segments for titles
title_segments = []
for title in titles:
    tts = gTTS(text=title.strip(), lang='fr', slow=False)
    tts.save("temp.mp3")  # Save the audio file
    title_audio = AudioSegment.from_file("temp.mp3", format="mp3")
    title_segments.append(title_audio)
    title_segments.append(silence)

# Concatenate audio segments
audio = sum(title_segments)

# Save the final audio file
audio.export("cool.mp3", format="mp3")

print("Le fichier audio a été créé avec succès.")
ffplay cool.mp3

