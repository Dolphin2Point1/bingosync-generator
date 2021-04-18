import random

import BingoEntry
import ChoicePool


class BingoBoard:
    def __init__(self, choice_pool: ChoicePool, size: tuple = (5, 5)):
        choices: list = choice_pool.getChoices()
        self.board = []
        for i in range(size[0]):
            temp = []
            for j in range(size[1]):
                array_length = len(choices)
                choice_number = random.randrange(0, array_length)

                choice = choices.pop(choice_number)
                entry = BingoEntry.BingoEntry(choice)
                temp.append(entry)
                del array_length, choice_number, choice, entry
            self.board.append(temp)

    def getBoard(self):
        return_value = []
        for row in self.board:
            for item in row:
                return_value.append(item)
        return return_value
