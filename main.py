from user_taste_spotify import SpotifyTaste
from retriever_recent import RecentUploads
from video_pytube_handler import Video
from metric_analyzer_bpm import RegexBPM
from metric_analyzer_key import LibrosaKey
from converter_ffmpeg import FfmpegWrapper
from getpass import getpass

client_id = '9bf2211d3826492aa72471ec394689e1' #swap for different user
client_secret = getpass("Spotify client secret:")

spotify = SpotifyTaste(client_id, client_secret)
spotify.triggerCallback()
authUrl = input("Auth URL:")
spotify.authenticate(authUrl)

artists = spotify.getSearchTerms()

retriever = RecentUploads()
videoLinks = retriever.search(artists)

converter = FfmpegWrapper()
bpmProcessor = RegexBPM()
keyProcessor = LibrosaKey()

for link in videoLinks:
    videoWrapper = Video(link)
    videoPath = videoWrapper.download('defaultPath')

    if videoPath and videoWrapper.description:
        fileName = converter.convert(videoPath)
        bpm = bpmProcessor(videoWrapper.description)
        key = keyProcessor(videoPath)

        if bpm and key:
            converter.rename(fileName, key, bpm)
