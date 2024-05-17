import google.generativeai as genai

models = genai.list_models()

for i in models:
    print(f"{i}\n")