from converter import Converter
import os

class FfmpegWrapper(Converter):
    def __init__():
        pass

    def convert(self, filePath):

        fileWithoutExtension, ext = os.path.splitext(filePath)

        command = f"ffmpeg -i {filePath} {fileWithoutExtension}.mp3"

        os.system(command)
        os.remove(filePath)

        return fileWithoutExtension
    
    def rename(self, fileWithoutExtension, key, bpm, ext=".mp3"):

        dest = fileWithoutExtension + f"---{key}-{bpm}"
        os.rename(fileWithoutExtension + ext, dest + ext)

        return True