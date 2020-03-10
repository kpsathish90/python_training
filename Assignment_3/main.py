# -*-coding:<UTF-8> -*-
__author__ = "sathish"

from Assignment_3.module import *

if __name__ == '__main__':
    common_word, top_50_text1, top_50_text2 = common_words('data/829-0.txt', 'data/4737-0.txt')
    print("Common words in both the text files are:", '\n', common_word, '\n','\n')
    print("Top 50 common words from the text file 829-0.txt", '\n', top_50_text1, '\n', '\n')
    print("Top 50 common words from the text file 4737-0.txt", '\n', top_50_text2, '\n', '\n')

