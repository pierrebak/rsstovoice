Rsstovoice.py
By Pierre BaK

A python script to retrieve  rss feeds and convert them to MP3 (based on Gtts by Google). 


This script retrieve an rss feed, display it in the terminal and generates a mp3 file in the same directory.

Needed
------

Make sure you are using at least Python 3.7.

Install Ffmpeg.

Linux:

'sudo apt-get install ffmpeg'

MacOS:

'brew install ffmpeg'

Python libraries:

-Feedparser

'pip3 install feedparser'

-Gtts

'pip3 install gtts'


-Pydub

'pip 3 install pydub'

Running the script 
------------------

'python 3 rsstovoice.py'

Playing the generated mp3 file
------------------------------

You'll find the mp3 file generated in the same directory of the script.
It is called cool.mp3

'ffplay cool.mp3'

(Feel free to add this line at the end of the script if you want to listen to the generated file directly.)





