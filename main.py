import requests
import json

from utils.tools import tools, tools_map

# 获取你自己的Deepseek ApiKey
# 访问：https://platform.deepseek.com/api_keys
# ################### ApiKey #########################
apikey = "your apikey"

# ################### ApiKey #########################


def chat(message: str):
    url = "https://api.deepseek.com/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(apikey)
    }
    data = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": message}
        ],
        "tools": tools,  # 添加函数声明
        "tool_choice": "auto",
        "stream": False
    }

    response = requests.post(url, headers=headers, json=data, timeout=20)
    return response.json()


def call_function(call_info: dict):
    function_name = call_info["name"]
    print("call function: {}".format(function_name))
    function_arguments = json.loads(call_info["arguments"])
    callback = tools_map[function_name]
    callback(**function_arguments)


def start():
    while True:
        message = input(
            "请输入问题后按回车："
        )
        print("Wait Api Result...")
        result = chat(message=message)
        # print(result)
        call_info = result["choices"][0]["message"]["tool_calls"][0]["function"]
        call_function(call_info)


if __name__ == '__main__':
    start()
