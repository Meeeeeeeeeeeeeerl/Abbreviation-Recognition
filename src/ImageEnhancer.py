from PIL import Image, ImageEnhance

def enhance(image_path, edited_image_path):
    img = Image.open(image_path)

    enhancer_sharp = ImageEnhance.Sharpness(img)
    enhancer_contrast = ImageEnhance.Contrast(img)

    img_edit = enhancer_sharp.enhance(25.0)
    img_edit = enhancer_contrast.enhance(2.0)

    img_edit.save(edited_image_path)

    return img_edit