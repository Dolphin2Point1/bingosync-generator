import copy

import jsonpickle
import sys
import getopt


import BingoBoard
import ChoicePool

opts = getopt.getopt(sys.argv[1:], 'e:y:o:')

excel = False
file = ""

outputFile = 'output.json'

for o, a in opts[0]:
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
    import pandas
    dataframe: pandas.DataFrame = pandas.read_excel(io=file)
    choices = dataframe['Bingo Choices'].tolist()
else:
    import yaml
    from yaml import BaseLoader
    with open(file, "r") as f:
        yamlInput = f.read()
    yamlOutput = yaml.load(yamlInput, Loader=BaseLoader)
    choices = yamlOutput['choices']

choice_pool = ChoicePool.ChoicePool(choices)

bingo_board = BingoBoard.BingoBoard(choice_pool)

with open(outputFile, 'w') as file:
    file.write(jsonpickle.encode(bingo_board.getBoard()))
