import json

def getAbbreviations(input):
    input_list = input.split()
    json_file = open("abbreviations.json", "r")
    data = json.load(json_file)
    result = []
    for x in input_list:
        try:
            print("The abbreviation " + x + " means: " + data[x])
            result.append([x, data[x]])
        except:
            KeyError
    json_file.close
    return result

        

