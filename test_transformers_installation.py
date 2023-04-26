from transformers import GPTNeoForCausalLM

model = GPTNeoForCausalLM.from_pretrained('anon8231489123/gpt4-x-alpaca-13b-native-4bit-128g')

print(model.config)