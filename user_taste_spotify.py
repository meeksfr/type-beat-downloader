from user_taste import UserTaste
import requests
from urllib.parse import urlencode
import base64
import webbrowser

class SpotifyTaste(UserTaste):

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

    def getSearchTerms(self, endpoint="https://api.spotify.com/v1/me/top/artists?time_range=short_term"):

        req = requests.get(endpoint,
                        headers=self.headers)
        artists = req.json()

        names = []
        for artist in artists['items']:
            names.append(artist['name'])

        self.terms = names
        return names

    def triggerCallback(self):
        #adapted from https://python.plainenglish.io/bored-of-libraries-heres-how-to-connect-to-the-spotify-api-using-pure-python-bd31e9e3d88a

        auth_headers = {
            "client_id": self.client_id,
            "response_type": "code",
            "redirect_uri": "http://localhost:7777/callback",
            "scope": "user-top-read"}

        webbrowser.open("https://accounts.spotify.com/authorize?" + urlencode(auth_headers))

    def authenticate(self, callbackUrl):
        #adapted from https://python.plainenglish.io/bored-of-libraries-heres-how-to-connect-to-the-spotify-api-using-pure-python-bd31e9e3d88a

        code = callbackUrl.split("code=")[1]

        encoded_credentials = base64.b64encode(self.client_id.encode() + b':' + self.client_secret.encode()).decode("utf-8")

        token_headers = {
            "Authorization": "Basic " + encoded_credentials,
            "Content-Type": "application/x-www-form-urlencoded"
        }

        token_data = {
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": "http://localhost:7777/callback"
        }

        r = requests.post("https://accounts.spotify.com/api/token", data=token_data, headers=token_headers)

        token = r.json()["access_token"]

        headers = {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json"
        }

        self.headers = headers                                                                                                                    