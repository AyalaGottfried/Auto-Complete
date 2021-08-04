def get_char_index(char):
    """
    :param char: a printable char
    :return: the index in the trie of the char
    """
    if char == ' ':
        return 26
    elif 122 >= ord(char) >= 97:
        return ord(char) - 97
    return -1
