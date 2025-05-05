from Models.DeepSeek import DEEPSEEK

model = "deepseek-reasoner"
API_KEY = "API_KEY"
temperature = 0.3
system_role = "You are a helpful assistant."

deepseek_model = DEEPSEEK(model, API_KEY, temperature, system_role)

prompt = "Hello, how are you?"
response = deepseek_model.generate_text_response(prompt)
print(response)