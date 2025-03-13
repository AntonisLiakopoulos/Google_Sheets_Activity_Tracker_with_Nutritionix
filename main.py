import os
import requests
from datetime import datetime
import pprint
from dotenv import load_dotenv



load_dotenv("APIS.env")



GENDER = "male"
WEIGHT_KG = "85"
HEIGHT_CM = "175"
AGE = "38"


APP_ID = os.getenv("APP_ID", "Message")
API_KEY = os.getenv("API_KEY")
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ADD_ROW_ENDPOINT = os.getenv("SHEETY_ADD_ROW_ENDPOINT")

exercise_text = input("Tell me what exercise you did today: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key" : API_KEY,
    "x-remote-user-id": "0",
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,

}

response = requests.post(url=NUTRITIONIX_ENDPOINT,json=parameters,headers=headers)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

sheet_inputs = {
    "workout": {
        "date": today_date,
        "time": now_time,
        "exercise": result["exercises"][0]["user_input"].title(),
        "duration": result["exercises"][0]["duration_min"],
        "calories": result["exercises"][0]["nf_calories"]
        }
    }
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
bearer_header = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}
sheet_response = requests.post(SHEETY_ADD_ROW_ENDPOINT, json=sheet_inputs,headers=bearer_header)

print(sheet_response.text)



