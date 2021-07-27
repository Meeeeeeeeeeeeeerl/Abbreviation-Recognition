import cv2
import pytesseract
import matplotlib.pyplot as plt
import json
from WordTrimmer import trimWord
def createImageBoxes(edited_image_path):

    # CV2s way of reading images uses a path as input
    img = cv2.imread(edited_image_path)

    # Reads the abbreviations.json and loads it
    json_file = open("abbreviations.json", "r")
    json_abb = json.load(json_file)

    # Convertss the image into data (for every recognized word it outputs an array of data)
    # Array contains the following information: [level, page_num, block_num, par_num, lin_num, word_num, left, top, width, height, conf, text]
    data = pytesseract.image_to_data(img)

    # The following steps are executed for every entry in data 
    for d in data.splitlines():
        d = d.split()
        try:
            # The word that PyTesseract finds is compared to all entries in the abbreviations.json
            word = d[11]

            # Checks if any word given from PyTesseract contains a word from the abbreviation.json. Python's contains function is case-sensitive. 
            # This method can be optimized. Currently it allows unintended abbreviations to be detected (e. g. "milkman", because it contains "km").
            for json_word in  json_abb:
                if word.__contains__(json_word):

                    # The rectangle is drawn onto the picture using the "left", "top", "width" and "height" parameter from PyTesseract
                    # The color is set to red and the thickness of the lines set to 2 to increase visibility.
                    cv2.rectangle(img, (int(d[6]), int(d[7])), (int(d[6]) + int(d[8]), int(d[7]) + int(d[9])),(255, 0, 0), 1)

                    # More elegant way would be to send these infos to the user directly. Since this is an MVP, it will have to do for now
                    print(word + " is short for: " + json_abb[word])
        except:
            Exception # :D

    # Shows the edited picture with the added rectangles. This is mainly for demonstration purposes, if used in an productive environment this probably wouldn't be the case     
    plt.imshow(img)

    # Saves the picture with added rectangles as a plot 
    plt.savefig("img/plot.png")
    plt.show()