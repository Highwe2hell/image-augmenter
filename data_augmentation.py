import os
import cv2
import imgaug.augmenters as iaa
from PIL import Image
from tqdm import tqdm

# 输入数据集的根目录
input_root_folder = r'data\tomato'

# 输出文件夹路径
output_root_folder = r'data\augmented_data'

# 如果输出文件夹不存在，则创建
os.makedirs(output_root_folder, exist_ok=True)

# 定义数据增强操作
augmenter = iaa.Sequential([
    iaa.Fliplr(0.5),  # 50% 的概率水平翻转
    iaa.Flipud(0.2),  # 20% 的概率垂直翻转
    iaa.Affine(rotate=(-20, 20)),  # 随机旋转 -20 到 20 度
    iaa.Affine(translate_percent={"x": (-0.15, 0.15), "y": (-0.15, 0.15)}),  # 随机平移
    iaa.Affine(scale=(0.9, 1.1)),  # 随机缩放 90% 到 110%
    iaa.Multiply((0.8, 1.2)),  # 调整亮度
    iaa.LinearContrast((0.8, 1.2)),  # 调整对比度
    iaa.AddToHueAndSaturation((-10, 10)),  # 调整色调和饱和度
    iaa.GaussianBlur(sigma=(0, 0.8)),  # 添加高斯模糊
    iaa.AdditiveGaussianNoise(scale=(0, 0.02 * 255)),  # 添加轻微高斯噪声
    iaa.OneOf([
        iaa.ElasticTransformation(alpha=30, sigma=5),  # 弹性变换
        iaa.PiecewiseAffine(scale=(0.01, 0.03))  # 仿射变换
    ]),
    iaa.Crop(percent=(0, 0.05)),  # 随机裁剪
    iaa.CoarseDropout(0.05, size_percent=0.02),  # 随机遮挡
    iaa.GammaContrast((0.7, 1.5)),  # 伽马校正
])


def augment_image(image_path, augmenter, output_folder, num_augments=20):
    """读取图像，并生成多张增强后的图像"""
    # 读取图像
    image = cv2.imread(image_path)
    if image is None:
        print(f"无法读取图像：{image_path}")
        return
    # 转换为 RGB 格式
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # 生成指定数量的增强图像
    for i in range(num_augments):
        # 应用数据增强
        augmented_image = augmenter(image=image)
        # 保存增强后的图像
        output_filename = os.path.join(
            output_folder, f"{os.path.splitext(os.path.basename(image_path))[0]}_aug_{i}.jpg"
        )
        Image.fromarray(augmented_image).save(output_filename)


# 自动遍历数据集目录，获取所有类别文件夹
for root, dirs, files in os.walk(input_root_folder):
    if not dirs:  # 只处理没有子目录的文件夹（即叶子节点文件夹）
        parent_folder = os.path.basename(os.path.dirname(root))
        category_folder = os.path.basename(root)

        # 在输出目录中为每个类别创建对应的子文件夹
        output_folder = os.path.join(output_root_folder, parent_folder, category_folder)
        os.makedirs(output_folder, exist_ok=True)

        # 获取当前文件夹中的所有图像文件
        image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

        # 使用 tqdm 显示进度条
        for filename in tqdm(image_files, desc=f"正在处理 {parent_folder}/{category_folder}", ncols=80):
            input_path = os.path.join(root, filename)
            # 生成增强后的图像
            augment_image(input_path, augmenter, output_folder, num_augments=10)

print("数据增强完成。")
