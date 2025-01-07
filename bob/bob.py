from enum import Enum


class Answer(Enum):
    QUESTION = 'Sure.'
    YELL = 'Whoa, chill out!'
    YELL_QUESTION = "Calm down, I know what I'm doing!"
    SILENCE = "Fine. Be that way!"
    DEFAULT = "Whatever."


def response(hey_bob):
    stripped_string = hey_bob.strip()
    isSilence = stripped_string == ''

    if isSilence:
        return Answer.SILENCE.value

    isQuestion = stripped_string[-1] == '?'
    isAllCaps = stripped_string.isupper()
    
    if isAllCaps and isQuestion:
        return Answer.YELL_QUESTION.value

    if isAllCaps:
        return Answer.YELL.value

    if isQuestion:
        return Answer.QUESTION.value

    return Answer.DEFAULT.value
