from get_char_index import get_char_index, remove_dup


class Trie:
    """
    Represents a trie.
    Each leaf of the trie contains the index of the sentence of that substring.
    """

    def __init__(self):
        self.__nodes = [0 for i in range(27)]
        self.self.__founded_sentences = []

    def add_sentence(self, sentence, file_index, sentence_index):
        """
        Adds sentence to the trie.
        :param sentence: a sentence to add
        :param file_index: the index of the sentence's file
        :param sentence_index: the index of the sentence in its file
        """
        sentence = sentence.lower()
        for i in range(len(sentence) - 1, -1, -1):
            char_index = get_char_index(sentence[i])
            if char_index != -1 and char_index != 26:
                index = (file_index, sentence_index, i)
                self.add_string(sentence[i:i + 10], index)

    def add_string(self, string, index):
        """
        Adds string to the trie.
        :param string: a string to add
        :param index: the index of the string in the data
        """
        node = self.__nodes
        last_index = -1
        for i in string:
            char_index = get_char_index(i)
            if char_index == -1:
                continue
            if char_index == 26 and last_index == 26:
                continue
            if node[char_index] == 0:
                node[char_index] = [0 for i in range(27)]
            node = node[char_index]
            last_index = char_index
        if len(node) > 27:
            if index not in node[27]:
                node[27].append(index)
        else:
            node.append([index])

    def search(self, substring):
        """
        Searches a substring in the trie.
        :param substring: a substring to search
        :return: a list with the five high scored sentences that contain the substring.
        """
        node = self.__nodes
        self.__founded_sentences = []
        self.req_search(node, substring, 0, 0)
        if len(self.__founded_sentences) < 5:
            self.repair_search(node, substring, 0, 0)
        if len(self.__founded_sentences) < 5:
            self.small_indexes_repair(node, substring, 0)
        return self.__founded_sentences

    def small_indexes_repair(self, node, substring, index):
        """
        Searches a substring with repairs on its small indexes.
        :param node: a node in the trie where the searches on
        :param substring: a substring to search
        :param index: the current index of the repair in the substring
        :param sentences: a list with the matches sentences
        """
        for i in range(4, -1, -1):
            for j in range(26):
                self.req_search(node, substring[:i] + chr(j + 97) + substring[i + 1:], index, 5 - i)
                if len(self.__founded_sentences) >= 5:
                    return
        for i in range(4, -1, -1):
            self.req_search(node, substring[:i] + substring[i + 1:], index, 10 - 2 * i)
            for j in range(26):
                self.req_search(node, substring[:i] + chr(j + 97) + substring[i:], index, 10 - 2 * i)
                if len(self.__founded_sentences) >= 5:
                    return

    def repair_search(self, node, substring, index, was_repair):
        """
        Searches a substring with repairs
        :param node:  a node in the trie where the searches on
        :param substring:  a substring to search
        :param index:  the current index of the repair in the substring
        :param was_repair: the last score decrease
        :param sentences: a list with the matches sentences
        """
        if node == 0:
            return
        if len(substring) == 0 and was_repair:
            if len(node) > 27:
                self.__founded_sentences += map(lambda s: (s, index * 2 - was_repair), node[27])
                self.__founded_sentences = remove_dup(self.__founded_sentences)
            if len(self.__founded_sentences) >= 5:
                return
            self.get_all_children(node, index, was_repair)
            return
        if len(substring) > 0:
            c = 0
            char_index = get_char_index(substring[c])
            while char_index == -1:
                c += 1
                if c == len(substring):
                    self.get_all_children(node, index, was_repair)
                    return
                char_index = get_char_index(substring[c])
            while c < len(substring) - 1:
                next_index = get_char_index(substring[c + 1])
                if next_index == 26 and char_index == 26:
                    c += 1
                    char_index = get_char_index(substring[c])
                else:
                    break
            if was_repair or index < 4:
                self.repair_search(node[char_index], substring[c + 1:], index + 1, was_repair)
                return
            else_decrease = 10 - 2 * index if index < 5 else 2
            self.repair_search(node, substring[c + 1:], index + 1, else_decrease)
            if len(self.__founded_sentences) >= 5:
                return
            for i in range(26):
                self.repair_search(node[char_index], chr(i + 97) + substring[c + 1:], index + 1, else_decrease)
                if len(self.__founded_sentences) >= 5:
                    return
                self.repair_search(node[char_index], ' ' + substring[c + 1:], index + 1, else_decrease)
                if len(self.__founded_sentences) >= 5:
                    return
            self.repair_search(node[char_index], substring[c + 1:], index + 1, 0)
        return

    def req_search(self, node, substring, index, was_repair):
        """
        Searches for a substring in a node recursively
        :param node: the current node
        :param substring: the substring to search
        :param index: the index of the current node in the whole string
        :param was_repair: score to decrease till now
        :param sentences: the sentences which contains the substring
        :return: score to decrease from now and then
        """
        if node == 0:
            return was_repair
        if len(substring) == 0:
            if len(node) > 27:
                self.__founded_sentences += map(lambda s: (s, index * 2 - was_repair), node[27])
                self.__founded_sentences = remove_dup(self.__founded_sentences)
            if len(self.__founded_sentences) >= 5:
                return was_repair
            self.get_all_children(node, index, was_repair)
            return was_repair
        c = 0
        char_index = get_char_index(substring[c])
        while char_index == -1:
            c += 1
            if c == len(substring):
                self.get_all_children(node, index, was_repair)
                return was_repair
            char_index = get_char_index(substring[c])
        while c < len(substring) - 1:
            next_index = get_char_index(substring[c + 1])
            if next_index == 26 and char_index == 26:
                c += 1
                char_index = get_char_index(substring[c])
            else:
                break
        self.req_search(node[char_index], substring[c + 1:], index + 1, was_repair)
        if len(self.__founded_sentences) >= 5:
            return was_repair
        if not was_repair and index > 3:
            replace_decrease = 5 - index if index < 5 else 1
            for i in range(27):
                self.req_search(node[i], substring[c + 1:], index + 1, replace_decrease)
                if len(self.__founded_sentences) >= 5:
                    return replace_decrease
        return was_repair

    def get_all_children(self, node, index, repair):
        """
        Adds to sentences up to five sentences from the leaves of a specific node
        :param node: a node to add its leaves to sentences
        :param index: the len of the substring that was searched
        :param repair: the cost of the repair in the substring that was searched
        :param sentences: a list with the matches sentences
        """
        if (len(self.__founded_sentences) >= 5 and repair == 0) or node == 0:
            return
        if len(node) > 27:
            self.__founded_sentences += map(lambda s: (s, index * 2 - repair), node[27])
            self.__founded_sentences = remove_dup(self.__founded_sentences)
            if len(self.__founded_sentences) >= 5:
                return
        for i in range(27):
            self.get_all_children(node[i], index, repair)
            if len(self.__founded_sentences) >= 5:
                return
