#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#


def breakingRecords(scores):
    # Write your code here

    max_score = scores[0]
    min_score = scores[0]
    max_count = 0
    min_count = 0

    for index in range(1, len(scores)):
        if min_score > scores[index]:
            min_score = scores[index]
            min_count += 1
        if max_score < scores[index]:
            max_score = scores[index]
            max_count += 1

    return max_count, min_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
