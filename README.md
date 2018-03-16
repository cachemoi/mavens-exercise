# Mavens exercise

The ExtractSentence script will takes as input a file containing short pieces of text, one per line, UTF-8 encoded. 
The code reads the texts from the file and computes
all the 5-word sequences which occur in any line of
text. The output is written to a UTF-8-encoded CSV file, 
giving the ten most commonly-occurring sequences and how often each occurs.

You can run the script by replacing the filepaths with the ones to your own data

### Assumptions taken for this script:
- python 3 is used
- input is utf-8 encoded
- input lines are split by newline characters ('\n')
