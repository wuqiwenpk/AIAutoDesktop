from utils.browser import Browser
from utils.dingding import DingDing
from utils.wechat import Wechat


tools_map = dict(
    send_message_to_wechat=Wechat().search_and_chat,
    send_message_to_dingding=DingDing().search_and_chat,
    browser_search_question=Browser().search_bing
)

tools = [
    {
        "type": "function",
        "function": {
            "name": "send_message_to_wechat",
            "description": "发送消息到微信聊天软件",
            "parameters": {
                "type": "object",
                "properties": {
                    "friend_name": {"type": "string", "description": "好友名称"},
                    "message": {"type": "string", "description": "要发送的消息"},
                },
                "required": ["friend_name", "message"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "send_message_to_dingding",
            "description": "发送消息到钉钉聊天软件",
            "parameters": {
                "type": "object",
                "properties": {
                    "friend_name": {"type": "string", "description": "好友名称"},
                    "message": {"type": "string", "description": "要发送的消息"},
                },
                "required": ["friend_name", "message"]
            }
        }
    },
{
        "type": "function",
        "function": {
            "name": "browser_search_question",
            "description": "打开浏览器并搜索问题",
            "parameters": {
                "type": "object",
                "properties": {
                    "message": {"type": "string", "description": "要发送的问题"}
                },
                "required": ["message"]
            }
        }
    },
]
