"""
让我们编写一个随机响应“是”或“否”的聊天函数。

"""
import random
import gradio as gr


def random_response(message, history):
    return random.choice(["yes", "no"])


"""
现在，我们可以将其插入 gr.ChatInterface() 并调用 .launch() 方法来创建 Web 界面：
"""
gr.ChatInterface(random_response).launch()
