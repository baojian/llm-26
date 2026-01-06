import os
import time
import math
import requests

# If you have proxy, make sure bypass proxies for local services (e.g., Ollama on localhost:11434)
# You can check whether Ollama is running or not by tpying: http://127.0.0.1:11434/ in your Chrome.
# export OLLAMA_HOST=http://127.0.0.1:11434
# export NO_PROXY=localhost,127.0.0.1
# export no_proxy=localhost,127.0.0.1
os.environ["OLLAMA_HOST"] = "http://127.0.0.1:11434"
os.environ["NO_PROXY"] = "localhost,127.0.0.1"
os.environ["no_proxy"] = "localhost,127.0.0.1"

s = requests.Session()
s.trust_env = False  # <- ignore ALL proxy env vars

print(s.get("http://127.0.0.1:11434/api/version", timeout=3).json())

# !!!! make sure to import after the s.trust_env !!!!

import ollama
from ollama import chat
from ollama import ChatResponse

s = requests.Session()
s.trust_env = False  # <- ignore ALL proxy env vars

response: ChatResponse = chat(model='qwen3:0.6b', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])
print(response['message']['content'])

models = ["qwen3:0.6b", "qwen3:1.7b"]
prompt = "Fudan University is located in which city? Answer with one word."

for model in models:
    print('-' * 50)
    start_time = time.time()
    for _ in range(10):
        resp = ollama.generate(
            model = model,
            prompt = prompt
        )
        print(f"{model} with resp {_ + 1}: {resp["response"]}")
    print(f'total runtime of 10 responses of {model} is: {time.time() - start_time:.1f} seconds')