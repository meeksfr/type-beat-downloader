from video_wrapper import VideoWrapper
from pytube import YouTube
import os
from urllib.error import HTTPError

class PyTubeHandler(VideoWrapper):
    
    def __init__(self, link, bpmProcessor, callback):
        self.video = YouTube(link, on_complete_callback=callback)
        self.length = self.video.length
        self.description = self.getDescription()
        self.bpmProcessor = bpmProcessor

    def download(self, path, maxDuration=400):
        try:
            print(self.video.title)
            if self.length > maxDuration:
                #video too long (probably not a beat)
                return None

            audio_track = self.video.streams.filter(only_audio=True).first()
            
            #getting bpm here in order to work with restricted args of pytube callback function
            bpm = self.bpmProcessor.analyse(self.description)
            if bpm:
                bpm = str(bpm) + "_"
            
            if audio_track:
                audio_track.download(output_path=path, filename_prefix=bpm)
                #also calls callback function

        except HTTPError as err:
            if err.code == 429:
                print('rate limited :/ pls abort')
                return None
            else:
                print('http error', err)
                return None

    def getDescription(self):
        # from https://github.com/pytube/pytube/issues/1626
        for n in range(6):
            try:
                description = self.video.initial_data["engagementPanels"][n]["engagementPanelSectionListRenderer"]["content"]["structuredDescriptionContentRenderer"]["items"][1]["expandableVideoDescriptionBodyRenderer"]["attributedDescriptionBodyText"]["content"]
                return description
            except:
                continue
        return None