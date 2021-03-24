import requests
from requests_oauthlib import OAuth1
import os


class IconGetter:
    def __init__(self, path):
        self._path = path
        self._base_url = "http://api.thenounproject.com/icon/"
        self._auth = OAuth1(os.getenv("KEY"), os.getenv("SECRET"))

    @property
    def path(self):
        return self._path

    def _get_responce(self, key_word):
        endpoint = f"{self._base_url}{key_word}"
        response = requests.get(endpoint, auth=self._auth)
        return response.json()

    def get_icon(self, key_word):
        res = self._get_responce(key_word)
        if "icon_url" not in res["icon"]:
            print("term_id")
            key_word_term_id = res["icon"]["term_id"]
            res = self._get_responce(key_word_term_id)
        url_icon = res["icon"]["icon_url"]
        self._save_icon_from_url(url_icon, key_word)

    def _save_icon_from_url(self, url_icon, key_word):
        responce = requests.get(url_icon)
        icon = responce.content
        with open(f"{self._path}/{key_word}.svg", "wb") as file:
            file.write(icon)


icon_getter = IconGetter("test")
icon_getter.get_icon("hummer")
