# slides/sd_server.py
import base64
import io
import time
from typing import Optional

import torch
from diffusers import DiffusionPipeline
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


MODEL_ID = "stable-diffusion-v1-5/stable-diffusion-v1-5"  # SD1.5

app = FastAPI(title="Local Stable Diffusion (Diffusers) API")

# Allow requests from your slides (localhost server, file, etc.)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for classroom demo; tighten later if desired
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

device = "mps" if torch.backends.mps.is_available() else "cpu"
dtype = torch.float16 if device == "mps" else torch.float32

pipe: Optional[DiffusionPipeline] = None


class GenReq(BaseModel):
    prompt: str
    num_inference_steps: int = 30
    guidance_scale: float = 7.5
    seed: Optional[int] = None


@app.on_event("startup")
def load_pipeline():
    global pipe
    pipe = DiffusionPipeline.from_pretrained(
        MODEL_ID,
        torch_dtype=dtype,
        use_safetensors=True,
        variant="fp16" if device == "mps" else None,
    ).to(device)

    # Disable safety checker for lecture demo (you already do this)
    pipe.safety_checker = None
    pipe.requires_safety_checker = False

    # Recommended for Macs with limited RAM
    pipe.enable_attention_slicing()


@app.get("/health")
def health():
    return {"ok": True, "device": device, "model": MODEL_ID}


@app.post("/generate")
def generate(req: GenReq):
    assert pipe is not None, "Pipeline not loaded"

    g = None
    if req.seed is not None:
        # MPS generator support can vary; if it fails, remove seed usage
        try:
            g = torch.Generator(device=device).manual_seed(req.seed)
        except Exception:
            g = None

    t0 = time.time()
    out = pipe(
        req.prompt,
        num_inference_steps=req.num_inference_steps,
        guidance_scale=req.guidance_scale,
        generator=g,
    )
    img = out.images[0]
    dt = time.time() - t0

    buf = io.BytesIO()
    img.save(buf, format="PNG")
    b64 = base64.b64encode(buf.getvalue()).decode("utf-8")

    return {
        "seconds": round(dt, 3),
        "device": device,
        "model": MODEL_ID,
        "image_base64": b64,
    }
