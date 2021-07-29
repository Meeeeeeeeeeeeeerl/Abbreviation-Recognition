import cv2

def enhance(image_path, edited_image_path):

    # Open the image and save it to the variable
    img = cv2.imread(image_path)
    img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_edit = cv2.adaptiveThreshold(img_grey,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)   

    # Saves the edited image to the given path
    cv2.imwrite(edited_image_path, img_edit)

    # Returns edited image
    return img_edit