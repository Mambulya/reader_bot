import  pytesseract as tess
from PIL import Image

tess.pytesseract.tesseract_cmd = r"C:\Users\Anya\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

img = Image.open("SAMPLES/so.png")
text = tess.image_to_string(img, lang='rus')

print(text.split("\n"))