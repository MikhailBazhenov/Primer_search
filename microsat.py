#!/usr/bin/env python3
import sys
fn = sys.argv[1] #input file
ms_len = int(sys.argv[2]) #length of simple tandem repeat to search
f1 = open(fn, 'r')
seq = ''
for line in f1:
    if line[0] != '>':
        seq = seq + line.strip()
seq = seq.upper()

repeats = []
for i in range(len(seq) - ms_len):
    pat = seq[i: i + ms_len]
    for j in range(ms_len):
        if seq[i + j + 1: i + j + ms_len + 1] == pat:
            repeats.append([seq[i: i + j + ms_len + 1], i])

repeats_2 = []
for i in range(len(repeats) - 1):
    if repeats[i][1] == repeats[i+1][1]:
            continue
    else:
        repeats_2.append(repeats[i])

p = 1
for i in range(len(repeats_2) - 1):
    if repeats_2[i][1] == repeats_2[i + 1][1] - p:
        repeats_2[i + 1][0] = repeats_2[i][0][0:p] + repeats_2[i + 1][0]
        repeats_2[i + 1][1] = repeats_2[i][1]
        p += 1
    else:
        p = 1


repeats = []
for i in range(len(repeats_2) - 1):
    if repeats_2[i][1] == repeats_2[i + 1][1]:
        continue
    else:
        repeats.append(repeats_2[i])


for i in range(len(repeats)):
    print('>' + 'STR' + str(i + 1) + '_position=' + str(repeats[i][1]))
    print(repeats[i][0])
