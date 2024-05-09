import gradio as gr
import cv2


def greet(name):
    return "Hello " + name + "!"


def turn_gray(image):
    """
    将图片转成其的灰度图
    """
    gray = cv2.cvtColor(image, cv2.COLOR_RGBA2GRAY)
    return gray


def file_path(input, radio):
    return input


"""
Interface 类通常用于构建一些简单的界面
接受三个参数，处理函数，输入，输出
"""
# iface = gr.Interface(fn=greet, inputs="text", outputs="text")


"""
inputs 和 outputs 都可以自定义组件，比如说这里限制行数，没有输入时显示的文字，标签
"""
# iface = gr.Interface(fn=greet, inputs=gr.Textbox(lines=5, placeholder="text here", label="name: "), outputs=gr.Textbox(label="Greeting"))


"""
图生图
"""
# iface = gr.Interface(fn=turn_gray, inputs=gr.Image(), outputs="image")


"""
还可以接受音频
"""
# iface = gr.Interface(fn=file_path, inputs=gr.Audio(sources=["microphone"], type="filepath"), outputs="text")


"""
inputs 可以是一个列表
当然，fn 方法也要对应增加入参
"""
iface = gr.Interface(fn=file_path, inputs=[gr.Audio(sources=["microphone"], type="filepath"), gr.Radio(["a", "b"])], outputs="text")


"""
启动界面
"""
iface.launch()
