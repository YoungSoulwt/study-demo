"""
如果您熟悉 Gradio 的 Interface 类，那么 gr.ChatInterface 包含许多相同的参数，您可以使用它们来自定义聊天机器人的外观和感觉。例如，您可以：
- 使用 title 和 description 参数在聊天机器人上方添加标题和描述。
- 分别使用 theme 和 css 参数添加主题或自定义 css。
- 添加示例，甚至启用cache_examples，这让用户更容易尝试。
- 您可以更改文本或禁用聊天机器人界面中显示的每个按钮：submit_btn、retry_btn、undo_btn、clear_btn。

如果您想自定义构成 ChatInterface 的 gr.Chatbot 或 gr.Textbox，那么您也可以传入您自己的聊天机器人或文本框。以下是我们如何使用这些参数的示例：
"""
import gradio as gr


def yes_man(message, history):
    if message.endswith("?"):
        return "Yes"
    else:
        return "Ask me anything!"


gr.ChatInterface(
    yes_man,
    chatbot=gr.Chatbot(height=300),
    textbox=gr.Textbox(placeholder="Ask me a yes or no question", container=False, scale=7),
    title="Yes Man",
    description="Ask Yes Man any question",
    theme="soft",
    examples=["Hello", "Am I cool?", "Are tomatoes vegetables?"],
    cache_examples=True,
    retry_btn=None,
    undo_btn="Delete Previous",
    clear_btn="Clear",
).launch()
