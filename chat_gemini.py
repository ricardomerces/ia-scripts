import google.generativeai as genai

model = genai.GenerativeModel('gemini-1.0-pro')
generation_config = {"temperature": 0.4}
# Safety config
#https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/configure-safety-attributes
# safety_config = {
#     generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
#     generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
#     }

while True:
    query = input(f"\nQuery: ")
    response = model.generate_content(query, generation_config=generation_config)
    print(f"\nGenai: {response.text}")