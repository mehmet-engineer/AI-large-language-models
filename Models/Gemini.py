from google import genai
from google.genai import types

class GEMINI:

    """ https://ai.google.dev/gemini-api/docs/quickstart?lang=python """

    def __init__(self, model: str, api_key: str, temperature: float):
        self.model = model
        self.api_key = api_key
        self.temperature = temperature
        self.client = genai.Client(api_key=api_key)

    def generate_text_response(self, prompt: str) -> str:
        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=self.temperature
                )
            )
        except Exception as e:
            print(f"Error: {e}")
            return None
        
        response = response.text

        return response
    
    def generate_response_with_image(self, prompt: str, input_img: str) -> str:
        try:
            client_file = self.client.files.upload(file=input_img)
            response = self.client.models.generate_content(
                model=self.model,
                contents=[client_file, prompt]
            )
        except Exception as e:
            print(f"Error: {e}")
            return None
        
        response = response.text

        return response
    
    def generate_python_code(self, prompt: str) -> str:
        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt,
                config=types.GenerateContentConfig(
                    tools=[types.Tool(
                        code_execution=types.ToolCodeExecution
                    )]
                )
            )
        except Exception as e:
            print(f"Error: {e}")
            return None
        
        response = response.text
        
        return response