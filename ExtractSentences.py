import re

# ParseInput will parse a UTF8 encoded input text file at each new lines character
# and return an array containing each lines. Empty lines are ignored and case is removed.
def ParseInput(path):

    with open(path, 'r', encoding="utf-8") as f:

        data = f.read()
        lines = re.split("\n+", data)

        for index, line in enumerate(lines):
            if line == "":
                lines.pop(index)

        return lines

# FindCombinations takes an array of lines and finds every 5 word substring within each one of them.
# It returns a dict with the lines as keys pointing to the corresponding occurence number
def FindCombinations(lines):

    # This regular expression will match every word in a sentence, including those with
    # an apostrophe (e.g 'It's')
    regex = r"(\b\S+\b)"

    subStrings = {}

    for line in lines:
        matches = re.findall(regex, line)

        for matchIndex in range(0, (len(matches)- 4)):
            combination = matches[matchIndex] + " " + \
                          matches[matchIndex +1] + " " + \
                          matches[matchIndex + 2] + " " + \
                          matches[matchIndex + 3] + " " + \
                          matches[matchIndex + 4]

            if combination in subStrings:
                subStrings[combination] = subStrings[combination] + 1
            else:
                subStrings[combination] = 1

    return subStrings

# SaveOutPut will take an array containing the top sentences and their
# occurences number and save this to the path specified in csv format, utf-8 encoded
def SaveOutPut(path, sentences):
    with open(path, 'w', encoding="utf-8") as f:
        f.write('sentence , occurrences \n')
        for sentence, occurrences in sentences.items():
            f.write(sentence + ' , ' + str(occurrences) + '\n')

#---------------------------------------------------------------

lines = ParseInput("/home/cachemoi/Desktop/Programs/Python/mavens/data/Mavens_0_Dev_SecondInterviewTest-TestData_v0.1_09-March-2018.txt")

subStrings = FindCombinations(lines)

SaveOutPut('/home/cachemoi/Desktop/Programs/Python/mavens/data/results.csv', subStrings)