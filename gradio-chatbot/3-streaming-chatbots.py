"""
在聊天功能中，您可以使用 yield 生成一系列部分响应，每个响应都会替换之前的响应。这样，您最终将得到一个流式聊天机器人。就这么简单！
"""
import time
import gradio as gr


def slow_echo(message, history):
    for i in range(len(message)):
        time.sleep(0.3)
        yield "You typed: " + message[: i+1]


"""
当响应流式传输时，“提交”按钮会变成“停止”按钮，可用于停止生成器功能。您可以使用“stop_btn”参数自定义“停止”按钮的外观和行为
"""
gr.ChatInterface(slow_echo).launch()
