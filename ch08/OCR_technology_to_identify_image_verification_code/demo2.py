from PIL import Image
import tesserocr
import numpy as np

img = Image.open('./imgs/captcha2.png')

# 转化为数组，查看维度
# 三维数组，38图片高；112图片宽；4每个像素点的表示向量，代表R、G、B、A（透明度）
print(np.array(img).shape)
print(img.mode)

# 将RGBA转化为L，即把图片转化为灰度图像。
img = img.convert('L')
img.show()

# 传入1，把图片二值化处理
img = img.convert('1')
img.show()

result = tesserocr.image_to_text(img)
print(result)