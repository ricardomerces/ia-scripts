# from diffusers import StableDiffusionPipeline
# import torch

# def gerar_imagem(): 
#     model_id = "runwayml/stable-diffusion-v1-5"
#     pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
#     pipe = pipe.to("cuda")
#     prompt = input("Descreva a imagem a ser criada? ")
#     image = pipe(prompt).images[0]  
#     image.save("img.png")


# def main():
#   while True:
#     gerar_imagem()

# if __name__ == '__main__':
#   main()
import torch

print("Torch version:",torch.__version__)

print("Is CUDA enabled?",torch.cuda.is_available())