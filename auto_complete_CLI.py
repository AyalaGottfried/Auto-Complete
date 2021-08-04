from data import Data


class CLI:
    def __init__(self):
        print("Loading the files and preparing the system...")
        self.__data = Data()

    def run(self):
        """
        Gets new requests and handles them
        """
        while True:
            print("The system is ready. Enter your text:")
            sentence = " "
            while sentence[-1] != "#":
                sentence += input(sentence)
                if sentence[-1] == "#": break
                completions = self.__data.get_best_completions(sentence)
                if len(completions) == 0:
                    print("There is no matches suggestions.")
                else:
                    print("Here are {} suggestions:".format(len(completions)))
                    for i in range(len(completions)):
                        print("{}. {} {}".format(i + 1, completions[i], completions[i].get_score()))
