import requests
import json

class RemoteOllamaModelWithTools:
    BASE_PROMPT = """
You have access to functions. If you decide to invoke any of the function(s),
you MUST put it in the format of
{"name": function name, "parameters": dictionary of argument name and its value}

You SHOULD NOT include any other text in the response if you call a function.
If there is no functions specifications, you should respond with a text response only.
"""


    def __init__(self, generate_url):
        self._generate_url = generate_url

    def invoke(self, model, messages, tools=None):
        payload = {
            "model": model,
            "prompt": RemoteOllamaModelWithTools.BASE_PROMPT + (str(tools) if tools else "") + str(messages)
        }

        response = requests.post(self._generate_url, json=payload, stream=True)

        full_text = ""
        for line in response.iter_lines():
            if line:
                data = json.loads(line.decode("utf-8"))
                full_text += data.get("response", "")
                if data.get("done"):
                    break

        return full_text

