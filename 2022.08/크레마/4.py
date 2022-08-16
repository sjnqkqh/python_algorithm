#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'longestChain' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY words as parameter.
#

# 단어목록 정리
result = 0


def longestChain(words):
    # 단어 사전에 입력된 배열 등록
    word_dict = dict()
    for item in words:
        word_dict[item] = 0

    for item in words:
        reduce_spell(word_dict, item, 1)

    return sorted(word_dict.values())[-1]


# 단어 목록을 정리하며, 체이닝 확인
def reduce_spell(word_dict: dict, word: str, length: int):
    global result
    result = max(result, length)
    if len(word) == 1:
        return

    spell_list = list(word)

    for i in range(len(spell_list)):
        temp = spell_list.copy()
        temp[i] = ''
        temp_str = list_to_str(temp)

        if word_dict.get(temp_str) is not None:
            word_dict[word] = word_dict[word] + 1 if word_dict[word] != 0 else word_dict[temp_str] + 1
            if word_dict[word] > len(word):
                word_dict[word] = len(word)


def list_to_str(arr: list):
    string = ''
    for item in arr:
        string = string + item

    return string


if __name__ == '__main__':

    words_count = int(input().strip())

    words = []

    for _ in range(words_count):
        words_item = input()
        words.append(words_item)

    print(longestChain(words))
