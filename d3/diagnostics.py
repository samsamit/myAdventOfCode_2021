file1 = open('diagData.txt', 'r')
Lines = file1.readlines()

data = []
for d in Lines:
    binArr = []
    for char in d:
        try:
            binArr.append(int(char))
        except:
            pass
    data.append(binArr)

# make arrays for each bit index
indexArr = [[] for i in range(len(data[0]))]
for bitArr in data:
    for i in range(len(bitArr)):
        indexArr[i].append(bitArr[i])
        pass


def isCommonBit1(bitArr):
    return bitArr.count(1) > (len(bitArr) / 2)


def binListToInt(binList):
    return int("".join(str(x) for x in binList), 2)


# Part1
# # get the most significant and not
# gamma = []
# epsilon = []
# for i in range(len(indexArr)):
#     # print(f'{indexArr[i].count(0)} of {len(indexArr[i])}')
#     if indexArr[i].count(0) > (len(indexArr[i]) / 2):
#         gamma.append(1)
#         epsilon.append(0)
#     else:
#         gamma.append(0)
#         epsilon.append(1)

# print(f'gam: {gamma}, eps: {epsilon}')
# gammaInt = binListToInt(gamma)
# epsilonInt = binListToInt(epsilon)
# print(f'gam: {gammaInt}, eps: {epsilonInt}')
# print(f'powerConsumption: {gammaInt * epsilonInt}')

# Part 2
find = True
i = 0
inspectArr = indexArr


def removeWithBit(bit, bitIndex, arr):
    newArr = arr
    for i in range(len(arr)):
        print(f'{arr[bitIndex]} == {bit}')
        if arr[i][bitIndex] == bit:
            del newArr[bitIndex]

    return newArr


for i in range(len(indexArr)):
    if isCommonBit1(indexArr[i]):
        inspectArr = removeWithBit(0, i, inspectArr)
    else:
        inspectArr = removeWithBit(1, i, inspectArr)

    print(len(inspectArr))
    if len(inspectArr) == 1:
        print(inspectArr)
    i += 1
