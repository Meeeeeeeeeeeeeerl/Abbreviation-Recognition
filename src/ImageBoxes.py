import cv2
import pytesseract
import matplotlib.pyplot as plt
import json
def createImageBoxes(edited_image_path):
    img = cv2.imread(edited_image_path)
    json_file = open("abbreviations.json", "r")
    json_abb = json.load(json_file)

    data = pytesseract.image_to_data(img)

    for d in data.splitlines():
        d = d.split()
        try:
            if d[11] in json_abb:
                cv2.rectangle(img, (int(d[6]), int(d[7])), (int(d[6]) + int(d[8]), int(d[7]) + int(d[9])),(255, 0, 0), 1)
        except:
            Exception
        
    plt.imshow(img)
    plt.savefig("img/plot.png")
    plt.show()