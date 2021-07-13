from PIL import Image
import pytesseract
from image_enhancer import enhance
from abbreviation_recognicer import getAbbreviations
from ImageBoxes import createImageBoxes

image_path = "img/example.png"
edited_image_path = "img/edited_image.png"

image_edit = enhance(image_path, edited_image_path)
createImageBoxes(image_path)
image_string = pytesseract.image_to_string(image_edit) 

with open("text/text_result.txt", mode="w") as file:
    file.write(image_string)
    print("done")