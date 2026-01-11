import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Qwen3-0.6B is the standard dense version
model_id = "Qwen/Qwen3-0.6B"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto")

def get_sentence_probability(sentence):
    inputs = tokenizer(sentence, return_tensors="pt").to(model.device)
    input_ids = inputs["input_ids"]
    
    with torch.no_grad():
        # Passing labels=input_ids tells the model to calculate the cross-entropy loss
        outputs = model(input_ids, labels=input_ids)
        avg_loss = outputs.loss.item()
    
    # Total Log-Likelihood is -(average_loss * sequence_length)
    total_log_prob = -avg_loss * input_ids.shape[1]
    
    return avg_loss, total_log_prob

s1 = "He to reporters introduced main content"
s2 = "He briefed reporters on the main contents of the statement"

s1 = "It's hard to recognize speech"
s2 = "It's hard to wreck a nice beach"

loss1, logprob1 = get_sentence_probability(s1)
loss2, logprob2 = get_sentence_probability(s2)

print(f"Sentence 1 (Broken):  Loss: {loss1:.4f} | Total Log-Prob: {logprob1:.4f}")
print(f"Sentence 2 (Natural): Loss: {loss2:.4f} | Total Log-Prob: {logprob2:.4f}")

if loss2 < loss1:
    print("\nResult: Sentence 2 is more likely/natural according to Qwen3.")