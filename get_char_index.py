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

def remove_dup(lst):
    new_lst = []
    for i in lst:
        added = False
        for j in range(len(new_lst)):
            if i[0] == new_lst[j][0]:
                new_lst[j] = max(i, new_lst[j], key=lambda s: s[1])
                added = True
                break
        if not added:
            new_lst.append(i)
    return new_lst
