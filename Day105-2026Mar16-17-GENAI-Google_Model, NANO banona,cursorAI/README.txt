Nano Banana Image Prompts 
& Gemini / Gemma Generative AI Projects

Project Overview This repository contains experiments and practical
implementations of Generative AI using Google Gemini, Google Gemma LLMs,
Groq API, Hugging Face, and Nano Banana image generation prompts.

The project demonstrates multiple Generative AI capabilities including:

-   Text-to-text generation using Gemini
-   Image-to-text generation using Gemini Vision
-   Conversational AI chatbots using Streamlit
-   Integration of Gemma models with Hugging Face and Groq
-   Advanced image prompt engineering using Nano Banana
-   Multimodal AI applications

Technologies Used

-   Python
-   Google Gemini API
-   Google Gemma LLM
-   Hugging Face Transformers
-   LangChain
-   Groq Cloud
-   Streamlit
-   Jupyter Notebook
-   Google Colab

Nano Banana Image Prompt Engineering

Nano Banana is used for generating high‑quality AI images using detailed
prompts.

Example Prompt 1 – Figurine Generation

Using the nano-banana model, create a 1/7 scale commercialized figurine
of the characters in the picture, in a realistic style, in a real
environment. The figurine is placed on a computer desk with a
transparent acrylic base. The computer screen displays the brush
modeling process of the figurine. Next to the screen is a toy packaging
box printed with the original artwork.

Example Prompt 2 – Image Blending

Blend two images so that the subject appears to be wearing the jacket
from the second image. Match lighting, shadows, textures, and colors to
make the output photorealistic and cinematic. Remove glasses and ensure
natural facial features.

These prompts demonstrate advanced prompt engineering techniques used
for photorealistic image generation.

Google Gemini AI

Gemini is a multimodal large language model developed by Google DeepMind
capable of understanding and generating:

-   Text
-   Images
-   Audio
-   Video
-   Code

Gemini models can be accessed through Google AI Studio.

Create API Key

https://aistudio.google.com/app/apikey

Example Code – Gemini Text Generation

import google.generativeai as genai

genai.configure(api_key=“YOUR_API_KEY”)

model = genai.GenerativeModel(“gemini-pro”)

response = model.generate_content(“What is the meaning of life?”)

print(response.text)

Gemini Vision (Image Understanding)

Gemini Vision allows image analysis and description generation.

Example:

model = genai.GenerativeModel(“gemini-pro-vision”)

response = model.generate_content([prompt, image])

print(response.text)

Streamlit AI Chatbot Applications

This project includes multiple Streamlit applications:

app.py Basic Gemini question answering chatbot.

chat.py Conversation-based chatbot with streaming responses.

qachat.py Chatbot with persistent chat history.

vision.py Image analysis chatbot using Gemini Vision.

Run Application

streamlit run app.py

Google Gemma Models

Gemma is an open-source family of LLMs released by Google.

Available models:

-   Gemma 2B
-   Gemma 9B
-   Gemma 27B

Example Model

google/gemma-2-9b-it

Gemma Integration Methods

Gemma + Hugging Face Gemma + LangChain Gemma + Groq Cloud

Groq Cloud

Groq provides extremely fast inference for LLMs using LPUs.

Create API Key

https://console.groq.com/keys

Applications

These projects demonstrate real-world Generative AI applications:

-   AI chatbots
-   Question answering systems
-   Image understanding
-   AI assistants
-   Prompt engineering
-   Multimodal AI systems

Example Dataset

The repository includes text datasets such as:

Essay about India Essay about Indian Cricket

These are used for testing text summarization and question answering
tasks.

Learning Resources

Google DeepMind https://deepmind.google/

Gemini API Docs https://ai.google.dev/gemini-api/docs

Hugging Face Transformers https://huggingface.co/docs/transformers

LangChain Documentation https://python.langchain.com/docs

Conclusion

This repository demonstrates how modern Generative AI models such as
Gemini and Gemma can be combined with frameworks like LangChain, Hugging
Face, and Groq to build advanced AI applications including chatbots,
multimodal systems, and AI-powered image generation workflows.
