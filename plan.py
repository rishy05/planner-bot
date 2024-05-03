import os

from groq import Groq

from dotenv import load_dotenv

from time import sleep

load_dotenv()

gr_key = os.getenv("GROQ_API_KEY")

client = Groq(
    api_key=gr_key,
)


def get_plan(origin, desti, num_peo, num_days):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"You are my itinerary planner. I will give you the details and give me the best possible itinerary for each day. Here are the details 1. Strating city: {origin} 2. Destination: {desti} 3. Number of People: {num_peo} 4. Number of Days: {num_days}. Make sure it's less than 600 characters in length (very important). Make it very simple",
            }
        ],
        model="mixtral-8x7b-32768",
    )
    msgg = chat_completion.choices[0].message.content
    sleep(2)
    chat_completion_2 = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"Get all the monuments and place names except for city names from this text and return it in this format in python string separated by commas format. Just the string nothing else, no need for a variable name. no need to add the python format. here is the text {msgg}",
            }
        ],
        model="mixtral-8x7b-32768",
    )
    pl = chat_completion_2.choices[0].message.content

    return [msgg, pl]
