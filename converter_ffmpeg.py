from converter import Converter
import os

class FfmpegWrapper(Converter):
    def __init__(self):
        pass

    def convert(self, filePath):

        fileWithoutExtension, ext = os.path.splitext(filePath)

        print("a:", fileWithoutExtension)
        print("b", ext)
        print("c", filePath)

        command = f"ffmpeg -i {filePath} {fileWithoutExtension}.mp3"

        os.system(command)
        os.remove(filePath)

        return fileWithoutExtension
    
    def rename(self, fileWithoutExtension, key, ext=".mp3"):

        dest = fileWithoutExtension + f"_{key}"
        os.rename(fileWithoutExtension + ext, dest + ext)

        return True