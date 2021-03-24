"""
This is the main file of the bot project. There is transferring images to text

Lists:

Notes: replace "=", "®" to an unified sign
>   измерить время выполнения
>   оформить в ООП стиле
>   устранить минусы:  цвет рукописи, сделать расположение каждой строчки строко по разлиновке листа
>   загрузать линейную и пустую разлиновку

*** Supposed fonts : 0-3
"""
import pytesseract as tess
from cv2 import imread, imshow, imwrite, waitKey
from numpy import size, array
from PIL import Image, ImageDraw, ImageFont
from os import listdir
from data import fonts, colors_rgb

paper = input("what kind of paper do you want? k/l/b\n")

if paper == 'k':
    from data import IntPaper as paper

    FILE = r"D:\PYTHON\fineReader_bot\BACKs\good\graph.png"
elif paper == 'l':
    from data import LinePaper as paper

    FILE = r"D:\PYTHON\fineReader_bot\BACKs\good\lined.png"
else:
    from data import A4 as paper

    FILE = r"D:\PYTHON\fineReader_bot\BACKs\good\A4.png"

FONT = int(input("what kind of font do you want? 0-3\n"))


def get_text(path):
    """
    reads text IN RUSSIAN from image
    :param path: image path

    :return: image (PIL instance), text in russian from image
    """

    tess.pytesseract.tesseract_cmd = r"C:\Users\Anya\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
    img = Image.open(path)

    # читаем текст с картинки
    start_text = tess.image_to_string(img, lang='rus').replace("\n", " ")

    return img, start_text


def prepare_text(start_text: str):
    """
    prepare text: clean from unnecessary signs, make lines according to paper frame and line break\n
            1. split text on paragraphs
            2. split every paragraph on lines

    :param start_text: text from GET_TEXT()

    :return: clean, ready text for putting on background, broken on lines
    :type: returns list of lines
    """

    # так как под знаками =, ® подразумаваются значки выделения пунктов, то заменим их на ">"
    samples = start_text.maketrans("=®", "> >")

    # заменяем все неправильные знаки
    start_text = start_text.translate(samples).replace("- ", "")

    line = paper.DIMENSIONS[0][FONT]  # how much signs 1 line would contain
    paragraphs = start_text.split("  ")
    lines = []
    paragraphs = ["    " + p for p in paragraphs]

    for paragraph in paragraphs:
        text_length = len(paragraph)
        times = text_length // line
        end = text_length % line

        for time in range(times):
            lines.append(paragraph[time * line:time * line + line])
        lines.append(paragraph[-end:])
    del paragraphs
    del samples
    return lines


img, text_0 = get_text(r"C:\Users\Anya\Pictures\book.png")
final_text = prepare_text(text_0)


def put_text(txt: list, font: int, color: str, bc="BACKs\\good\\graph.png", size_arg=50):
    """
    puts handwriting text on paper
    ** default text font is Russian

    :param bc: path of background
    :param size_arg: size of text
    :param color: color of text
    :param txt: notes text
    :param font: handwriting font

    :return: PIL instance - image with handwriting text on it
    """

    image = Image.open(bc).convert("RGB")
    w, h = size(image)
    w *= 2
    h *= 2
    image = image.resize((w, h))

    tool = ImageDraw.Draw(image)
    font = ImageFont.truetype("FONTS\\" + fonts[font] + " Font4You.ttf", size=size_arg)

    x_start = paper.DIMENSIONS[2]
    y = 0

    if FILE == r"D:\PYTHON\fineReader_bot\BACKs\good\lined.png" and FONT == 0:
        paper.Y_POS = [y - 10 for y in paper.Y_POS]

    for line in txt:
        tool.multiline_text((x_start, paper.Y_POS[y]), line, fill=colors_rgb[color], font=font)
        y += 1

    return image


img = put_text(final_text, FONT, 'blueM', bc=FILE, size_arg=paper.DIMENSIONS[1][FONT])

Image.show(img)

# imshow('Result', img)
#
# d = waitKey()
#
# if d == ord('s'):
#     print("saving....")
#     # сохраняет каждый результат под уникальным именем, соответствующим номеру
#     files = listdir(r"D:\PYTHON\fineReader_bot\RESULTS\tests")
#     imwrite('RESULTS/tests/inLine' + str(FONT) + '.png', img)
#     print("saved")
