import cv2
import pytesseract
import matplotlib.pyplot as plt
import json
import config as cfg
def createImageBoxes(img, image_name):

    # Reads the abbreviations.json and loads it
    json_file = open("abbreviations.json", "r")
    json_abb = json.load(json_file)

    # Convertss the image into data (for every recognized word it outputs an array of data)
    # Array contains the following information: [level, page_num, block_num, par_num, lin_num, word_num, left, top, width, height, conf, text]
    data = pytesseract.image_to_data(img, lang="deu")

    # The following steps are executed for every entry in data 
    for d in data.splitlines():
        d = d.split()

        # If imageBoxesMode is set to ALL, it will draw a rectangle around every word found
        if cfg.imageBoxes["imageBoxesMode"] == "ALL":
            try:
                cv2.rectangle(img, (int(d[6]), int(d[7])), (int(d[6]) + int(d[8]), int(d[7]) + int(d[9])),(0, 0, 255), 1)
            except:
                Exception # :D
        else:
            try:
                # The word that PyTesseract finds is compared to all entries in the abbreviations.json
                word = d[11]

                # Checks if any word given from PyTesseract contains a word from the abbreviation.json. Python's contains function is case-sensitive. 
                # This method can be optimized. Currently it allows unintended abbreviations to be detected (e. g. "milkman", because it contains "km").
                for json_word in  json_abb:
                    if word.__contains__(json_word):
                        # The rectangle is drawn onto the picture using the "left", "top", "width" and "height" parameter from PyTesseract
                        # The color is set to red and the thickness of the lines set to 2 to increase visibility.
                        cv2.rectangle(img, (int(d[6]), int(d[7])), (int(d[6]) + int(d[8]), int(d[7]) + int(d[9])),(0, 0, 255), cfg.imageBoxes["borderThickness"])

                        # More elegant way would be to send these infos to the user directly. Since this is an MVP, it will have to do for now
                        print(word + " is short for: " + json_abb[word])
            except:
                Exception # :D

    # Shows the edited picture with the added rectangles. It needs to convert to RGB color scheme first. cv2 uses BGR, matplotlib uses RGB.
    img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)     
    plt.imshow(img_RGB)

    # Saves the picture with added rectangles as a plot 
    plt.savefig("output/" + image_name + "-plot.png", dpi=300)
    plt.show()