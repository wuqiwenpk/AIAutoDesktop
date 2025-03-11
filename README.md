# AIAutoDesktop
基于Python开发的,结合大模型API调用,返回结构化的数据,执行桌面自动化任务

# 目前支持的功能
- 发送微信消息
- 发送钉钉消息
- 打开和访问浏览器

![自定义标题](show.gif)



# 本项目技术栈为： 
- Python 3.10


# 运行前准备
- Windows10桌面环境

- 安装第三方库
```bash
pip install -r requirements.txt
pip install assets/pywin32-304.0-cp310-cp310-win_amd64.whl
```
- 获取API-KEY
```
访问Deepseek
https://platform.deepseek.com/api_keys
```
- 配置API-KET
```
在main.py 顶部配置你自己的 apikey
```

# 运行
```bash
python main.py
```


# 声明
- 本项目仅用作学习用途
- 本项目不会上传任何你的数据至任何第三方系统
- 如果发生任何回传行为，请检查是否为第三方修改版本
