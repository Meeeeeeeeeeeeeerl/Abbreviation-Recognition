import cv2
import pytesseract
import matplotlib.pyplot as plt
import json
from WordTrimmer import trimWord
def createImageBoxes(edited_image_path):
    img = cv2.imread(edited_image_path)
    json_file = open("abbreviations.json", "r")
    json_abb = json.load(json_file)

    data = pytesseract.image_to_data(img)

    for d in data.splitlines():
        d = d.split()
        try:
            word = d[11]
            word = trimWord(word)
            if word in json_abb:
                cv2.rectangle(img, (int(d[6]), int(d[7])), (int(d[6]) + int(d[8]), int(d[7]) + int(d[9])),(255, 0, 0), 3)
                print(word + " is short for: " + json_abb[word])
        except:
            Exception # :D
        
    plt.imshow(img)
    plt.savefig("img/plot.png")
    plt.show()