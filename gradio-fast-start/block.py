import gradio as gr


"""
尝试用 block 模块手搓一个 stable_diffusion 出来
"""
with gr.Blocks(css="style.css") as demo:  # 可以自己手搓一个 css 文件，更加细腻的定制化界面
    # 第一个标签
    with gr.Tab(label="txt2img"):
        # 上半部分是第一块水平布局
        with gr.Row():
            # 第一块垂直布局
            with gr.Column(scale=15):  # scale 设置与相邻组件的比例关系，min_width 设置该组件的最小宽度
                txt1 = gr.Textbox(lines=2, label="")
                txt2 = gr.Textbox(lines=2, label="")

            # 第二块垂直布局
            with gr.Column(scale=1, min_width=1):
                button1 = gr.Button(value="1", elem_classes="btn")
                button2 = gr.Button(value="2", elem_classes="btn")
                button3 = gr.Button(value="3", elem_classes="btn")
                button4 = gr.Button(value="4", elem_classes="btn")

            # 第三块垂直布局
            with gr.Column(scale=6):
                generate_button = gr.Button(value="Generate", variant="primary", scale=1)  # variant 设置按钮的颜色主题
                with gr.Row():
                    dropdown1 = gr.Dropdown(["1", "2", "3", "4"], label="Style1")
                    dropdown2 = gr.Dropdown(["1", "2", "3", "4"], label="Style2")
        # 下半部分是第二块水平布局
        with gr.Row():
            # 左边的垂直布局
            with gr.Column():
                with gr.Row():
                    dropdown3 = gr.Dropdown(["1", "2", "3"], label="Sampling method")
                    slider1 = gr.Slider(minimum=0, maximum=100, label="Sampling steps")

                checkboxgroup = gr.Checkboxgroup(["Restore faces", "Tiling", "H fix"], label="")

                with gr.Row():
                    slider2 = gr.Slider(minimum=0, maximum=100, label="Width")
                    slider3 = gr.Slider(minimum=0, maximum=100, label="Batch count")

                with gr.Row():
                    slider4 = gr.Slider(minimum=0, maximum=100, label="Height")
                    slider5 = gr.Slider(minimum=0, maximum=100, label="Batch size")

                slider6 = gr.Slider(minimum=0, maximum=100, label="CFG scale")

                with gr.Row():
                    number1 = gr.Number(label="Seed", scale=5)
                    button5 = gr.Button(value="Randomize", min_width=1)
                    button6 = gr.Button(value="Reset", min_width=1)
                    checkbox1 = gr.Checkbox(label="Extra", min_width=1)

                dropdown4 = gr.Dropdown(["1", "2", "3", "4"], label="Script")
            # 右边的垂直布局
            with gr.Column():
                # 演示用的图片
                cheetahs = [
                    "https://upload.wikimedia.org/wikipedia/commons/0/09/TheCheethcat.jpg",
                    "https://nationalzoo.si.edu/sites/default/files/animals/cheetah-003.jpg",
                ]
                gallery = gr.Gallery(cheetahs, columns=3)
                with gr.Row():
                    button7 = gr.Button(value="🤣", min_width=1)
                    button8 = gr.Button(value="Save", min_width=1)
                    button9 = gr.Button(value="Zip", min_width=1)
                    button10 = gr.Button(value="Send to img2img", min_width=1)
                    button11 = gr.Button(value="Send to inpaint", min_width=1)
                    button12 = gr.Button(value="Send to extras", min_width=1)

                txt3 = gr.Textbox(lines=4, label="")
    # 第二个标签
    with gr.Tab(label="img2img"):
        pass
    # 可以展开或者隐藏
    with gr.Accordion():
        # 组
        with gr.Group():
            button13 = gr.Button(value="1")
            button14 = gr.Button(value="2")


demo.launch()
