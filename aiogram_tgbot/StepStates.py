from aiogram.utils.helper import Helper, HelperMode, ListItem

class StepStates(Helper):
    mode = HelperMode.snake_case

    NAME_STATE = ListItem()
    AGE_STATE = ListItem()