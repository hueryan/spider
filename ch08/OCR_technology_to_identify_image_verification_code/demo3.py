from PIL import Image
import tesserocr
import numpy as np

img = Image.open('./imgs/captcha2.png')
img = img.convert('L')
# 灰度的阈值
threshold = 50
# 将图片转化为 NumPy 数组
array = np.array(img)
# print(array)
# 利用where方法对数组进行筛选和处理。灰度大于阈值的图片的像素设置为255，表示白色，否则设置为0，表示黑色
array = np.where(array > threshold, 255, 0)
# print(array)

# 将 NumPy 数组转换为 PIL 的 Image 对象
# 将NumPy数组转换为PIL图像对象，但需要确保数据类型正确。
img = Image.fromarray(array.astype('uint8'))
img.show()
print(tesserocr.image_to_text(img))