from PIL import Image
import pytesseract
from image_enhancer import enhancer
image_path = "img/example.png"
image_string = enhancer(image_path)

with open("text/text_result.txt", mode="w") as file:
    file.write(image_string)
    print("done")