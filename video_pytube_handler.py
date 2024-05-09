from video import Video
from pytube import YouTube
import os
from urllib.error import HTTPError

class PyTubeHandler(Video):
    
    def __init__(self, link):
        self.video = YouTube(link)
        self.length = self.video.length
        self.getDescription()

    def getDescription(self):
        # from https://github.com/pytube/pytube/issues/1626
        for n in range(6):
            try:
                description = self.video.initial_data["engagementPanels"][n]["engagementPanelSectionListRenderer"]["content"]["structuredDescriptionContentRenderer"]["items"][1]["expandableVideoDescriptionBodyRenderer"]["attributedDescriptionBodyText"]["content"]
                self.description = description
            except:
                continue
        self.description = None
        
    def download(self, path, maxDuration=400):
        try:
            print(self.video.title)
            if self.length > maxDuration:
                #video too long (probably not a beat)
                return

            audio_track = self.video.streams.filter(only_audio=True).first()
            mp4_file = audio_track.download(output_path=path)
            fileName = audio_track.default_filename

            source = path + fileName
            os.rename(source, source.replace(' ', '_'))
            filePath = source.replace(' ','_')

            return filePath

        except HTTPError as err:
            if err.code == 429:
                print('rate limited :/ pls abort')
                return None
            else:
                print('http error', err)
                return None