from PIL import Image
import pytesseract
from ImageEnhancer import enhance
from ImageBoxes import createImageBoxes

image_path = "img/example.png"
edited_image_path = image_path.replace(".png", "-edited.png")

image_edit = enhance(image_path, edited_image_path)
createImageBoxes(edited_image_path)
image_string = pytesseract.image_to_string(image_edit) 

with open("text/text_result.txt", mode="w") as file:
    file.write(image_string)
    print("done")