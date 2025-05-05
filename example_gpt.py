from Models.Gpt import GPT

model = "gpt-3.5-turbo"
API_KEY = "API_KEY"

gpt_model = GPT(model=model, api_key=API_KEY)

prompt = "Hello, how are you?"
response = gpt_model.generate_text_response(prompt)
print(response)