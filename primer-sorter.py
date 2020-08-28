#!/usr/bin/env python3
import sys
file = sys.argv[1] #input file
target = sys.argv[2] #tagret gene coordinates. Example: 2444-6962
MPL = int(sys.argv[3]) #minimum PCR-product length
a = 5 #maximum number of primer pairs that is supposed to cover entire or a part of the sequence
begin = int(target.split('-')[0])
end = int(target.split('-')[1])
f1 = open(file, 'r')
primers = []
paths = []
output = []
second = False
first_line = ''
last_coord = 0
for line in f1:
    if len(line) < 5:
        continue
    if not second:
        first_line = line.strip() + '\t'
        second = True
        continue
    if second:
        primers.append(first_line + line.strip())
        second = False
        continue


def sort(data):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(data) - 1):
            if int(data[i].split()[2]) > int(data[i+1].split()[2]):
                data[i], data[i + 1] = data[i + 1], data[i]
                swapped = True


sort(primers)


def cover():
    global bagin
    global end
    global primers
    cover_primers = []
    for i in range(len(primers)):
        RPC = int(primers[i].split()[7])
        LPC = int(primers[i].split()[2])
        if (begin < RPC < end) or (begin < LPC < end):
            cover_primers.append(primers[i])
    return cover_primers


def pathfinder(k):
    global RP
    global LP
    global path
    global paths
    global itr
    global cover_primers
    for j in range(len(cover_primers))[k:]:
        path[k] = j
        RP[k] = int(cover_primers[j].split()[7])
        LP[k] = int(cover_primers[j].split()[2])
        if len(RP) > 1:
            cover = True
            for l in range(len(RP) - 1):
                if RP[l] - LP[l + 1] < 100:
                    cover = False
        else:
            cover = True
        if (LP[0] < begin) and (RP[len(RP)-1] > end) and cover:
            out = ''
            for m in range(len(path)):
                out = out + str(path[m]) + '\t'
            paths.append(out)
        else:
            if k < itr - 1:
                pathfinder(k+1)
    return


def out():
    global paths
    global cover_primers
    global output
    min = 1000000
    for m in range(len(paths)):
        pair = paths[m].split()
        s = 0
        for n in range(len(pair)):
            RPC = int(cover_primers[int(pair[n])].split()[7])
            LPC = int(cover_primers[int(pair[n])].split()[2])
            s = s + RPC - LPC
        if s < min:
            min = s
            min_index = m

    path = paths[min_index].split()
    for p in path:
        output.append(cover_primers[int(p)])
        last_coord = int(cover_primers[int(p)].split()[7])
    return last_coord


cover_primers = cover()
if end - begin <= (a - 1) * MPL:
    #print('<4000')
    for itr in range(a)[1:]:
        #print(itr)
        RP = []
        LP = []
        path = []
        for i in range(itr):
            path.append(0)
            RP.append(0)
            LP.append(0)
        pathfinder(0)
        if len(paths) > 0:
            last_coord = out()
            break
else:
    divider = int((end - begin) / ((a - 1) * MPL)) + 1
    new_target_length = int((end - begin) / divider)
    begin_old = begin
    end_old = end
    for u in range(divider):
        if u == 0:
            begin = begin_old
        else:
            begin = last_coord - 100
        if u > 0 and output == []:
            print('ERROR')
            begin = u * new_target_length + begin_old
        end = u * new_target_length + new_target_length + begin_old
        if abs(end_old - end) < 50:
            end = end_old
        paths = []
        cover_primers = cover()
        for itr in range(a)[1:]:
            # print(itr)
            RP = []
            LP = []
            path = []
            for i in range(itr):
                path.append(0)
                RP.append(0)
                LP.append(0)
            pathfinder(0)
            if len(paths) > 0:
                last_coord = out()
                break

output2 = []

for w in range(len(output)-1):
    if int(output[w+1].split()[2]) <= int(output[w].split()[2]):
        continue
    else:
        output2.append(output[w])
if len(output) > 0:
    output2.append(output[len(output)-1])


for q in output2:
    print(q.split()[0] + '\t' + q.split()[1] + '\t' + q.split()[2] + '\t' + q.split()[3] + '\t' + q.split()[4])
    print(q.split()[5] + '\t' + q.split()[6] + '\t' + q.split()[7] + '\t' + q.split()[8] + '\t' + q.split()[9] + '\t' + q.split()[10])

