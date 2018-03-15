import re
import itertools

#----------------------------------------------------------
# Assumptions taken for this script:
#  - you are using python 3
#  -
#----------------------------------------------------------

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


def findCombinations(lines):
    #could hash to find same

    # This regular expression will match every word in a sentence, including those with
    # an apostrophe (e.g 'It's')
    regex = r"(\b\S+\b)"

    # The class Sentence is used to keep track of a sentence's occurences. We use a class because
    # it's more robust than a dict
    class Sentence:
        def __init__(self, string, occurences):
            self.string = string
            self.occurences = occurences

    sentences = []

    for line in lines:
        matches = re.findall(regex, line)

        for matchIndex in range(0, (len(matches)- 4)):
            combination = matches[matchIndex] + " " + \
                          matches[matchIndex +1] + " " + \
                          matches[matchIndex + 2] + " " + \
                          matches[matchIndex + 3] + " " + \
                          matches[matchIndex + 4]

            # TODO there's a way to optimise that, we only need the top 10 sentences
            incremented = False
            for sentence in sentences:
                if sentence.string == combination:
                    sentence.occurences = sentence.occurences + 1
                    incremented = True

            if not incremented:
                sentences.append(Sentence(combination, 1))

    topTen = []

    lowestOccurence = 2
    for i, sentence in enumerate(sentences):
        if sentence.occurences > lowestOccurence:
            topTen.append(sentence)

    return topTen

# SaveOutPut will take an array containing the top sentences and their
# occurences number and save this to the path specified in csv format, utf-8 encoded
def SaveOutPut(path, sentences):
    with open(path, 'w', encoding="utf-8") as f:
        f.write('sentence , occurrences \n')

        for sentence in sentences:
            f.write(sentence.string + ' , ' + str(sentence.occurences) + '\n')

#---------------------------------------------------------------

lines = ParseInput("/home/cachemoi/Desktop/Programs/Python/mavens/data/Mavens_0_Dev_SecondInterviewTest-TestData_v0.1_09-March-2018.txt")

topTen = findCombinations(lines)

SaveOutPut('/home/cachemoi/Desktop/Programs/Python/mavens/data/results.csv', topTen)