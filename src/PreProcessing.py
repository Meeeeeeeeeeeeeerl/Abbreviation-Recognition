import cv2

def enhance(image_path, edited_image_path):

    # Opens the image and save it to the variable
    img = cv2.imread(image_path)

    # Changes the color of the image to a greyscale.
    img_edit = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Applies Binarization using an adaptive threshold. It decides if a pixel is black or white using its position and neighbour pixels (Gaussian Adaptive Threshold)
    img_edit = cv2.adaptiveThreshold(img_edit,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)   
    cv2.imwrite("img/picture-binarized.png", img_edit)
    # Saves the edited image to the given path
    cv2.imwrite(edited_image_path, img_edit)

    # Returns edited image
    return img_edit