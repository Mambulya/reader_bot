""""
the oop version
"""

import pytesseract as tess
from numpy import size
from PIL import Image, ImageDraw, ImageFont
from data import fonts, colors_rgb, IntPaper, LinePaper, A4
from itertools import groupby


class Reader_bot:
    def __init__(self, paper='graph', color='purple-blue', font=0):

        self.image = None
        self.lines = None
        self.start_text = None

        self.COLOR = colors_rgb[color]  # get a tuple already
        self.FONT = font

        if paper == 'lined':
            self.PAPER = LinePaper
        elif paper == 'A4':
            self.PAPER = A4
        else:
            self.PAPER = IntPaper

        self.size = self.PAPER.DIMENSIONS[1][self.FONT]

    def get_text(self, path: str):
        """
        reads text IN RUSSIAN from image
        :param: path : path to an image with text
        :return: image (PIL instance), text in russian from image
        """

        tess.pytesseract.tesseract_cmd = r"C:\Users\Anya\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
        img = Image.open(path)

        # читаем текст с картинки
        self.start_text = tess.image_to_string(img, lang='rus').replace("\n", " ")

        # bot cannot read the text
        if (not self.start_text) or (self.start_text == ''):
            raise ValueError('Empty notes')

        del img

    def prepare_text(self, own_text=None):
        """
        prepare text: clean from unnecessary signs, make lines according to paper frame and line break\n
                1. split text on paragraphs
                2. split every paragraph on lines

        :return: clean, ready text for putting on background, broken on lines
        :type: returns list of lines
        """
        if own_text:
            self.start_text = own_text

        # так как под знаками =, ® подразумаваются значки выделения пунктов, то заменим их на ">"
        samples = self.start_text.maketrans("=®", "> >")

        # заменяем все неправильные знаки
        start_text = self.start_text.translate(samples).replace("- ", "")

        line = self.PAPER.DIMENSIONS[0][self.FONT]  # how much signs 1 line would contain
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
        self.lines = [el for el, _ in groupby(lines)]
        del lines
        del start_text
        del text_length

    def put_text(self):
        """
        puts handwriting text on paper
        ** default text font is Russian

        :return: PIL instance - image with handwriting text on it
        """

        # if we didn't do the function "get_text()"

        image = Image.open(self.PAPER.PATH).convert("RGB")
        w, h = size(image)
        w *= 2
        h *= 2
        image = image.resize((w, h))

        tool = ImageDraw.Draw(image)
        font = ImageFont.truetype("FONTS\\" + fonts[self.FONT] + " Font4You.ttf", size=self.size)

        x_start = self.PAPER.DIMENSIONS[2]
        y = 0

        if self.PAPER.PATH == r"D:\PYTHON\fineReader_bot\BACKs\good\inLine.jpg" and self.FONT == 0:
            self.PAPER.Y_POS = [y - 10 for y in self.PAPER.Y_POS]

        for line in self.lines:
            tool.multiline_text((x_start, self.PAPER.Y_POS[y]), line, fill=self.COLOR, font=font)
            y += 1

        self.image = image

        del tool
        del font
        del y
