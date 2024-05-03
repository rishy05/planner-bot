import requests
from pprint import pprint
import os
from dotenv import load_dotenv

load_dotenv()


API_URL = (
    "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
)
headers = {"Authorization": f"Bearer {os.getenv("API_HUGGING")}"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()[0]["generated_text"]


output = query(
    {
        "inputs": f"You are my itinerary planner. I will give you the details and give me the best possible itinerary for each day. Here are the details 1. Strating city: Chennai, 2. Destination: paris, 3. Number of People: 3, 4. Number of Days: 3. Make sure it's less than 500 characters in length (very important). Make it very simple",
    }
)

print(output)


def q2(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


pprint(
    q2(
        {
            "inputs": f"Get all the monuments and place names except for city names from this text and return it in this format in python string separated by commas format. Just the list nothign else no need for a variable name. no need to add the python format {output}"
        }
    )
)
