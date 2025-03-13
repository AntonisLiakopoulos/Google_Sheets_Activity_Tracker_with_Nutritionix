This Python script allows users to log their workouts by simply describing the exercise they performed. 
It utilizes the Nutritionix API to analyze the workout and estimate calorie burn. The data is then stored in a Google Sheet using the Sheety API.

How It Works
User Input: The script prompts the user to enter details about their workout (e.g., "I ran for 30 minutes").
Nutritionix API Request:
The script sends the exercise description, along with user-specific details (gender, weight, height, and age), to the Nutritionix API.
The API returns structured information about the workout, including estimated calories burned and duration.
Data Logging:
The script formats the extracted data with the current date and time.
It then sends this information to a Google Sheet using Sheety’s API.
Response Handling:
The script prints the response from both APIs to confirm successful execution.
