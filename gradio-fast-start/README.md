# Gradio 初学

学习了 Gradio 中的各种输入、输出组件

在 block.py 文件中，尝试编写了一个 stable_diffusion 的 ui 界面出来

在安装好 python 环境和 pip 库的前提下，首先把 Gradio 库给下载好：

**Gradio** 库使你能够快速创建可分享的Web应用来展示机器学习模型。

```shell
pip install gradio
```

可能还用到了以下几个库：

- **Pandas**: Pandas是一个开源的、BSD许可的库，提供高性能、易用的数据结构和数据分析工具。

```shell
pip install pandas
```

- **NumPy**: NumPy是Python的一个科学计算库。它提供了一个高性能的多维数组对象，以及用于处理这些数组的工具。

```shell
pip install numpy
```

- **Matplotlib**: Matplotlib是一个Python 2D绘图库，可用于生成发布质量级别的图形，在Jupyter notebooks内部与NumPy一起使用效果非常好。

```shell
pip install matplotlib
```

- **OpenCV(cv2)**:  这将安装OpenCV的主要功能，适用于大多数应用。

```shell
pip install opencv-python
```

如果你还需要OpenCV的额外模块（如贡献包中的特征），你可以安装`opencv-contrib-python`：

```shell
pip install opencv-contrib-python
```

记得在使用这些命令之前，你可能需要确保你的`pip`是最新版本的，可以使用下面的命令进行升级：

```shell
pip install --upgrade pip
```

可以用`pip list`确保你成功下载了这些库：

```shell
pip list
```

