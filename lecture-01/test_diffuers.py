import torch
from diffusers import DiffusionPipeline

MODEL_ID = "stable-diffusion-v1-5/stable-diffusion-v1-5"  # SD1.5

device = "mps" if torch.backends.mps.is_available() else "cpu"

pipe = DiffusionPipeline.from_pretrained(
    MODEL_ID,
    torch_dtype=torch.float16 if device == "mps" else torch.float32,
    use_safetensors=True,
    variant="fp16" if device == "mps" else None,
).to(device)

pipe.safety_checker = None
pipe.requires_safety_checker = False

# Recommended on Macs with <64GB RAM to reduce memory pressure
pipe.enable_attention_slicing()  #  [oai_citation:2‡Hugging Face](https://huggingface.co/docs/diffusers/en/optimization/mps)

prompt = "a watercolor painting of a university campus gate at sunset, people fully clothed, family-friendly"
img = pipe(prompt, num_inference_steps=50, guidance_scale=7.5).images[0]
img.save("out.png")
print("saved out.png")
