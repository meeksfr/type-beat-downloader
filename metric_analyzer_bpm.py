from metric_analyzer import MetricAnalyzer
import re

class RegexBPM(MetricAnalyzer):

    def __init__(self):
        super().__init__()

    def analyse(self, videoDesc, pattern=r"\b(\d{2,3})(?:[^\d]{0,3})(?:bpm)\b|\b(?:bpm)(?:[^\d]{0,3})(\d{2,3})\b"):
        text = videoDesc.lower()
        matches = re.search(pattern, text)
        if matches:
            return matches.group(1) or matches.group(2)