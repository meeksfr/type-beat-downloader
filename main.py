from user_taste_spotify import SpotifyTaste
from retriever_recent import RecentUploads
from video_pytube_handler import PyTubeHandler
from metric_analyzer_bpm import RegexBPM
from metric_analyzer_key import LibrosaKey
from converter_ffmpeg import FfmpegWrapper
from getpass import getpass
import os

#callback function for using pytube - has restricted parameters
def postProcess(stream, filePath):
    global converter
    global paths

    os.rename(filePath, filePath.replace(' ', '_'))
    filePath = filePath.replace(' ','_')
    
    fileName = converter.convert(filePath)
    paths.append(fileName)

client_id = '9bf2211d3826492aa72471ec394689e1' #swap for different user
client_secret = getpass("Spotify client secret:")

spotify = SpotifyTaste(client_id, client_secret)
spotify.triggerCallback()
authUrl = input("Auth URL:")
spotify.authenticate(authUrl)

artists = spotify.getSearchTerms()

retriever = RecentUploads()
videoLinks = retriever.search(artists)

bpmProcessor = RegexBPM()
keyProcessor = LibrosaKey()
converter = FfmpegWrapper()

paths = []

x = 0
for link in videoLinks:
    try:
        videoWrapper = PyTubeHandler(link, bpmProcessor, postProcess)
        videoWrapper.download('defaultPath/')
        x += 1
        if x == 12:
          break
    except:
        print(f"error w {link}")

for path in paths:
    try:
        fullPath = path + ".mp3"
        key = keyProcessor.analyse(fullPath)
        converter.rename(fullPath, key)
    except:
        print(f"error on {path}")