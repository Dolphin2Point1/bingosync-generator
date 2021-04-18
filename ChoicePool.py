import copy


class ChoicePool:
    def __init__(self, choices: list):
        self.choices = choices

    def getChoices(self):
        return copy.copy(self.choices)
