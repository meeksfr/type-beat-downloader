from .converter import Converter
import os

class FfmpegWrapper(Converter):
    def __init__(self):
        pass

    def convert(self, filePath):

        fileWithoutExtension, ext = os.path.splitext(filePath)
        
        command = f"ffmpeg -i {filePath} {fileWithoutExtension}.mp3"

        os.system(command)
        os.remove(filePath)

        return fileWithoutExtension
    
    def rename(self, filepath, key):
        
        directory, filename = os.path.split(filepath)
        name, extension = os.path.splitext(filename)
        
        newName = f"{directory}/{key}_{name}{extension}"
        
        os.rename(filepath, newName)
