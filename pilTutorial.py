from PIL import Image, ImageDraw, ImageFont
import numpy as np
from mainOOP import Reader_bot

"""
PIL library discovering
____________________________________________________
 Open an image 
1 way:                                              2 way:
        open: cv2                                           open: Image
        transform to array: Image                           transform to array: nuPy
        res: PIL obj                                        res: PIL obj
____________________________________________________




#---text opacity in PIL---


image = Image.open(r'BACKs\good\bcInt.png').convert("RGBA")
w, h = np.size(image)
w *= 2
h *= 2
image = image.resize((w, h))


txt = Image.new("RGBA", (w, h), (0, 0, 0, 0))

tool = ImageDraw.Draw(txt)
font = ImageFont.truetype(r"D:\PYTHON\fineReader_bot\FONTS\Abram Font4You.ttf", size=50)

y = 0
for line in book_text:
    tool.multiline_text((192, y_pos[y]), line, fill="#132C7D", font=font)
    y += 1

out = Image.alpha_composite(image, txt)

out.show()



#sample = Image.fromarray(cv2.imread('BACKs/background.jpg'))
""" """

def put_point(img, x, y):
    """ """ 
    :param img: a picture in massive type
    :param x: horizontal dimension
    :param y: vertical dimension
    :return: the image with drawn point
    """ """ 
    draw = ImageDraw.Draw(img)
    draw.point((x, y), fill='red')

    # img = np.asarray(img)
    return img


def put_text(img, txt):
    font = ImageFont.truetype("FONTS/Abram Font4You.ttf", size=80)

    y_pos = 80
    draw = ImageDraw.Draw(img)

    draw.text((70, y_pos), txt, fill='rgb(0, 0, 0)', font=font)

    return img

def put_text1(backImg: np.array, txt: list, font: int, color: str, size=50, paper="BACKs\\good\\bcInt.png"):
    """ """ 
    puts handwriting text on paper
    ** default text font is in Russian

    :param backImg: background image
    :param txt: notes text
    :param font: handwriting font
    :return: PIL instance - image with handwriting text on it
    """ """
    backImg = cv2.imread(paper)
    image = Image.fromarray(backImg).convert("RGBA")
    w, h = np.size(image)
    w *= 2
    h *= 2
    image = image.resize((w, h))

    for_txt = Image.new("RGBA", (w, h), (0, 0, 0, 0))

    tool = ImageDraw.Draw(for_txt)
    font = ImageFont.truetype("FONTS\\" + fonts[font] + " Font4You.ttf", size=size)

    y = 0

    for line in txt:
        tool.multiline_text((192, y_pos[y]), line, fill=colors_rgb[color], font=font)
        y += 1

    out = Image.alpha_composite(image, for_txt)

    return out


sample = Image.open(r"C:/Users\Anya\Pictures\PzpgoPqy-eM.jpg")
res = sample.crop((300, 70, 500, 200))  # x,y - the lefty uppermost coordinate
                                        # x1, y1 - the rightly lowest coordinate
res.show()

"""  """ 
x,y+ _ _ _ _ _
   |         |
   |         |
   | _ _ _ _ + x1, y1
""" """

box = (300, 70, 500, 200)
res = sample.crop(box).transpose(Image.ROTATE_180)
sample.paste(res, box)
sample.show()

new_sample = sample.resize((1280, 640))
new_sample.show()

sample.rotate(91).show()
"""


def check(pipcture_arg):
    print(pipcture_arg)
    res = Image.open(pipcture_arg).convert('L')
    res.show()