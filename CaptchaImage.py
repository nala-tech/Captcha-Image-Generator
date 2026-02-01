'''https://www.youtube.com/watch?v=O70FuH2LhNg'''

from captcha.image import ImageCaptcha
from io import BytesIO

captcha_text = 'Captcha Image' 

image = ImageCaptcha(width = 280, height = 90)
data = image.generate(captcha_text)  
image.write(captcha_text, 'CAPTCHA.png')

