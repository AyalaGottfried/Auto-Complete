from dataclasses import dataclass


@dataclass
class AutoCompleteData:
    def __init__(self, sentence, source_text, offset, score):
        self.__completed_sentence = sentence
        self.__source_text = source_text
        self.__offset = offset
        self.__score = score

    def get_completed_sentence(self):
        return self.__completed_sentence

    def get_source_text(self):
        return self.__source_text

    def get_offset(self):
        return self.__offset

    def get_score(self):
        return self.__score

    def __str__(self):
        return "{} ({}:{})".format(self.__completed_sentence, self.__source_text, self.__offset)
