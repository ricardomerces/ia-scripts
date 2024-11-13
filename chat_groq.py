import os
import dotenv
from groq import Groq

dotenv.load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)
def chat_ai(prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "Você é a minha assistente pessoal, tem 75% de humor e de maneira informal. Suas responstas devem utilizar o idioma Portugues do  Brasil.",
            },
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama3-8b-8192",
        temperature=1,
    )

    print(chat_completion.choices[0].message.content)

def main():
    while True:
        prompt = input("Prompt: ")
        chat_ai(prompt)

if __name__ == "__main__":
    main()