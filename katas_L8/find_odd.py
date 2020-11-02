import numpy as np


def find_it_v1(seq):
    freq = np.unique(seq, return_counts=True)
    freq1 = np.array(freq[:1]).tolist()[0]
    freq2 = np.array(freq[1:]).tolist()[0]
    for digit in freq2[:]:
        if digit % 2 != 0:
            odd_num = freq2.index(digit)
            return freq1[odd_num]


def find_it_v2(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i


print(find_it_v1([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]))
print(find_it_v2([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]))
