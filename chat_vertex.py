from vertexai import generative_models
from vertexai.generative_models import GenerativeModel

model = GenerativeModel(model_name="gemini-1.0-pro")
generation_config = {"temperature": 0.4}

# Safety config
#https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/configure-safety-attributes
# safety_config = {
#     generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
#     generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
# #     }
# prompt = input("prompt: ")

# responses = model.generate_content(
#     prompt,
#     generation_config=config,
#     stream=True,
#     safety_settings=safety_config,
#     )

# text_responses = []
# for response in responses:
#     print(response.text)
#     text_responses.append(response.text)
#     # return "".join(text_responses)
while True:
    query = input(f"\nQuery: ")
    response = model.generate_content(query, generation_config=generation_config)
    print(f"\nVertexAI: {response.text}")