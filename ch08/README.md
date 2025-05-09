# 验证码的识别

## 使用OCR技术识别图形验证码

**安装 tesserocr** [_](https://setup.scrape.center/tesserocr) 

[Tesseract](https://github.com/tesseract-ocr/tesseract)  

`conda install -c conda-forge tesserocr`  

安装retrying

- demo1：识别图片

- demo2：图片的处理

  image.mode属性

  ​	1：像素用1位表示，Python中表示为True 或 False，即二值化。

  ​	L：像素用8位表示，取值 0~255，表示灰度图像，数字越小，颜色越黑。

  ​	P：像素用8位表示，即调色板数据

  ​	RGB：像素用 3×8 位表示，即真彩色。

  ​	RGBA：像素用 4×8 位表示，即有透明通道的真彩色。

  ​	CMYK：像素用 4×8 位表示，即印刷四色模式。

  ​	YCbCr：像素用 3×8 位表示，即彩色书品格式。

  ​	I：像素用32位整型表示。

  ​	F：像素用32位浮点型表示。

- demo3：处理图片删除干扰值。

- demo4：登录验证

## 使用OpenCV识别滑动验证码的缺口

`pip install opencv-python` [_](https://setup.scrape.center/opencv-python) 

- 高斯模糊：去除图片的噪声，将图片模糊化。

  ```py
  def GaussianBlur(src, ksize, sigmaX, dst=None, sigmaY=None, borderType=None)
  ```

  src:处理图片

  ksize：高斯滤波处理所用的高斯内核大小，传入元组，包含x,y两元素

  sigmaX：高斯内核函数在X方向上的标准偏差。

  sigmaY：高斯内核函数在Y方向上的标准偏差。若为0，就将他设置为sigmaX；若X和Y都为0，通过ksize计算出sigmaX，sigmaY

- 边缘检测：找出缺口位置

  ```py
  def Canny(image, threshold1, threshold2, edges=None, apertureSize=None, L2gradient=None)
  ```

  image：预处理图片

  threshold1，threshold2：阈值，分别为最小最大判定临界点。

  apertureSize：应用查找图片渐变的索贝尔内核大小

  L2gradient：查找梯度幅度的方式。

- 轮廓提取：

  ```py
  def findContours(image, mode, method, contours=None, hierarchy=None, offset=None)
  ```

  image：图片

  mode：定义轮廓的检索模式，详情见OpenCV官方文档中对RetrievalModes的介绍

  method：用于定义轮廓的近似方法。详情见OpenCV官方文档中对ContourApproximationModes的介绍

- 外接矩阵：计算出轮廓的外界矩形，以便我们根据面积、周长等参数判断提取到的轮廓是否为目标缺口轮廓。

  ```py
  def boundingRect(arrat)
  ```

  array:可以是一个灰度图或者2D点集，这里传入轮廓信息。

-  轮廓面积

  ```py
  def contourArea(contour, oriented=None)
  ```

  contour：轮廓信息

  oriented：方向标识符，默认False。若取True，则该方法返回一个带符号的面积值，正负取决于轮廓的方向（顺、逆时针）。若去False，返回绝对值。

- 轮廓周长

  ```py
  def arcLength(curve, closed)
  ```

  curve：轮廓信息

  closed：轮廓是否封闭

- demo：缺口识别

  

## 使用深度学习识别图形验证码

安装 [_](https://setup.scrape.center/pytorch) [官网](https://pytorch.org/get-started/previous-versions/) 

captcha 验证码生成器 `pip install captcha` 

先执行generate.py 修改 count和path 当TRAIN_DATASET_PATH 时count足够大（10w），EVAL_DATASET_PATH时，count设置3000就可以

运行train，后面可以进行预测

## 使用深度学习识别滑动验证码的缺口

```
pip install matplotlib tensorflow==2.8.0 terminaltables tensorboard pillow tqdm loguru
```

执行collect.py截取图片
