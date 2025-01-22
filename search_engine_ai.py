import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

def answer_question_in_sms(user_message):
    hint_for_sms_form = "Make it short like an SMS"
    question = user_message + hint_for_sms_form
    response = model.generate_content(question)
    return response.text

