Generative AI with Stable Diffusion & Hugging Face

Project Overview This repository contains hands-on implementations of
Generative AI models using Stable Diffusion, Hugging Face, and PyTorch.
The project demonstrates how diffusion models can generate images,
audio, and other AI outputs using natural language prompts.

Technologies Used - Python - PyTorch - Hugging Face Transformers -
Hugging Face Diffusers - Stable Diffusion - Google Colab - Gradio -
NumPy - Pandas - TorchSDE

Key Concepts Covered - Generative AI - Diffusion Models - Stable
Diffusion Architecture - Text-to-Image Generation - Text-to-Audio
Generation - Multilingual Prompt Generation - Sentiment Analysis - Named
Entity Recognition (NER) - Hugging Face Model Hub usage

Stable Diffusion Architecture 1. CLIP Text Encoder – Converts text
prompt into embeddings. 2. Latent Noise Initialization – Model starts
with random Gaussian noise. 3. Noise Scheduler – Controls noise removal
during generation. 4. U-Net with Attention – Core model that removes
noise step-by-step. 5. Decoder – Converts latent representation into
final image. 6. Iterative Denoising – Image is refined until final
output is generated.

Repository Contents

1.  Text-to-Image Generation Notebooks demonstrating prompt-based image
    generation using Stable Diffusion models.

Examples: - stable_diffusion_2.ipynb -
stabilityai_stable_diffusion_2_1.ipynb -
stabilityai_stable_diffusion_xl_base_1_0.ipynb

2.  Text-to-Audio Generation Generate audio from natural language
    prompts using Hugging Face Stable Audio models. Example prompt: “The
    sound of a hammer hitting a wooden surface.” Output example:
    hammer.wav

3.  Image-to-Image Generation Using Stable Diffusion pipelines to modify
    or generate images from existing images.

Example: ghibli_&stable_diffusion_Image_Image_based_model.ipynb

4.  Multilingual Prompt Image Generation Generate images from prompts
    written in multiple languages using translation + Stable Diffusion
    pipeline.

5.  Hugging Face NLP Pipelines Includes examples of:

-   Text Generation
-   Named Entity Recognition (NER)
-   Sentiment Analysis

Example Code (Text-to-Audio)

from diffusers import StableAudioPipeline import torch import soundfile
as sf

pipe = StableAudioPipeline.from_pretrained(
“stabilityai/stable-audio-open-1.0”, torch_dtype=torch.float16 )

pipe = pipe.to(“cuda”)

prompt = “The sound of a hammer hitting a wooden surface.”

audio = pipe(prompt).audios

sf.write(“hammer.wav”, audio[0].T, pipe.vae.sampling_rate)

Real World Applications - Social Media Content Creation - Video Game
Asset Generation - Product Visualization for E-commerce - Animation
Storyboarding - AI Art Generation

Useful Resources Stable Diffusion Wikipedia:
https://en.wikipedia.org/wiki/Stable_Diffusion

Stable Diffusion GitHub: https://github.com/CompVis/stable-diffusion

Hugging Face Model Hub: https://huggingface.co/models

PyTorch Documentation: https://pypi.org/project/torch/

Hugging Face Authentication Create a Hugging Face token:
https://huggingface.co/settings/tokens

Login Example: from huggingface_hub import notebook_login
notebook_login()

Project Goals - Learn Generative AI concepts - Explore Stable Diffusion
models - Build AI applications - Understand Hugging Face ecosystem -
Experiment with AI pipelines for images, audio, and text
