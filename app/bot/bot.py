import requests as req
import os
import json

class OpenAI:
    
    def __init__(self, base_url : str, api_key : str):
        self.base_url = base_url
        self.api_key = api_key
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def get_chat(self , prompt : str , model : str = "gpt-4o-mini") -> str:
        
        data = {
            "model": model,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }
        
        try:
            response = req.post(
                url=f"{self.base_url}/v1/chat/completions",
                headers=self.headers,
                json=data
            )
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]
        except req.exceptions.RequestException as err:
            return f"Error: {err}"
    
if __name__ == "__main__":
    bot = OpenAI(
        base_url="https://api.openai.com",
        api_key=str(os.getenv("SECRET_KEY"))
    )
    
    while True:
        prompt = input("You: ")
        response = bot.get_chat(prompt)
        if response.lower() in ["exit", "quit", "sair", "bye"]:
            print("OpenAI: Goodbye!")
            break
        print(f"OpenAI: {response}")
        
        