import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Browser:

    def __init__(self):
        self.browser = None
        self.wait = None

    def init(self):
        # 初始化Chrome浏览器
        self.browser = webdriver.Chrome()
        # 设置等待时间
        self.wait = WebDriverWait(self.browser, 10)

    def search_bing(self, message: str):
        self.init()
        try:
            # 访问Bing
            self.browser.get("https://www.bing.com")

            # 等待页面加载完成
            time.sleep(2)

            try:
                # 尝试多种定位方式
                search_box = self.browser.find_element(By.NAME, "q")
            except:
                try:
                    search_box = self.browser.find_element(By.CLASS_NAME, "sb_form_q")
                except:
                    search_box = self.browser.find_element(By.ID, "sb_form_q")

            # 确保元素可见和可交互
            self.wait.until(EC.element_to_be_clickable((By.NAME, "q")))

            # 使用JavaScript直接设置值
            self.browser.execute_script("arguments[0].value = arguments[1]", search_box, message)

            # 等待一下确保输入完成
            time.sleep(2)

            # 模拟按下回车键
            search_box.send_keys(Keys.RETURN)

            # 等待搜索结果加载
            time.sleep(2)

            # 获取窗口高度
            window_height = self.browser.execute_script("return window.innerHeight")
            last_height = self.browser.execute_script("return document.body.scrollHeight")

            # 缓慢滚动到底部
            while True:
                # 获取当前滚动位置
                current_position = self.browser.execute_script("return window.pageYOffset")
                scroll_step = 400  # 每次滚动300像素

                # 执行滚动
                self.browser.execute_script(f"window.scrollTo(0, {current_position + scroll_step})")

                # 等待滚动动画完成
                time.sleep(0.8)

                # 获取新的高度
                new_height = self.browser.execute_script("return document.body.scrollHeight")
                current_position = self.browser.execute_script("return window.pageYOffset")

                # 检查是否到达底部
                if current_position + window_height >= new_height - 100:
                    break

                if new_height != last_height:
                    last_height = new_height

        except Exception as e:
            print(f"发生错误: {str(e)}")

        finally:
            self.close()

    def close(self):
        # 关闭浏览器
        self.browser.quit()


browserProxy = Browser()

if __name__ == '__main__':
    # 使用示例
    b = Browser()
    b.search_bing("附近的餐厅")
