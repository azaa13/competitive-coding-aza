#!/bin/python3

import math
import os
import random
import re
import sys
import string

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    alpha = list(string.ascii_lowercase)
    mapping_dict = dict()
    for i in range(len(alpha)):
        mapping_dict[alpha[i]] = h[i]
    #return mapping_dict

    values = []
    for i in range(len(word)):
        values.append(mapping_dict[word[i]])
    return max(values) * len(word)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()