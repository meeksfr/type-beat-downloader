from metric_analyzer import MetricAnalyzer
import numpy as np
import librosa

class LibrosaKey(MetricAnalyzer):
    '''
    adapted from: https://medium.com/@oluyaled/detecting-musical-key-from-audio-using-chroma-feature-in-python-72850c0ae4b1
    '''

    def __init__(self):
        self.keyMapping = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'Ab', 'A', 'Bb', 'B']

    def analyse(self, path):
        # Load the audio file
        y, sr = librosa.load(path)

        # Compute the Chroma Short-Time Fourier Transform (chroma_stft)
        chromagram = librosa.feature.chroma_stft(y=y, sr=sr)

        # Calculate the mean chroma feature across time
        mean_chroma = np.mean(chromagram, axis=1)

        # Find the key by selecting the maximum chroma feature
        estimated_key_index = np.argmax(mean_chroma)
        estimated_key = self.keyMapping[estimated_key_index]

        return estimated_key