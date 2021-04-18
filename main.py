import jsonpickle
import sys
import getopt
import yaml

import pandas

import BingoBoard
import ChoicePool

opts = getopt.getopt(sys.argv[1:], 'e:y:o:')

excel = False
file = ""

outputFile = 'output.json'

for o, a in opts:
    if o == '-e':
        excel = True
        file = a
    elif o == '-y':
        excel = False
        file = a
    elif o == '-o':
        if not outputFile.endswith(".json"):
            raise ValueError("Output file must end with .json, currently only json is supported.")
        outputFile = a

if file == "":
    raise ValueError("You must specify an input file.")

if excel:
    dataframe: pandas.DataFrame = pandas.read_excel(io=file)
    choices = dataframe['Bingo Choices']
else:
    yamlInput = yaml.load(file)
    choices = yamlInput['choices']

choice_pool = ChoicePool.ChoicePool(choices.tolist())

bingo_board = BingoBoard.BingoBoard(choice_pool)

with open('output.json', 'w') as file:
    file.write(jsonpickle.encode(bingo_board.getBoard()))
