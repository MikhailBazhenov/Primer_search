#!/usr/bin/env python3
import sys

a = sys.argv[1]
step = int(sys.argv[2])
size_range = sys.argv[3]
unwanted = sys.argv[4]
max_len = int(size_range.split('-')[1])
f1 = open(a, 'r')
i = 0
seq = ''
for line in f1:
    i += 1
    ln = line.strip()
    if i == 1:
        name = ln.split(' ')[0][1:]
    if i > 1:
        seq = seq + ln
l = len(seq)
s = int(l/step)
task = ''
for i in range(s):
    k = step * i
    if k + max_len > l:
        continue
    task = task + 'SEQUENCE_ID=' + name + '_' + str(i + 1) + '\n'
    task = task + 'SEQUENCE_TEMPLATE=' + seq + '\n'
    task = task + 'SEQUENCE_INCLUDED_REGION=' + str(k) + ',' + str(max_len) + '\n'
    task = task + 'PRIMER_PRODUCT_SIZE_RANGE=' + size_range + '\n'
    task = task + '''PRIMER_TM_FORMULA=1
PRIMER_SALT_CORRECTIONS=1
PRIMER_THERMODYNAMIC_OLIGO_ALIGNMENT=1
PRIMER_SALT_DIVALENT=1.5
PRIMER_DNTP_CONC=0.6
PRIMER_LIB_AMBIGUITY_CODES_CONSENSUS=0
PRIMER_MISPRIMING_LIBRARY='''
    task = task + unwanted + '\n'
    task = task + '''PRIMER_MAX_LIBRARY_MISPRIMING=16.00
PRIMER_MAX_TEMPLATE_MISPRIMING=16.00
PRIMER_PAIR_MAX_LIBRARY_MISPRIMING=28.00
PRIMER_OPT_SIZE=23
PRIMER_MIN_SIZE=20
PRIMER_MAX_SIZE=26
PRIMER_MAX_SELF_ANY=8
PRIMER_PAIR_MAX_COMPL_ANY=8
PRIMER_MAX_SELF_END=3
PRIMER_LOWERCASE_MASKING=1
PRIMER_TASK=generic
PRIMER_NUM_RETURN=1
=
'''
task = task[0:len(task)-1]
print(task)
