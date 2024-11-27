import gradio as gr
import os
import dotenv

dotenv.load_dotenv()

#model="black-forest-labs/FLUX.1-dev"
model="black-forest-labs/FLUX.1-schnell"

app = gr.load(name=model, src="models", token=os.getenv("HUGGINGFACE_API_KEY"))

app.launch()