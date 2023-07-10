import os.path
import markdown

def readFile(filename):
    filepath = os.path.join("app/pages/", filename)
    with open(filepath, "r", encoding="utf-8") as textFile:
        text = textFile.read()

    return {
        "text": markdown.markdown(text)
    }

def readRaw(filename):
    filepath = os.path.join("generated/", filename)
    with open(filepath, "r", encoding="utf-8") as textFile:
        text = textFile.read()
    return text

