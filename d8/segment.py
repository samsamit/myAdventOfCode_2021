from os import remove


file1 = open("segmentData.txt", "r")
lines = file1.readlines()

ins, outs = [], []
for line in lines:
    sLine = line.strip()
    S_inputs, S_outputs = sLine.split('|')
    ins.append(S_inputs.split(' '))
    outs.append(S_outputs.split(' '))

# # part 1 
# count = 0
# for out in outs:
#     for str in out:
#         if len(str) == 2 or len(str) == 4 or len(str) == 3 or len(str) == 7:
#             count += 1

# print(count)

# part 2

display = {
    "top": None,
    "tLeft": None,
    "tRight": None,
    "middle": None,
    "bLeft": None,
    "bRight": None,
    "bot": None
}

def extract(extFrom, extThease):
    ext = extFrom
    for char in extThease:
        ext = ext.replace(char, "")
    return ext

def strSort(str):
    sort_s = sorted(str)
    a_str = "".join(sort_s)
    return a_str

def findNum(key, list):
    sKey = strSort(key)
    for i in range(len(list)):
        segment = strSort(list[i])
        if sKey == segment:
            return i

def findPromising(segments, target):
    promising = ("", 99)
    for segment in segments:
        ext = extract(segment, target)
        print(len(ext))
        if len(ext) < promising[1]:
            promising = (ext, len(ext))
    return promising



ins = [ins[0]]

for In in ins:
    numbers = [None for i in range(10)]
    segments = []
    for i in In:
        if len(i) == 2:
            numbers[1] = i
        elif len(i) == 3:
            numbers[7] = i
        elif len(i) == 4:
            numbers[4] = i
        elif len(i) == 7:
            numbers[8] = i
        else:
            if len(i) > 0:
                segments.append(i)
        
    thisDisplay = display

    print(numbers)
    # get top
    ext = extract(numbers[7], numbers[1])
    thisDisplay["top"] = ext

    # nro 3
    for segment in segments:
        if len(segment) == 5:
            ext = extract(segment, numbers[1])
            if len(ext) == 3:
                numbers[3] = ext

    # # nro. 9
    # fNine = extract(numbers[8], thisDisplay["bLeft"])
    # nineIndex = findNum(fNine, segment)
    # print(nineIndex)
                




    print(numbers)
    print(thisDisplay)


