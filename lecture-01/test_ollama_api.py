import os
import requests

os.environ["OLLAMA_HOST"] = "http://127.0.0.1:11434"
os.environ["NO_PROXY"] = "localhost,127.0.0.1"
os.environ["no_proxy"] = "localhost,127.0.0.1"

s = requests.Session()
s.trust_env = False  # <- ignore ALL proxy env vars

print(s.get("http://127.0.0.1:11434/api/version", timeout=3).json())

# make sure to import after the s.trust_env

from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model='qwen3:0.6b', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])
print(response['message']['content'])