import gradio as gr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def audio_fn(audio):
    hz = audio[0]
    data = audio[1]
    return hz, data


def process():
    cheetahs = [
        "https://upload.wikimedia.org/wikipedia/commons/0/09/TheCheethcat.jpg",
        "https://nationalzoo.si.edu/sites/default/files/animals/cheetah-003.jpg",
    ]
    cheetahs = [(cheetah, f"Cheetah {i+1}") for i, cheetah in enumerate(cheetahs)]
    return cheetahs


def fig_out():
    Fs = 8000
    f = 5
    sample = 10
    x = np.arange(sample)
    y = np.sin(2 * np.pi * f * x / Fs)
    plt.plot(x, y)  # 折线图
    plt.bar(x, y)  # 柱状图

    return plt


def hello():
    return "Hello World!"


"""
输出对象可以是音频
可以接受一个 numpy 数组或者一个文件路径
"""
# demo = gr.Interface(fn=audio_fn, inputs=gr.Audio(type="numpy"), outputs="audio")


"""
输出一个柱状图
"""
# simple = pd.DataFrame({
#     "a": [1, 2, 3],
#     "b": [4, 5, 6]
# })
# demo = gr.Interface(fn=None, inputs=None, outputs=gr.BarPlot(simple, x="a", y="b"))


"""
输出一个图片列表
"""
# demo = gr.Interface(fn=process, inputs=None, outputs=gr.Gallery(columns=5))


"""
输出一个坐标图
"""
# demo = gr.Interface(fn=fig_out, inputs=None, outputs=gr.Plot())


"""
输出文本
"""
# demo = gr.Interface(fn=hello, inputs=None, outputs=gr.Textbox())


"""
输出 Json
"""
# json_sample = {"name": "John", "age": 18, "city": "Japan"}
# demo = gr.Interface(fn=None, inputs=None, outputs=gr.Json(json_sample))


"""
输出 html
"""
html_sample = "<h1>Hello World!</h1>"
demo = gr.Interface(fn=None, inputs=None, outputs=gr.HTML(html_sample))


demo.launch()


"""
一般来说，输入组件也都可以当输出组件使用，但是就看好不好用了。
"""
