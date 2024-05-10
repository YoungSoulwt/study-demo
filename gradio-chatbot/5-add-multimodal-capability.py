"""
您可能想为您的聊天机器人添加多模式功能。例如，您可能希望用户能够轻松地将图像或文件上传到您的聊天机器人并提出相关问题。
您可以通过向 gr.ChatInterface 类传递单个参数 (multimodal=True) 来使聊天机器人成为“多模式”。
"""
import gradio as gr
import time


def count_files(message, history):
    num_files = len(message["files"])
    return f"You uploaded {num_files} files"


file_path = "E:\技术文档\github\study-demo\gradio-chatbot\README.md"

demo = gr.ChatInterface(fn=count_files, examples=[{"text": "Hello", "files": [file_path]}], title="Echo Bot",
                        multimodal=True)

demo.launch()
