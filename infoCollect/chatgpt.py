import openai

# Please fill in your key
openai.api_key = "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"

# Interacting with chatgpt
def chat_gpt(prompt):
    
    prompt = prompt
    
    model_engine = "text-davinci-003"
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    response = completion.choices[0].text
    return response

