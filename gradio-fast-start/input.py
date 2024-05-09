import gradio as gr

"""
输入列表
"""
input_list = [
    # 音频输入，源文件可以选择上传或者麦克风输入
    gr.Audio(sources=["upload", "microphone"], type="numpy", label="Audio File"),
    # 选择框
    gr.Checkbox(label="Checkbox"),
    # 颜色选择器，支持选择颜色作为输入
    gr.ColorPicker(label="Color Picker"),
    # 表格
    gr.Dataframe(label="Dataframe"),
    # 下拉框
    gr.Dropdown(["op1", "op2"], label="Dropdown"),
    # 文件
    gr.File(type="binary", label="File"),
    # 图片
    gr.Image(sources=["upload", "clipboard"], label="Image"),
    # 数字
    gr.Number(label="Number"),
    # 单选框
    gr.Radio(["op1", "op2"], label="Radio"),
    # 滑动条
    gr.Slider(minimum=0, maximum=10, step=5, label="Slider"),
    # 文本
    gr.Textbox(lines=3, max_lines=7, placeholder="Placeholder", label="Textbox"),
    # 大号版的 textbox
    gr.TextArea(lines=3, max_lines=7, placeholder="Placeholder", label="Text Area"),
    # 视频
    gr.Video(sources=["upload", "webcam"], label="Video"),
    # 复选框
    gr.Checkboxgroup(["op1", "op2"], label="Checkboxgroup Group")
]

"""
输出列表
"""
output_list = [
    gr.Textbox(label="Audio outputs", lines=7),
    gr.Textbox(label="Checkbox outputs"),
    gr.Textbox(label="ColorPicker outputs"),
    gr.Textbox(label="Dataframe outputs"),
    gr.Textbox(label="Dropdown outputs"),
    gr.Textbox(label="File outputs"),
    gr.Textbox(label="Image outputs"),
    gr.Textbox(label="Number outputs"),
    gr.Textbox(label="Radio outputs"),
    gr.Textbox(label="Slider outputs"),
    gr.Textbox(label="Textbox outputs"),
    gr.Textbox(label="TextArea outputs"),
    gr.Textbox(label="Video outputs"),
    gr.Textbox(label="Checkboxgroup outputs"),
]


def input_and_output(*input_data):
    """
    处理函数
    """
    return input_data


iface = gr.Interface(fn=input_and_output,
                     inputs=input_list,
                     outputs=output_list,
                     title="Input and Output",
                     description="This is a test of all the input types.",
                     live=True,  # 不用submit了，每次输入更改以后会直接刷新输出
                     )

iface.launch()

"""
可以直接在控制台输入：
gradio input.py
这样做的好处是，每次改完代码以后，就不用重新执行文件了，热部署？
"""
