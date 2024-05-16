from openai import OpenAI
import webbrowser
client = OpenAI()

def gerar_imagem(): 
  imagem = input("Qual a imagem a ser gerada? ")
  response = client.images.generate(
  model="dall-e-3",
  prompt=imagem,
  size="1024x1024",
  quality="standard",
  n=1,
)
  image_url = response.data[0].url
  webbrowser.open(image_url)

def main():
  while True:
    gerar_imagem()

if __name__ == '__main__':
  main()