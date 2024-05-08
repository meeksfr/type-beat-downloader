from metric_analyzer import MetricAnalyzer
import re

class RegexBPM(MetricAnalyzer):

    def __init__(self, pattern=r"\b(\d{2,3})(?:[^\d]{0,3})(?:bpm)\b|\b(?:bpm)(?:[^\d]{0,3})(\d{2,3})\b"):
        self.pattern = pattern

    def analyse(self, videoDesc):
        text = videoDesc.lower()
        matches = re.search(self.pattern, text)
        if matches:
            return matches.group(1) or matches.group(2)