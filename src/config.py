general = {

    # Name of the picture located in the img-Folder. DO NOT add the file extension, only enter the name
    "imageName": "normal",

    # Enable Or disable PreProcessing. Options are True, False
    #"enablePreProcessing": False
}

preProcessing = {

    # Change intensity of denoising. Options are full numbers between 0-100
    #"denoising": 3,

    # Choose method to use for binarization. Options are MEAN, GAUSSIAN. MEAN uses the mean value of the neighbourhood area, GAUSSIAN uses the weighted sum of the neighbourhood area.
    #"binarizationMethod": "GAUSSIAN",

    # Choose the maximum skew angle. Options are full numbers between 0-100
    #"maxSkew": 10
}

imageBoxes = {

    # Choose which words should be highlighted. Options are ALL, ABBREVIATIONS, NONE
    "imageBoxesMode": "ABBREVIATIONS",

    # Choose the thickness of the border. Options are full numbers from 0-100
    "borderThickness": 1
}

