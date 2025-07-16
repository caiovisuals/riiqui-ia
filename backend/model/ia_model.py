from transformers import pipeline

chat = pipeline("text-generation", model="pierreguillou/gpt2-small-portuguese")

def respond(question: str) -> str:
    result = chat(question, max_length=50, num_return_sequences=1)
    return result[0]["generated_text"]
