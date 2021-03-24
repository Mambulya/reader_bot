import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

img = cv2.imread("background.jpg")

def put_text(img: np.array, txt: str):
    im = Image.fromarray(img)

    font_size = 80
    font = ImageFont.truetype("Abram Font4You.ttf", size=font_size)

    # здесь узнаем размеры сгенерированного блока текста
    #w, h = draw.textsize(txt, font=font)

    y_pos = 78
    draw = ImageDraw.Draw(im)

    # теперь можно центрировать текст
    #draw.text((int((img.shape[1] - w) / 2), y_pos), txt, fill='rgb(0, 0, 0)', font=font)
    draw.text( (70, y_pos), txt, fill='rgb(0, 0, 0)', font=font)

    img = np.asarray(im)
    return img


img = put_text(img, 'Тут мой код')
cv2.imshow('Result', img)
d = cv2.waitKey()

if d == ord('s'):
    print("saving....")
    cv2.imwrite('savedBackground.png', img)
    print("saved")