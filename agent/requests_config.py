import os
import requests

# https://platform.openai.com/docs/assistants/overview

class request_config:
    def __init__(self, deployment_id, api_version,):
        self.deployment_id = deployment_id
        self.api_version = api_version
    def create_url(self):
        self.url = f"https://cld.akkodis.com/api/openai/deployments/{self.deployment_id}/chat/completions?api-version={self.api_version}"
        return self.url
    def create_headers(self):
        self.headers = {
        "Content-Type": "application/json",
        "Cache-Control": "no-cache",
        "api-key": open(os.path.join(os.path.expanduser('.'), ".akr_key.txt"), 'r').read().strip()
        }
        return self.headers
    def create_data(self):
        self.data = {
        "temperature": 0.,
        "top_p": 1,
        "stream": False,
        "stop": None,
        "max_tokens": 4096,
        "presence_penalty": 0,
        "frequency_penalty": 0,
        "logit_bias": {},
        "user": "user",
        "n": 1,
        "seed": 0,
        "response_format": {
            "type": "text"
            }
        }
        return self.data
    def send_message(self, message):
        payload = self.create_data()
        payload.update({"messages": message})
        headers = self.create_headers()
        response = requests.post(self.create_url(), headers=headers, json=payload).json()
        return response['choices'][0]['message']['content']