import google.generativeai as genai
import os
import dotenv

dotenv.load_dotenv()
ai_model = "gemini-1.5-flash"
generation_config=genai.types.GenerationConfig(
        candidate_count=1,
        temperature=1,
    )
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel(ai_model, generation_config=generation_config)

def chat_ai(prompt):
    chat = model.start_chat(
        history=[]
    )
    response = chat.send_message(prompt)
    print(response.text)

while True:
    prompt = input("Prompt: ")
    chat_ai(prompt)
