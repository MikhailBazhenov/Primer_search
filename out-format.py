#!/usr/bin/env python3
import sys
prev_out = ''
total_out = ''
a = sys.argv[1]
f1 = open(a, 'r')
primers = []
for line in f1:
    ln = line.strip()
    if ln == '=':
        if PNR == 0:
            continue
        out = id + 'L' + '\t' + PLS + '\t' + PLP + '\t' + PLL + '\t' + PLT + '\t' + '\n'
        out = out + id + 'R' + '\t' + PRS + '\t' + PRP + '\t' + PRL + '\t' + PRT + '\t' + PPS + '\n'
        out_nn = PLS + '\t' + PLP + '\t' + PLL + '\t' + PLT + '\t' + '\n'
        out_nn = out_nn + PRS + '\t' + PRP + '\t' + PRL + '\t' + PRT + '\t' + PPS + '\n'
        if out_nn != prev_out:
            total_out = total_out + out
            prev_out = out_nn
        continue
    ls = ln.split('=')
    if ls[0] == 'SEQUENCE_ID':
        id = ls[1]
    if ls[0] == 'PRIMER_LEFT_0_SEQUENCE':
        PLS = ls[1]
    if ls[0] == 'PRIMER_RIGHT_0_SEQUENCE':
        PRS = ls[1]
    if ls[0] == 'PRIMER_LEFT_0':
        PLP = ls[1].split(',')[0]
        PLL = ls[1].split(',')[1]
    if ls[0] == 'PRIMER_RIGHT_0':
        PRP = ls[1].split(',')[0]
        PRL = ls[1].split(',')[1]
    if ls[0] == 'PRIMER_LEFT_0_TM':
        PLT = ls[1]
    if ls[0] == 'PRIMER_RIGHT_0_TM':
        PRT = ls[1]
    if ls[0] == 'PRIMER_PAIR_0_PRODUCT_SIZE':
        PPS = ls[1]
    if ls[0] == 'PRIMER_PAIR_NUM_RETURNED':
        PNR = int(ls[1])
print(total_out)

