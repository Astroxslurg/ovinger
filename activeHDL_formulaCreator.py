#!/usr/bin/python3

# Active-HDL formula creator

# Usage:
# 1: set the variables defined in the top of main() to fit your usage
# 2: write your bit sequence in a separate txt file e.g. input.txt
#   the bit sequence can be space-separated if you wish
#   e.g.: 10101010 00001111 11110000 01010101

# 3: in unix terminal write: python3 activeHDL_formulaCreator.py < input.txt >> output.txt
#   This gives you the formula on a new line in output.txt

from sys import stdin


def main():
    # --- Define these variables to fit your usage ---
    encoding = 'FM0'  # Must be either 'FM0' or 'NRZ'
    bitTime = 2
    timescale = 'us'
    # ---

    inpSeq = []

    for line in stdin.readline().split():
        inpSeq.extend(list(line))

    inpSeq.reverse()

    outArr = []
    curTime = 0

    if (encoding == 'NRZ'):
        for b in inpSeq:
            s = "%s %s %s" % (b, curTime, timescale)
            outArr.append(s)
            curTime = curTime + bitTime

    elif (encoding == 'FM0'):
        curVal = 0
        s = "%s %s %s" % (curVal, curTime, timescale)
        outArr.append(s)

        for b in inpSeq:
            if (int(b) == 1):
                curTime = curTime + bitTime
                curVal = 1 - curVal
                s = "%s %s %s" % (curVal, curTime, timescale)
                outArr.append(s)
            else:
                for i in range(2):
                    curTime = curTime + (bitTime // 2)
                    curVal = 1 - curVal
                    s = "%s %s %s" % (curVal, curTime, timescale)
                    outArr.append(s)

    outString = ", ".join(outArr)
    print(outString)

if __name__ == "__main__":
    main()
