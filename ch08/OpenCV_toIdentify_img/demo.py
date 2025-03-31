import cv2

GAUSSIAN_BLUR_KERNEL_SIZE = (5, 5)
GAUSSIAN_BLUR_SIGMA_X = 0
CANNY_THRESHOLD1 = 200
CANNY_THRESHOLD2 = 400
PIC_LOC = 'imgs/captcha.png'
PIC_SAV = 'imgs/captcha-label.png'
# 传入待处理图片，返回高斯滤波处理后的图片信息
def get_gaussian_blur_image(image):
    return cv2.GaussianBlur(image, GAUSSIAN_BLUR_KERNEL_SIZE, GAUSSIAN_BLUR_SIGMA_X)

# 传入待处理图片，返回边缘检测处理后的图片信息
def get_canny_image(image):
    return cv2.Canny(image, CANNY_THRESHOLD1, CANNY_THRESHOLD2)

# 传入待处理图片，返回提取得到的轮廓信息
def get_contours(image):
    contours, _ = cv2.findContours(image, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    return contours

image_raw = cv2.imread(PIC_LOC)
# 获取宽高信息
image_height, image_width, _ = image_raw.shape
image_gaussian_blur = get_gaussian_blur_image(image_raw)
image_canny = get_canny_image(image_gaussian_blur)
# 各个边缘的轮廓信息
contours = get_contours(image_canny)

# 定义目标轮廓的面积下限、上限
def get_contour_area_threshold(image_width, image_height):
    contour_area_min = (image_width * 0.15) * (image_height * 0.25) * 0.8
    contour_area_max = (image_width * 0.15) * (image_height * 0.25) * 1.2
    return contour_area_min, contour_area_max

# 定义目标轮廓的周长下限、上限
def get_arc_length_threshold(image_width, image_height):
    arc_length_min = ((image_width * 0.15) + (image_height * 0.25)) * 2 * 0.8
    arc_length_max = ((image_width * 0.15) + (image_height * 0.25)) * 2 * 1.2
    return arc_length_min, arc_length_max

# 定义缺口位置的偏移量下限和上限
def get_offset_threshold(image_width):
    offset_min = 0.2 * image_width
    offset_max = 0.85 * image_width
    return offset_min, offset_max

contour_area_min, contour_area_max = get_contour_area_threshold(image_width, image_height)
arc_length_min, arc_length_max = get_arc_length_threshold(image_width, image_height)
offset_min, offset_max = get_offset_threshold(image_width)
offset = None
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    if contour_area_min < cv2.contourArea(contour) < contour_area_max and \
            arc_length_min < cv2.arcLength(contour, True) < arc_length_max and \
            offset_min < cv2.arcLength(contour, True) < offset_max:
        cv2.rectangle(image_raw, (x, y), (x + w, y + h), (0, 0, 255), 2)
        offset = x

cv2.imwrite(PIC_SAV, image_raw)
print(f'{offset = }')