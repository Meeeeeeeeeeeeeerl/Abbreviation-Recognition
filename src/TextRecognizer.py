import pytesseract
from preprocess import preprocess
from createImageBoxes import createImageBoxes
import config as cfg

# Run this class for the OCR magic

# Path of the image that the OCR is working with
image_name = cfg.general["imageName"]
image_path = "img/" + image_name + ".png"

# Pre-processing the image
image_edit = preprocess(image_name)

# Recognizes and marks the words written in the abbreviations.json
if cfg.imageBoxes["imageBoxesMode"] == "ALL" or cfg.imageBoxes["imageBoxesMode"] == "ABBREVIATIONS":
    createImageBoxes(image_edit, image_name)

# Converts the edited image to a string using PyTesseract
image_string = pytesseract.image_to_string(image_edit, lang="deu") 

# Saves the string to a text file
with open("output/text-result.txt", mode="w", encoding="utf-8") as file:
    file.write(image_string)
    print("done")