import requests
from pprint import pprint
import os
from dotenv import load_dotenv

load_dotenv()

rapid = os.getenv("API_RAPID")


def get_searchh(q):

    url = "https://real-time-web-search.p.rapidapi.com/search"

    querystring = {"q": f"things to do in {q}", "limit": "100"}

    headers = {
        "X-RapidAPI-Key": rapid,
        "X-RapidAPI-Host": "real-time-web-search.p.rapidapi.com",
    }

    response = requests.get(url, headers=headers, params=querystring)

    return [response.json()["data"][0]["url"], response.json()["data"][1]["url"]]
