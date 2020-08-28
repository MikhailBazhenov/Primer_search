#!/usr/bin/env python3
import sys

file1 = sys.argv[1]
file2 = sys.argv[2]
file3 = 'masked_' + file1

f1 = open(file1, 'r') #file with a sequence
f2 = open(file2, 'r') #gff3 file with TE coordinates
f3 = open(file3, 'w') #masked sequence

intervals = []
for line in f2:
    if line.find('sequence-region') > 0:
        ls = line.strip()
        lss = line.split()
        begin_reg = int(lss[2])
        end_reg = int(lss[3])
    if line[0:2] != '##':
        ls = line.strip()
        lss = line.split()
        intervals.append(lss[3] + '\t' + lss[4])

intervals_new = []
for interval in intervals:
    te = interval.split()
    lte = int(te[0]) - begin_reg
    rte = int(te[1]) - begin_reg
    interval = str(lte) + '\t' + str(rte)
    intervals_new.append(interval)

stroka = 0
n = 0
for line in f1:
    stroka += 1
    if stroka == 1:
        f3.write(line)
        continue
    out = ''
    for i in line:
        if i == 'A' or i == 'T' or i == 'G' or i == 'C' or i == 'N':
            n += 1
            inside = False
            for interval in intervals_new:
                te = interval.split()
                lte = int(te[0])
                rte = int(te[1])
                if lte < n < rte:
                    inside = True
            #print(n, lte, rte, inside)
            if inside:
                L = i.lower()
            else:
                L = i
            out = out + L
        else:
            out = out + i

    f3.write(out)

f1.close()
f2.close()
f3.close()
