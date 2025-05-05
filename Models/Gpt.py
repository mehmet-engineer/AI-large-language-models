from openai import OpenAI

class GPT:

    """ https://platform.openai.com/docs/quickstart """

    def __init__(self, model: str, api_key: str):
        self.model = model
        self.api_key = api_key
        self.client = OpenAI(api_key=api_key)

    def generate_text_response(self, prompt: str) -> str:
        response = self.client.responses.create(
            model=self.model,
            input=prompt
        )
        response = response.output_text

        return response
    
    def generate_response_with_image(self, prompt: str, input_img: str) -> str:
        response = self.client.responses.create(
            model=self.model,
            input=[
                { "role": "user", "content": prompt },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_image",
                            "image_url": input_img
                        }
                    ]
                }
            ]
        )
        response = response.output_text

        return response