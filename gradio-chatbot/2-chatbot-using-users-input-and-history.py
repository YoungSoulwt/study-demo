"""
当然，前面的例子非常简单，它甚至没有考虑用户输入或以前的历史记录！这是另一个简单的示例，展示了如何合并用户的输入和历史记录。
"""
import random
import gradio as gr


def alternatingly_agree(message, history):
    if len(history) % 2 == 0:
        return f"Yes, I do think that '{message}'"
    else:
        return "I don't think so"


gr.ChatInterface(alternatingly_agree).launch()
