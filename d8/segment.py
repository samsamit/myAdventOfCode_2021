

file1 = open("segmentData.txt", "r")
lines = file1.readlines()

ins, outs = [], []
for line in lines:
    sLine = line.strip()
    S_inputs, S_outputs = sLine.split("|")
    ins.append(S_inputs.split(" "))
    outs.append(S_outputs.split(" "))

# # part 1
# count = 0
# for out in outs:
#     for str in out:
#         if len(str) == 2 or len(str) == 4 or len(str) == 3 or len(str) == 7:
#             count += 1

# print(count)

# part 2

display = {
    "top": "",
    "tLeft": "",
    "tRight": "",
    "middle": "",
    "bLeft": "",
    "bRight": "",
    "bot": "",
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
    res = []
    for i in range(len(list)):
        segment = strSort(list[i])
        if sKey == segment:
            res.append(i)
    if len(res) > 1:
        print("multifound")
        print(res)
    else:
        return res[0]


# ins = [ins[2]]

results = []
for i in range(len(ins)):
    numbers = [None for i in range(10)]
    print(ins[i])
    segments = []
    for j in ins[i]:
        if len(j) == 2:
            numbers[1] = j
        elif len(j) == 3:
            numbers[7] = j
        elif len(j) == 4:
            numbers[4] = j
        elif len(j) == 7:
            numbers[8] = j
        else:
            if len(j) > 0:
                segments.append(j)

    thisDisplay = display

    # get top
    ext = extract(numbers[7], numbers[1])
    thisDisplay["top"] = ext

    # nro 3
    removeIndex = None
    for segmentI in range(len(segments)):
        if len(segments[segmentI]) == 5:
            ext = extract(segments[segmentI], numbers[1])
            if len(ext) == 3:
                numbers[3] = segments[segmentI]
                removeIndex = segmentI
                continue
    del segments[removeIndex]

    # nro. 6
    removeIndex = None
    for segmentI in range(len(segments)):
        if len(segments[segmentI]) == 6:
            ext = extract(segments[segmentI], numbers[7])
            if len(ext) == 4:
                numbers[6] = segments[segmentI]
                removeIndex = segmentI
                continue
    del segments[removeIndex]

    # nro. 0
    removeIndex = None
    for segmentI in range(len(segments)):
        if len(segments[segmentI]) == 6:
            ext = extract(segments[segmentI], numbers[3])
            if len(ext) == 2:
                numbers[0] = segments[segmentI]
                removeIndex = segmentI
                continue
    del segments[removeIndex]

    # bottom
    ext = extract(numbers[3], numbers[7] + numbers[4])
    thisDisplay["bot"] = ext

    # bLeft
    ext = extract(numbers[8], numbers[3] + numbers[4])
    thisDisplay["bLeft"] = ext

    # 9
    foundIndx = findNum(extract(numbers[8], thisDisplay["bLeft"]), segments)
    numbers[9] = segments[foundIndx]
    del segments[foundIndx]

    # nro 2, 5
    for segment in segments:
        if len(segment) == 5:
            ext = extract(segment, numbers[9])
            print(segment, ext, numbers[9])
            if len(ext) == 1:
                numbers[2] = segment
            if len(ext) == 0:
                numbers[5] = segment

    # tleft
    ext = extract(numbers[8], numbers[2] + numbers[1])
    thisDisplay["tLeft"] = ext

    # nro 2, 5
    for segment in segments:
        if len(segment) == 6:
            ext = extract(segment, numbers[7])
            print(segment, ext, numbers[9])
            if len(ext) == 3:
                numbers[0] = segment

    print(numbers)
    print(display)
    output = ""
    for out in outs[i]:
        if len(out) > 0:
            print(out, numbers)
            number = findNum(out, numbers)
            output += str(number)
    results.append(int(output))
    print(f"Found: {int(output)} at index {i}")

print(f"result is: {sum(results)}")
