import tesserocr
from PIL import Image

image = Image.open('imgs/captcha1.png')
result = tesserocr.image_to_text(image)
print(result)
result = tesserocr.file_to_text('./imgs/captcha1.png')
print(result)
