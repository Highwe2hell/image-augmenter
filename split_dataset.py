import os
import shutil
import random


def move_random_images(src_dir, dest_dir, percentage):
    """
    从源目录中随机选择指定比例的图片并移动到目标目录
    :param src_dir: 源目录（训练集目录），包含待划分的图像
    :param dest_dir: 目标目录（测试集目录），将被选择的图像移动到此目录
    :param percentage: 测试集所占比例（例如 0.2 表示 20%）
    """
    # 获取源目录中的所有图片文件
    all_images = [f for f in os.listdir(src_dir) if os.path.isfile(os.path.join(src_dir, f))]

    # 计算需要移动的图片数量
    num_images_to_move = int(len(all_images) * percentage)

    # 如果源目录图片数量不足，则调整数量
    num_images_to_move = min(num_images_to_move, len(all_images))

    # 随机选择图片
    images_to_move = random.sample(all_images, num_images_to_move)

    # 确保目标目录存在
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # 移动图片
    for image in images_to_move:
        src_image_path = os.path.join(src_dir, image)
        dest_image_path = os.path.join(dest_dir, image)
        shutil.move(src_image_path, dest_image_path)
        print(f"Moved: {image} -> {dest_dir}")


def main():
    """
    按照指定的类别和比例，将训练集中的一部分图像随机移动到测试集目录，进行数据集划分。
    """
    # 定义源目录（训练集）和目标目录（测试集）
    base_train_dir = 'data/tomato/train'
    base_test_dir = 'data/tomato/test'

    # 各类别的目录及其测试集划分比例
    categories = {
        'Tomato_Healthy': 0.2,  # 将 20% 的图像移动到测试集
        'Tomato__Target_Spot': 0.2,  # 将 20% 的图像移动到测试集
        'Tomato_Leaf_Mold': 0.2  # 将 20% 的图像移动到测试集
    }

    # 遍历每个类别，按照指定比例移动图片
    for category, percentage in categories.items():
        src_dir = os.path.join(base_train_dir, category)
        dest_dir = os.path.join(base_test_dir, category)

        print(f"\nProcessing category: {category} with {percentage * 100}% test split")
        move_random_images(src_dir, dest_dir, percentage)


if __name__ == "__main__":
    main()
