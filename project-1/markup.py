def readFile(filename):
    result = open(filename).readlines()
    for i in range(len(result)):
        result[i] = result[i].strip()
    return result

def boldify(line):
    sofar = "";
    d = "<b>"
    for c in line:
        if c != "*":
            sofar = sofar + c
        elif d == "<b>":
            sofar = sofar + d
            d = "</b>"
        else:
            sofar = sofar + d
            d = "<b>"
    if d == "</b>":
        sofar = sofar + d
    return sofar

def makeLink(line):
    words = line.split(" ")
    for i in range(len(words)):
        if len(words[i]) > 4 and words[i][-4:] in [".com", ".org", ".edu", ".net", ".xxx"]:
            address = words[i]
            if len(words[i]) < 8 or words[i][:9] != "https://":
                address = "http://" + address
            words[i] = "<a href=" + address + ">" + words[i] + "</a>"
    return " ".join(words)

def convertLineList(lines):
    result = lines
    for i in range(len(lines)):
        result[i] = makeLink(boldify(result[i]))
    return result

def listToWebPage(lines):
    return "<p>" + "</p>\n<p>".join(lines) + "</p>\n"

def convertFile(filename):
    print listToWebPage(convertLineList(readFile(filename)))

convertFile("markup.txt")
