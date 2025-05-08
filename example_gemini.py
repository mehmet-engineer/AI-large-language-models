from Models.Gemini import GEMINI

model = "gemini-2.0-flash"
API_KEY = "API_KEY"
temperature = 0.4
gemini_model = GEMINI(model, API_KEY, temperature)

system_prompt_path = "system_prompt.txt"
with open(system_prompt_path, "r") as file:
    system_prompt = file.read()

first_resp = gemini_model.chat_with_gemini(system_prompt)
print(first_resp)

while True:
    input_text = input("\n ----------- \n Your prompt: ")
    response = gemini_model.chat_with_gemini(input_text)
    print("\n", response)