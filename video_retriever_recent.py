from video_retriever import VideoRetriever
from youtubesearchpython import *

class RecentUploads(VideoRetriever):

    def __init__(self, baseQuery='intitle:"{x}" type beat'):
        self.baseQuery = baseQuery
    
    def search(self, terms, limit=3):
        allLinks = []
        for a in terms:
            res = self.singleSearch(self.baseQuery.replace("{x}", a), limit)
            allLinks.extend(res)

        self.links = allLinks
        return allLinks

    def singleSearch(self, query, limit):
        customSearch = CustomSearch(query, VideoSortOrder.uploadDate, limit=limit)
        links = []
        for vid in customSearch.result()['result']:
            links.append(vid['link'])

        return links