# -*-coding:<UTF-8> -*-
__author__ = "sathish"


def common_words(input_text_1, input_text_2):
    """
    This function will get the common words in two text files
    :param input_text_2:
    :param input_text_1:
    :return: Common words from two sets
    """
    file_1 = open(input_text_1, "r")
    input_list_1 = file_1.read().translate({ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\|~`=_+\n"})
    input_list_1 = input_list_1.split(" ")
    input_list_1 = [space for space in input_list_1 if space]
    file_1.close()

    file_2 = open(input_text_2, "r")
    input_list_2 = file_2.read().translate({ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\|~`=_+\n"})
    input_list_2 = input_list_2.split(" ")
    input_list_2 = [space for space in input_list_2 if space]
    file_2.close()

    common_word = set(input_list_1).intersection(set(input_list_2))

    count_list_1 = [input_list_1.count(i) for i in input_list_1]
    count_dict_1 = dict(list(zip(input_list_1, count_list_1)))
    count_dict_1 = {k: count_dict_1[k] for k in sorted(count_dict_1, key=count_dict_1.get, reverse=True)}

    count_list_2 = [input_list_2.count(i) for i in input_list_2]
    count_dict_2 = dict(list(zip(input_list_2, count_list_2)))
    count_dict_2 = {k: count_dict_2[k] for k in sorted(count_dict_2, key=count_dict_2.get, reverse=True)}

    top_50_text_1 = {}
    top_50_text_2 = {}

    for key in common_word:
        if key in count_dict_1:
            top_50_text_1[key] = count_dict_1[key]
    for key in common_word:
        if key in count_dict_2:
            top_50_text_2[key] = count_dict_2[key]

    top_50_text_1 = {k: top_50_text_1[k] for k in sorted(top_50_text_1, key=top_50_text_1.get, reverse=True)}
    top_50_text_2 = {k: top_50_text_2[k] for k in sorted(top_50_text_2, key=top_50_text_2.get, reverse=True)}

    count_1 = 0
    count_2 = 0

    common_fifty_words_text_1 = list()
    common_fifty_words_text_2 = list()

    for item in top_50_text_1.items():
        count_1 += 1
        common_fifty_words_text_1.append(item)
        if count_1 >= 50:
            break
    for item in top_50_text_2.items():
        count_1 += 1
        common_fifty_words_text_2.append(item)
        if count_2 >= 50:
            break
    return common_word, common_fifty_words_text_1, common_fifty_words_text_2
