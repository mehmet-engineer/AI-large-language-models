import requests

class DEEPSEEK:

    """ https://api-docs.deepseek.com/ """

    def __init__(self, model: str, api_key: str, temperature: float, system_role: str):
        self.model = model
        self.api_key = api_key
        self.temperature = temperature
        self.system_role = system_role

        self.api_url = "https://api.deepseek.com/chat/completions"
        self.headers = {
            "Authorization": "Bearer " + self.api_key,
            "Content-Type": "application/json"
        }

    def generate_text_response(self, prompt: str) -> str:
        data = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": self.system_role},
                {"role": "user", "content": prompt}
            ]
        }

        response = requests.post(self.api_url, headers=self.headers, json=data)
        response.raise_for_status()
        result = response.json()['choices'][0]['message']['content']

        return result