from PIL import Image
import pytesseract

img = Image.open("img/all-star.jpg")
result = pytesseract.image_to_string(img)

with open("text/text_result.txt", mode="w") as file:
    file.write(result)
    print("done")