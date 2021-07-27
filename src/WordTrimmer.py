# Removes given characters from a string. PyTesseract recognizes any word with extra symbols as one (e. g. "etc.)"), which would't allow it to be recognized.
# This is not elegant, but changing it has other technical implications that are not optimal either.
def trimWord(word):
    characters = [",", ".", "(", ")", '"', "'"]
    for c in characters:
        word = word.replace(c, "")
    return word