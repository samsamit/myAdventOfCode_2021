import time
import os

x1, y1, x2, y2 = 0, 1, 2, 3

# Get card
file1 = open("hydroData.txt", "r")
Lines = file1.readlines()

coords = []
for d in Lines:
    d.strip()
    start, end = d.split("->")
    valuex1, valuey1 = start.split(",")
    valuex2, valuey2 = end.split(",")
    coords.append((int(valuex1), int(valuey1), int(valuex2), int(valuey2)))

seaFloor = [[0 for i in range(1000)] for i in range(1000)]


def getCalcData(start, end):
    return (1 if start < end else -1), abs(end - start) + 1


def printFloor(floor):
    print("Floor")
    for row in floor:
        print(row)


# seaFloor = [[0 for i in range(10)] for i in range(10)]
# coords = [
#     (9, 0, 0, 9),
# ]


for i in range(len(coords)):
    x = coords[i][x1]
    y = coords[i][y1]
    # when moving y
    if coords[i][x1] == coords[i][x2]:
        mul, length = getCalcData(coords[i][y1], coords[i][y2])

        for j in range(length):
            seaFloor[y + (j * mul)][x] += 1
        pass
    # when moving x
    elif coords[i][y1] == coords[i][y2]:
        mul, length = getCalcData(coords[i][x1], coords[i][x2])
        for j in range(length):
            seaFloor[y][x + (j * mul)] += 1
        pass
    else:
        if coords[i][x1] < coords[i][x2] and coords[i][y1] < coords[i][y2]:
            mul, length = getCalcData(coords[i][x1], coords[i][x2])
            for j in range(length):
                seaFloor[y + (j * mul)][x + (j * mul)] += 1
        if coords[i][x1] > coords[i][x2] and coords[i][y1] > coords[i][y2]:
            mul, length = getCalcData(coords[i][x1], coords[i][x2])
            for j in range(length):
                seaFloor[y + (j * mul)][x + (j * mul)] += 1
        if coords[i][x1] < coords[i][x2] and coords[i][y1] > coords[i][y2]:
            mul, length = getCalcData(coords[i][x1], coords[i][x2])
            for j in range(length):
                seaFloor[y - (j * mul)][x + (j * mul)] += 1
        if coords[i][x1] > coords[i][x2] and coords[i][y1] < coords[i][y2]:
            mul, length = getCalcData(coords[i][x1], coords[i][x2])
            for j in range(length):
                seaFloor[y - (j * mul)][x + (j * mul)] += 1

# printFloor(seaFloor)
counter = 0

for row in seaFloor:
    for point in row:
        if point >= 2:
            counter += 1

print(f"points 2 or larger: {counter}")
