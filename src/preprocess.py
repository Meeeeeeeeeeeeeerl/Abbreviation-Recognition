import cv2
from deskew import deskew
import numpy
import config as cfg
def preprocess(image_name):

    # Opens the image and save it to the variable
    img = cv2.imread("img/"+ image_name + ".png")

    if cfg.general["enablePreProcessing"] == False:
        return img
        
    # Changes the color of the image to a greyscale.
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("output/" + image_name + "-grey.png", img)

    # Denoises the image and saves the denoised image
    img = cv2.fastNlMeansDenoising(img, h=cfg.preProcessing["denoising"])
    cv2.imwrite("output/" + image_name + "-denoised.png", img)

    # Applies Binarization using an adaptive threshold. It decides if a pixel is black or white using on of two algorithms. 
    # MEAN uses the mean value of the neighbourhood area, GAUSSIAN uses the weighted sum of the neighbourhood area.

    if cfg.preProcessing["binarizationMethod"] == "MEAN":
        img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)   
        cv2.imwrite("output/" + image_name + "-binarized-MEAN.png", img)
    else:
        img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)   
        cv2.imwrite("output/" + image_name + "-binarized-GAUSS.png", img)

    # Deskews the image and saves the deskewed image
    img = deskew(img, cfg.preProcessing["maxSkew"])
    cv2.imwrite("output/" + image_name + "-deskewed.png", img)

#    kernel = numpy.ones((2,2),numpy.uint8) Not included as thinning is not a one-for-all solution. It needs to be more flexible based on text size.
#    img = cv2.erode(img,kernel,iterations = 1)
#    cv2.imwrite("img/picture-thinned.png", img)
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    # Returns edited image
    return img