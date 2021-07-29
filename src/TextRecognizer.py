import pytesseract
from preprocess import preprocess
from createImageBoxes import createImageBoxes
import config as cfg

# Run this class for the OCR magic

# Path of the image that the OCR is working with
image_option = cfg.general["imageFolder"] # Choose the picture quality using this parameter. Has to match the folder name
image_path = "img/" + image_option + "/picture.png"

# Path of the edited image that the OCR is creating
edited_image_path = image_path.replace(".png", "-edited.png")

# Pre-processing the image
image_edit = preprocess(image_path, edited_image_path)

# Recognizes and marks the words written in the abbreviations.json
if cfg.imageBoxes["imageBoxesMode"] == "ALL" or cfg.imageBoxes["imageBoxesMode"] == "ABBREVIATIONS":
    createImageBoxes(edited_image_path)

# Converts the edited image to a string using PyTesseract
image_string = pytesseract.image_to_string(image_edit, lang="deu") 

# Saves the string to a text file
with open("text/text-result-" + image_option + ".txt", mode="w", encoding="utf-8") as file:
    file.write(image_string)
    print("done")