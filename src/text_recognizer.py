from PIL import Image
import pytesseract
from image_enhancer import enhance
from abbreviation_recognicer import getAbbreviations
image_path = "img/example.png"
image_edit = enhance(image_path)
image_string = pytesseract.image_to_string(image_edit) 
print(getAbbreviations(image_string))

with open("text/text_result.txt", mode="w") as file:
    file.write(image_string)
    print("done")