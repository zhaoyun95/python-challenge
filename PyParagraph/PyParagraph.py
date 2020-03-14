# Pytho Challenge
# PyParagraph.py

import re
import os

# define two input files with text for analysis
p1 = os.path.join(".", "raw_data", "paragraph_1.txt")
p2 = os.path.join(".", "raw_data", "paragraph_2.txt")

# function to process one file
def pyParagraph(p):
    print(f"Processing {p}")

    f = open(p)
    paragraph = f.read()
    f.close()

    words = re.split("\W+", paragraph)
    sentences = re.split("(?<=[.!?]) +", paragraph)

    # get Average Letter Count
    totalLetterCount = 0
    for word in words:
        totalLetterCount += len(word)
    avgLetterCount = totalLetterCount / len(words)

    # get Average Sentence Length
    totalSentenceLength = 0
    for s in sentences:
        totalSentenceLength += len(s)
    avgSentenceLength = totalSentenceLength / len(sentences)


    # print out results
    print("Paragraph Analysis")
    print("-----------------")
    print(f"Approximate Word Count: {len(words)}")
    print(f"Approximate Sentence Count: {len(sentences)}")
    print(f"Average Letter Count: {avgLetterCount:.1f}")
    print(f"Average Sentence Length: {avgSentenceLength:.1f}")
    print("-----------------")
    print("")

# call the function to process 2 files
pyParagraph(p1)
pyParagraph(p2)