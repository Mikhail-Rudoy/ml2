def readFile(filename):
    result = open(filename, "r").readlines()
    for i in range(len(result)):
        result[i] = result[i].strip()
    return " \n ".join(result)

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

def convertLine(line):
    result = makeLink(boldify(line))
    return result

def listToWebPage(lines):
    return "<p>" + "</p>\n<p>".join(lines.split("\n")) + "</p>\n"

def convertFile(filename):
    print listToWebPage(convertLine(readFile(filename)))

convertFile("markup.txt")
