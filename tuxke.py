from PIL import Image

# 打开原始图像文件
original_image = Image.open("证件照.jpg")

# 设置目标图像大小
target_size = (150, 200)

# 缩放图像
resized_image = original_image.resize(target_size)

# 保存缩放后的图像
resized_image.save("resized_image.jpg")

print("图像已成功缩放并保存为 resized_image.jpg")
