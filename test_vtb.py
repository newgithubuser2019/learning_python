import sys
from itertools import groupby

strings = ["aaaabbcaa", "abc"]
for i in strings:
    output = "".join([k + str(len(list(v))) for k, v in groupby(i)])
    print("Input: " + i)
    print("Output: " +  output)
    print("---")
sys.exit()
