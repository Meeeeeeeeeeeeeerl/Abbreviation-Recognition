from PIL import Image, ImageEnhance
import pytesseract

def enhancer(image_path):
    img = Image.open(image_path)

    enhancer_sharp = ImageEnhance.Sharpness(img)
    enhancer_contrast = ImageEnhance.Contrast(img)

    img_edit = enhancer_sharp.enhance(25.0)
    img_edit = enhancer_contrast.enhance(2.0)

    img_edit.save("img/edited_image.png")

    return pytesseract.image_to_string(img_edit, lang="deu")