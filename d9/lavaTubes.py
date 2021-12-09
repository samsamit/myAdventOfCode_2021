file1 = open("lavaTubeData.txt", "r")
lines = file1.readlines()

heightMap = []
for line in lines:
    sLine = line.strip()
    row = []
    for char in sLine:
        row.append([int(char), 0])
    heightMap.append(row)

# part 1
# result = 0
# for y in range(len(heightMap)):
#     for x in range(len(heightMap[y])):
#         # up
#         if y - 1 >= 0:
#             if heightMap[y][x] >= heightMap[y-1][x]:
#                 continue
#         # down
#         if y + 1 < height:
#             if heightMap[y][x] >= heightMap[y+1][x]:
#                 continue
#         # left
#         if x - 1 >= 0:
#             if heightMap[y][x] >= heightMap[y][x-1]:
#                 continue
#         # right
#         if x + 1 < width:            
#             if heightMap[y][x] >= heightMap[y][x+1]:
#                 continue
#         result += (heightMap[y][x] + 1)
# print(result)

# part 2
def isBasin(point):
    return point[0] < 9 and point[1] == 0

stateEnum = {
    0: 'r',
    1: 'u',
    2: 'l',
    3: 'd'
}

def turn(state, right = False):
    nState = state
    if right:
        nState -= 1
    else:
        nState += 1
    
    if nState > 3:
        nState = 0
    if nState < 0:
        nState = 3
    return nState

def getTunnel(y, x, map: list[list], prevY, prevX):
    if y-1 >= 0 and y-1 != prevY and map[y-1][x][1] == 1:
        return y-1, x
    if y+1 < len(map) and y+1 != prevY and map[y+1][x][1] == 1:
        return y+1, x
    if x-1 >= 0 and x-1 != prevX and map[y][x-1][1] == 1:
        return y, x-1
    if x+1 < len(map[0]) and x+1 != prevX and map[y][x+1][1] == 1:
        return y, x+1

    return x, y


# heightMap = [
#     [[9, 0],[9, 0],[1, 0],[9, 0],[9, 0]],
#     [[9, 0],[9, 0],[1, 0],[9, 0],[9, 0]],
#     [[1, 0],[1, 0],[1, 0],[1, 0],[1, 0]],
#     [[9, 0],[9, 0],[1, 0],[9, 0],[9, 0]],
#     [[9, 0],[9, 0],[1, 0],[9, 0],[9, 0]],
# ]

width = len(heightMap[0])
height = len(heightMap)

allBasins = []

for y in range(len(heightMap)):
    for x in range(len(heightMap)):
        point = heightMap[y][x]
        if isBasin(point):
            snake = True
            nX = x
            nY = y
            state = 0
            notBasin = 0
            basins = 0
            tunnel = 0
            while snake:
                #print('point', nY, nX, stateEnum[state], notBasin)
                if isBasin(heightMap[nY][nX]):
                    heightMap[nY][nX][1] = 1
                    basins += 1
                    state = turn(state)
                    notBasin = 0
                    tunnel = 0
                else:
                    notBasin += 1
                pY, pX = nY, nX
                nextY, nextX = nY, nX
                if state == 0:
                    if nextX + 1 < width:
                        nextX += 1
                if state == 1:
                    if nextY - 1 >= 0:
                        nextY -= 1
                if state == 2:
                    if nextX - 1 >= 0 :
                        nextX -= 1
                if state == 3:
                    if nextY + 1 < height:
                        nextY += 1
                
                isNextBasin = True
                curState = state
                if not isBasin(heightMap[nextY][nextX]):
                    state = turn(state, True)
                    isNextBasin = False
                else:
                    nY, nX = nextY, nextX
                if notBasin > 4:
                    notBasin = 0
                    if tunnel > 5:
                        snake = False
                    tunnel += 1
                    nY, nX = getTunnel(nY, nX, heightMap, pY, pX)
                    state = turn(state)

            allBasins.append(basins)

allBasins.sort(reverse = True)
threeBiggest = allBasins[:3]
result = threeBiggest[0] * threeBiggest[1] * threeBiggest[2]
print(threeBiggest)
print(result)