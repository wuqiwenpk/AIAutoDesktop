import time
from operator import index

import pyautogui
import pyperclip
import pythoncom
import win32gui
from win32com import client


class Wechat:
    def find_wechat_window(self):
        """
        查找微信窗口，需要确保微信窗口已打开。

        Returns:
            bool: 如果找到并激活微信窗口返回 True，否则返回 False。
        """
        try:

            hwnd = win32gui.FindWindow(None, '微信')
            print(hwnd)
            # 通过句柄窗口置顶
            if hwnd:
                # Windows以单线程的方式创建com对象
                pythoncom.CoInitialize()
                shell = client.Dispatch("WScript.Shell")
                shell.SendKeys('%')
                win32gui.SetForegroundWindow(hwnd)

            time.sleep(0.5)
            return True

        except Exception as e:
            print(f"查找或激活微信窗口时出错: {str(e)}")
            return False

    def search_and_chat(self, friend_name: str, message: str):
        """
        搜索指定好友并发送消息。

        Args:
            friend_name (str): 要搜索的好友名字。
            message (str): 要发送的消息。

        Returns:
            bool: 如果消息发送成功返回 True，否则返回 False。
        """
        print("send message:{} to {}".format(message, friend_name))
        if not self.find_wechat_window():
            return False

        # 按 Ctrl+F 激活搜索框
        pyautogui.hotkey('ctrl', 'f')
        time.sleep(0.5)

        # 使用剪贴板输入好友名字
        pyperclip.copy(friend_name)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.5)

        # 按回车选择第一个搜索结果
        pyautogui.press('enter')
        time.sleep(0.5)

        # 使用剪贴板输入消息
        pyperclip.copy(message)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.5)

        # 发送消息
        pyautogui.press('enter')

        return True


wechat_proxy = Wechat()


if __name__ == '__main__':
    friend_name = "小明"
    message = "你好！这是一条测试消息"
    wechat_proxy.search_and_chat(friend_name, message)
