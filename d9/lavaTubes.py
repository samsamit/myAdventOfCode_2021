file1 = open("lavaTubeData.txt", "r")
lines = file1.readlines()

heightMap = []
for line in lines:
    sLine = line.strip()
    row = []
    rawRow = []
    for char in sLine:
        row.append([int(char), 0])
    heightMap.append(row)

width = len(heightMap[0])
height = len(heightMap)

lowPoints = []

# part 1
result = 0
for y in range(len(heightMap)):
    for x in range(len(heightMap[y])):
        # up
        if y - 1 >= 0:
            if heightMap[y][x][0] >= heightMap[y - 1][x][0]:
                continue
        # down
        if y + 1 < height:
            if heightMap[y][x][0] >= heightMap[y + 1][x][0]:
                continue
        # left
        if x - 1 >= 0:
            if heightMap[y][x][0] >= heightMap[y][x - 1][0]:
                continue
        # right
        if x + 1 < width:
            if heightMap[y][x][0] >= heightMap[y][x + 1][0]:
                continue
        heightMap[y][x][1] = 1
        lowPoints.append([y, x])


# heightMap = [
#     [[9, 0], [9, 0], [1, 0], [9, 0], [9, 0]],
#     [[9, 0], [1, 0], [1, 0], [1, 0], [9, 0]],
#     [[9, 0], [1, 0], [1, 1], [1, 0], [9, 0]],
#     [[9, 0], [1, 0], [9, 0], [1, 0], [9, 0]],
#     [[9, 0], [1, 0], [9, 0], [1, 0], [9, 0]],
#     [[9, 0], [9, 0], [9, 0], [9, 0], [9, 0]],
# ]
# lowPoints = [[2, 2]]

width = len(heightMap[0])
height = len(heightMap)


def isBasin(point):
    return point[0] < 9 and point[1] == 0


allBasins = []

# lowPoints = [lowPoints[0]]

for point in lowPoints:
    y, x = point

    explore = True
    pointsToCheck = [[y, x]]
    basinCount = 1
    while explore:
        newPoints = []
        for points in pointsToCheck:
            eY, eX = points

            i = eY - 1
            j = eX
            if i >= 0:
                if isBasin(heightMap[i][j]):
                    heightMap[i][j][1] = 1
                    newPoints.append([i, j])
                    basinCount += 1

            i = eY + 1
            j = eX
            if i < height:
                if isBasin(heightMap[i][j]):
                    heightMap[i][j][1] = 1
                    newPoints.append([i, j])
                    basinCount += 1

            i = eY
            j = eX - 1
            if j > 0:
                if isBasin(heightMap[i][j]):
                    heightMap[i][j][1] = 1
                    newPoints.append([i, j])
                    basinCount += 1

            i = eY
            j = eX + 1
            if j < width:
                if isBasin(heightMap[i][j]):
                    heightMap[i][j][1] = 1
                    newPoints.append([i, j])
                    basinCount += 1

        if len(newPoints) == 0:
            explore = False
        pointsToCheck = newPoints
        newPoints = []
    allBasins.append(basinCount)

allBasins.sort(reverse = True)
result = allBasins[0] * allBasins[1] * allBasins[2]
print(allBasins)
print(result)