

def trimWord(word):
    characters = [",", ".", "(", ")", '"', "'"]
    for c in characters:
        word = word.replace(c, "")
    return word