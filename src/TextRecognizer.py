import pytesseract
from PreProcessing import enhance
from ImageBoxes import createImageBoxes

# Path of the image that the OCR is working with
image_path = "img/example.png"

# Path of the edited image that the OCR is creating
edited_image_path = image_path.replace(".png", "-edited.png")

# Pre-processing the image
image_edit = enhance(image_path, edited_image_path)

# Recognizes and marks the words written in the abbreviations.json
createImageBoxes(edited_image_path)

# Converts the edited image to a string using PyTesseract
image_string = pytesseract.image_to_string(image_edit, lang="deu") 

# Saves the string to a text file
with open("text/text_result.txt", mode="w") as file:
    file.write(image_string)
    print("done")