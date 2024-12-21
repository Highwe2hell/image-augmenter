# Image Augmenter

`Image Augmenter` 是一个用于图像数据预处理的工具集，包含数据集划分（Dataset Splitting）和图像增强（Data Augmentation）功能。它能够帮助你将数据集自动划分为训练集和测试集，并使用多种数据增强技术扩展训练数据集，提高深度学习模型的表现。

## 主要功能

### 1. 数据集划分

通过 `split_dataset.py` 脚本，可以将训练集中的一部分图像按指定比例随机移动到测试集目录，进行数据集划分。此功能通常用于准备训练和测试数据集。

### 2. 图像数据增强

使用 `imgaug` 库进行图像增强操作，支持：

- 水平翻转、垂直翻转
- 旋转、平移、缩放
- 亮度、对比度、色调调整
- 高斯噪声和模糊
- 随机裁剪、遮挡
- 弹性变换和仿射变换

通过这些增强操作，可以显著增加训练集的多样性，帮助模型更好地学习。

## 项目结构

```
image-augmenter/
├── data_augmentation.py  # 图像数据增强脚本
├── split_dataset.py      # 数据集划分脚本
├── requirements.txt      # 项目依赖
├── README.md             # 项目说明文档
```

## 安装

1. 克隆项目：

```bash
git clone https://github.com/your-username/image-augmenter.git
```

2. 安装依赖：

```bash
pip install -r requirements.txt
```

## 使用方法

### 1. 数据集划分

**`split_dataset.py`** 用于按比例将训练集中的一部分图像随机移动到测试集目录，进行数据集的划分。

- **输入：** 训练集文件夹路径、测试集文件夹路径、类别划分比例
- **输出：** 将指定比例的图像从训练集目录移动到测试集目录。

运行以下命令进行数据集划分：

```bash
python split_dataset.py
```

### 2. 图像数据增强

**`data_augmentation.py`** 用于对图像数据集进行增强操作。你可以根据需要自定义增强的操作和生成的图像数量。

- **输入：** 图像文件夹路径
- **输出：** 增强后的图像文件将保存在指定的输出文件夹。

运行以下命令进行图像增强：

```bash
python data_augmentation.py
```

### 示例

假设你的数据集目录结构如下：

```
data/
  tomato/
    train/
      Tomato_Healthy/
      Tomato_Target_Spot/
      Tomato_Leaf_Mold/
    test/
```

1. **数据集划分：** 运行 `split_dataset.py` 脚本，将 20% 的图像从 `train` 文件夹随机移动到 `test` 文件夹。
2. **图像数据增强：** 运行 `data_augmentation.py` 脚本，对 `train` 文件夹中的图像进行增强，并将增强后的图像保存到 `augmented_data` 文件夹。

### 依赖

以下是本项目的依赖库：

- Python 3.8
- `imgaug`
- `opencv-python`
- `Pillow`
- `tqdm`
- 其他依赖（已列出在 `requirements.txt`）

### 许可证

本项目使用 [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html) 许可证。