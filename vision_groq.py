from groq import Groq
import base64
import os
import dotenv

#setup
image_directory = "imagens/"
model = "llama-3.2-90b-vision-preview"

dotenv.load_dotenv()
client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)

# Função para codificar a imagem em base64
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Função para enviar a imagem e obter o resultado
def chat_ai(base64_image, image_filename):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Descreva em portugues e resuma em um paragrafo o conteudo da imagem"},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}",
                        },
                    },
                ],
            }
        ],
        model=model,
        temperature=0,
    )
    print(f"----- Descrição da imagem {image_filename}: -----")
    print(f"{chat_completion.choices[0].message.content}\n")

def main():
    for image_filename in os.listdir(image_directory):
        image_path = os.path.join(image_directory, image_filename)
        if os.path.isfile(image_path):
            base64_image = encode_image(image_path)
            chat_ai(base64_image, image_filename)
            
if __name__ == "__main__":
    main()