import jsonpickle
import sys

import pandas

import BingoBoard
import ChoicePool

dataframe: pandas.DataFrame = pandas.read_excel(io=sys.argv[1])

choices = dataframe['Bingo Choices']

choice_pool = ChoicePool.ChoicePool(choices.tolist())

bingo_board = BingoBoard.BingoBoard(choice_pool)

with open('output.json', 'w') as file:
    file.write(jsonpickle.encode(bingo_board.getBoard()))
