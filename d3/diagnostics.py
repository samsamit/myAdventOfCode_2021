file1 = open('diagData.txt', 'r')
Lines = file1.readlines()

data: list[list] = []
for d in Lines:
    binArr = []
    for char in d:
        try:
            binArr.append(int(char))
        except:
            pass
    data.append(binArr)


# make arrays for each bit index
def getBitIndexArray(data):
    indexArr = [[] for i in range(len(data[0]))]
    for bitArr in data:
        for i in range(len(bitArr)):
            indexArr[i].append(bitArr[i])
    return indexArr


def isCommonBit1(bitArr):
    return bitArr.count(1) > (len(bitArr) / 2)


def binListToInt(binList):
    return int("".join(str(x) for x in binList), 2)


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

def getSignificantBitIndexs(bit, bitIndex, arr):
    delCount = 0
    newArr = []
    for i in range(len(arr)):
        if arr[i][bitIndex] == bit:
            newArr.append(arr[i])
            delCount += 1
    return newArr


oxygenData = [*data]
co2Data = [*data]


for i in range(len(data[0])):
    if len(oxygenData) > 1:
        indexArray = list(map(lambda x: x[i], oxygenData))
        if float(indexArray.count(0)) > (len(indexArray) / 2):
            oxygenData = getSignificantBitIndexs(0, i, oxygenData)
        else:
            oxygenData = getSignificantBitIndexs(1, i, oxygenData)

    if len(co2Data) > 1:
        indexArray = list(map(lambda x: x[i], co2Data))
        if float(indexArray.count(0)) > (len(indexArray) / 2):
            co2Data = getSignificantBitIndexs(1, i, co2Data)
        else:
            co2Data = getSignificantBitIndexs(0, i, co2Data)

oxygenRating = binListToInt(oxygenData[0])
co2Rating = binListToInt(co2Data[0])
print(oxygenRating)
print(co2Rating)
print(oxygenRating * co2Rating)
