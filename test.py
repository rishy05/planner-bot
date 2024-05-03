import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()


token_gemini = os.getenv("API_GEMINI")
genai.configure(api_key=token_gemini)

# Set up the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]


def get_plan(origin, desti, num_peo, num_days):
    print("Entering get_plan")
    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro-latest",
        generation_config=generation_config,
        safety_settings=safety_settings,
    )
    print("All set up")
    convo = model.start_chat(history=[])
    print("Generating plan")
    convo.send_message(
        f"You are my itinerary planner. I will give you the details and give me the best possible itinerary for each day. Here are the details 1. Strating city: {origin} 2. Destination: {desti} 3. Number of People: {num_peo} 4. Number of Days: {num_days}. Make sure it's less than 500 characters in length (very important). Make it very simple"
    )

    resp = convo.last.text
    print("Generating places names.")
    convo.send_message(
        f"Get all the monuments and place names except for city names from this text and return it in this format in python string separated by commas format. Just the list nothign else no need for a variable name. no need to add the python format"
    )

    places = convo.last.text

    r = [resp, places]
    print(r)
    return r
