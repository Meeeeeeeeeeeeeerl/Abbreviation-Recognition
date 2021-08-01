# Abbreviation-Recognizer-MVP (v0.1)
### *Goal of the MVP*
The goal of the MVP is to detect given abbreviations in a picture using OCR.
It is my hope that it can serve as a "Getting Started" to OCR technology and its use in the future.

### *Set-up*
1. Install the latest (stable) version of Python (https://www.python.org/downloads/)
2. Clone the GitHub Repository 
3. Install PyTesseract (https://pypi.org/project/pytesseract/ or https://github.com/UB-Mannheim/tesseract/wiki (recommended)) 
This is a Python Wrapper for the Google-OCR Tesseract (https://github.com/tesseract-ocr/tesseract).
4. Add Python, the Python scripts folder and Tesseract to your PATH system variable
5. Install opencv-python (https://pypi.org/project/opencv-python/)

### Explanation on folder/files
img-folder: This folder contains more image folders. They are named after the type of picture you find inside:
- normal: normal example picture with no added visual effects
- noise: example picture with added noise
- lowContrast: example picture with reduced contrast
- skewed: example picture skewed by 10 degrees
- all: example picture with all of the above visual effects
- individual: empty folder for you to add your own picture (name has to be picture.png)

src-folder: This folder contains all the code written for this project:
- TextRecognizer: This is the main class. 
- createImageBoxes: This function creates rectangles around configured words
- deskew: This function can deskew an image
- preprocess: This function pre-processes an image to help increase accuracy of the OCR
- config: This file contains several configurations to try out

text-folder: This folder contains all the text-results created by the OCR </br>
README.md: The file you're reading right now ;) </br>
abbreviations.json: This file contains all the abbreviations the programm should search for


