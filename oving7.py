#!/usr/bin/python3

from sys import stdin

class NoteValueSolver:
    def __init__(self, notes):
        self.storedValues = {}
        self.notes = notes

    def getRelativeValue(self, tup):
        return tup[1]

    def cutByHeight(self, w, h):
        if (w, h) in self.storedValues:
            return self.storedValues[(w, h)]

        relativeValues = [(0, 0)] * h

        for i in range(1, h+1):
            val = 0
            if(i in self.notes):
                val = self.cutByWidth(w, i)
                # print('h:', i,'w:', w, 'val:', val)
            relativeValues[i-1] = (i, val/(i))
        relativeValues.sort(key=self.getRelativeValue, reverse=True)

        rem = h
        i = 0
        j = 1
        val = 0
        maxVal = 0
        needToCheckMoreSolutions = False
        while (rem > 0):
            tup = relativeValues[i]
            if(tup[0] <= rem):
                howMany = rem//tup[0]
                rem = rem%tup[0]
                val += howMany*tup[0]*tup[1]
            else:
                needToCheckMoreSolutions = True

            if (rem == 0):
                if (val > maxVal):
                    maxVal = val
                if(needToCheckMoreSolutions):
                    val = 0
                    rem = h
                    i = j
                    j += 1
                    needToCheckMoreSolutions = False
                    continue
            i += 1

        self.storedValues[(w, h)] = maxVal
        return maxVal

    def cutByWidth(self, w, h):
        # print('-- cutByWidth -- w:', w, 'h:', h)
        if (w, h) in self.storedValues:
            return self.storedValues[(w, h)]

        thisNotes = self.notes[h][:]
        # thisNotes = []
        # TODO: see if this can be reversed +? optimized more
        for height in sorted(self.notes.keys()):
            if height >= h:
                break
            for note in self.notes[height]:
                thisNotes.append(((note[0]*(height/h)),note[1],note[2]))
        thisNotes.sort(key=getKey, reverse=True)

        rem = w
        i = 0
        j = 1
        val = 0
        maxVal = 0
        needToCheckMoreSolutions = False
        while (rem > 0):
            note = thisNotes[i]
            # print('rem:', rem, 'note:', note)
            if(note[1] <= rem):
                howMany = rem//note[1]
                rem = rem%note[1]
                val += howMany*note[2]
                # print('howMany:', howMany, 'rem:', rem, 'val:', val)
            else:
                needToCheckMoreSolutions = True
                # print('needToCheckMoreSolutions')

            if (rem == 0):
                # ('maxVal:', maxVal, 'val:', val, 'nTCMS:', needToCheckMoreSolutions)
                if (val > maxVal):
                    maxVal = val
                if(needToCheckMoreSolutions):
                    val = 0
                    rem = w
                    i = j
                    j += 1
                    needToCheckMoreSolutions = False
                    continue
            i += 1

        self.storedValues[(w, h)] = maxVal
        return maxVal

def getKey(item):
    return item[0]

def main():
    notes = {}
    widths = []
    heights = []
    values = []
    relativeValues = []
    for triple in stdin.readline().split():
        dim_value = triple.split(':', 1)
        dim = dim_value[0].split('x', 1)
        width = int(dim[0][1:])
        height = int(dim[1][:-1])
        value = int(dim_value[1])
        relativeValue = value/(width*height)
        if (height in notes):
            notes[height].append((relativeValue, width, value))
        else:
            notes[height] = [(relativeValue, width, value)]
        if not width == height:
            if (width in notes):
                notes[width].append((relativeValue, height, value))
            else:
                notes[width] = [(relativeValue, height, value)]

    for height in notes:
        notes[height].sort(key=getKey, reverse=True)
        notes[height].append((0,1,0))
        # print(height, ':', notes[height])
    nvs = NoteValueSolver(notes)
    for line in stdin:
        paper_width, paper_height = [int(x) for x in line.split('x', 1)]
        if paper_width < paper_height:
            # print('paper_width:', paper_height, 'paper_height:', paper_width)
            print(nvs.cutByHeight(paper_height, paper_width))
        else:
            # print('paper_width:', paper_width, 'paper_height:', paper_height)
            print(nvs.cutByHeight(paper_width, paper_height))

    # for height in sorted(notes.keys()):
        # print(height)


if __name__ == "__main__":
    main()
