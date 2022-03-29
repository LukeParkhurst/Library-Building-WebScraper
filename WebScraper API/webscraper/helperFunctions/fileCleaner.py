# Helper function file purposely set up in a MicroServices architecture to reuse elements in different areas

"""
Helper function to clean files into more usable data
rawFile: parameter for the raw file to be cleaned, involves stripping white space
cleanFilePath: parameter for the path of 
"""
def fileClean(rawFile, cleanFilePath, writeOverClnFile = 0, removeStopWords = 0, removeDuplicates = 0):
    cleanFile = []

    # opens file and by line, strips white space
    with open(rawFile, "r") as file:
        for line in file:
            currentLine = line.strip()
            cleanFile.append(currentLine)

    # if user choices to write over the cleaned text file instead of appending more to it, otherwise just append
    if writeOverClnFile == 0:
        with open(cleanFilePath, "w") as f:
            f.write("")
        writeToFile(cleanFilePath, cleanFile)
    else:
        writeToFile(cleanFilePath, cleanFile)

# following DRY for writing to file
def writeToFile(cleanFilePath, cleanFile):
    for cleanedLine in cleanFile:
        try:
            with open(cleanFilePath, "a") as clnFile:
                clnFile.write(cleanedLine)
                clnFile.write("\n")
        except:
            print("Failed to write cleaned data to file")

def removeStopWords(cleanedFile):
    return

def removeDuplicates(cleanFile):
    return