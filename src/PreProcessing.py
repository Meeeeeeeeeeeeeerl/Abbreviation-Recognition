from PIL import Image, ImageEnhance

def enhance(image_path, edited_image_path):

    # Open the image and save it to the variable
    img = Image.open(image_path)

    # Increases the sharpness and contrast of the image to help the text recognition
    enhancer_sharp = ImageEnhance.Sharpness(img)
    enhancer_contrast = ImageEnhance.Contrast(img)

    img_edit = enhancer_sharp.enhance(25.0)
    img_edit = enhancer_contrast.enhance(3.0)

    # Saves the edited image to the given path
    img_edit.save(edited_image_path)

    # Returns edited image
    return img_edit