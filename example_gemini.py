from Models.Gemini import GEMINI

model = "gemini-2.0-flash"
API_KEY = "API_KEY"
temperature = 0.4
gemini_model = GEMINI(model, API_KEY, temperature)

# trial 1
prompt = "what is ai?"
response = gemini_model.generate_text_response(prompt)

# trial 2
prompt = "what is the object inside of the image?"
input_img = "Assets/example_img.png"
response = gemini_model.generate_response_with_image(prompt, input_img)

# trial 3
prompt = "write a python code to calculate the sum of two numbers."
response = gemini_model.generate_python_code(prompt)

print(response)