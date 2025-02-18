# llama_model.py

from ollama import chat, ChatResponse

def query_llama(prompt, conversation_history=""):
    # Queries the Llama model to respond based on user input, considering product data.

    full_prompt = conversation_history + f"\nUser: {prompt}\nAssistant:"

    response: ChatResponse = chat(model='llama3.1', messages=[
        {'role': 'user', 'content': full_prompt}
    ])

    assistant_response = response['message']['content']
    return assistant_response