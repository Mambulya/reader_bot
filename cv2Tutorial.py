import cv2
from PIL import Image

bc = Image.fromarray(cv2.imread("BACKs/bc1.jpg"))

bc.resize((1722, 2160)).show()