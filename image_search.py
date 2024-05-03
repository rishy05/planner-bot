import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

token_pexels = os.getenv("API_PEXELS")


def get_image(queries):
    url = "https://api.pexels.com/v1/search"

    img_l = []

    for query in queries:

        params = {"query": query, "per_page": 1}

        headers = {"Authorization": token_pexels}

        response = requests.get(url, params=params, headers=headers)

        if response.status_code == 200:
            try:
                # pprint(str(response.json()["photos"][0]["src"]["large"]))
                img_l.append(response.json()["photos"][0]["src"]["large"])
            except:
                try:
                    img_l.append(str(response.json()["src"]["original"]))
                    # pprint(str(response.json()["src"]["original"]))
                except:
                    pass
    pprint(img_l)
    return img_l


# get_image(["taj majal", "burj khalifa", "great barrier reef"])
