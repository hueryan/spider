import time
import re
import tesserocr
import numpy as np
from retrying import retry
from selenium import webdriver
from io import BytesIO
from PIL import Image
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

url = 'https://captcha7.scrape.center/'

def preprocess(image):
    image = image.convert('L')
    array = np.array(image)
    array = np.where(array > 130, 255, 0)
    image = Image.fromarray(array.astype('uint8'))
    return image

@retry(stop_max_attempt_number=10, retry_on_result=lambda x:x is False)
def login():
    browser.get(url)
    # 找两个输入框
    browser.find_element(By.CSS_SELECTOR, '.username input[type="text"]').send_keys('admin')
    browser.find_element(By.CSS_SELECTOR, '.password input[type="password"]').send_keys('admin')
    # 找到验证码图片元素
    captcha = browser.find_element(By.CSS_SELECTOR, '#captcha')
    # 转化为图片对象
    image = Image.open(BytesIO(captcha.screenshot_as_png))
    # image.show()
    # 去噪
    image = preprocess(image)
    # image.show()
    captcha = tesserocr.image_to_text(image)
    # 使用正则表达式移除 captcha 字符串中的所有非字母数字字符
    # [^A-Za-z0-9] 表示匹配 "非字母或数字" 的字符
    # re.sub 的作用是将这些字符替换为空字符串（即删除）
    captcha = re.sub('[^A-Za-z0-9]', '', captcha)
    browser.find_element(By.CSS_SELECTOR, '.captcha input[type="text"]').send_keys(captcha)
    browser.find_element(By.CSS_SELECTOR, '.login span').click()

    try:
        # 等待登录成功
        WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//h2[contains(.,"登录成功")]')))
        time.sleep(5)
        browser.close()
        return True
    except TimeoutException:
        return False

if __name__ == '__main__':
    browser = webdriver.Chrome()
    login()
