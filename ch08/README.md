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
