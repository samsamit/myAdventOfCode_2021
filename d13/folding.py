file1 = open("foldingData.txt", "r")
lines = file1.readlines()

coordinates = []
for line in lines:
    sline = line.strip()
    x, y = sline.split(',')
    coordinates.append([int(x), int(y)])
w, h = 0, 0
for i in range(len(coordinates)):
    if coordinates[i][0] > w or w == 0:
        w = coordinates[i][0]
    if coordinates[i][1] > h or h == 0:
        h = coordinates[i][1]

paper = [[0 for _ in range(w+1)] for _ in range(h+1)]
print(f'w: {w}, h: {h}')
for coord in coordinates:
    x, y = coord
    paper[y][x] = 1

folds = [
    ['x', 655],
    ['y', 447],
    ['x', 327],
    ['y', 223],
    ['x', 163],
    ['y', 111],
    ['x', 81],
    ['y', 55],
    ['x', 40],
    ['y', 27],
    ['y', 13],
    ['y', 6],
]


def mergeXRow(row1, row2):
    newRow = []
    for i in range(len(row1)):
        if row1[i] > 0:
            newRow.append(row1[i])
        elif row2[i] > 0:
            newRow.append(row2[i])
        else:
            newRow.append(0)
    return newRow


def makeNewPaper(breakPoint, firstArr, secondArr):
    newPaper = []
    for i in range(len(firstArr)):
        if i < breakPoint:
            newPaper.append(firstArr[i])
        else:
            newRow = mergeXRow(firstArr[i], secondArr[i-breakPoint])
            newPaper.append(newRow)
    return newPaper


def makeXFold(paper, row):
    newPaper = []
    upper = [*paper][:row]
    lower = [*paper][row+1:]
    lower.reverse()
    if len(upper) >= len(lower):
        lowerStart = len(upper) - len(lower)
        newPaper = makeNewPaper(lowerStart, upper, lower)

    if len(upper) < len(lower):
        upperStart = len(lower) - len(upper)
        newPaper = makeNewPaper(upperStart, lower, upper)
    return newPaper


def mergeYRow(breakPoint, row1, row2):
    newRow = []
    for i in range(len(row1)):
        if i < breakPoint:
            newRow.append(row1[i])
        else:
            if row1[i] > 0:
                newRow.append(row1[i])
            elif row2[i-breakPoint] > 0:
                newRow.append(row2[i-breakPoint])
            else:
                newRow.append(0)
    return newRow


def makeYFold(paper, col):
    newPaper = []
    for i in range(len(paper)):
        newRow = []
        first = [*paper[i]][:col]
        second = [*paper[i]][col+1:]
        second.reverse()
        if len(first) >= len(second):
            breakPoint = len(first) - len(second)
            newRow = mergeYRow(breakPoint, first, second)

        if len(second) > len(first):
            breakPoint = len(second) - len(first)
            newRow = mergeYRow(breakPoint, second, first)
        newPaper.append(newRow)
    return newPaper


def getHoles(paper):
    count = 0
    for row in paper:
        for point in row:
            count += point
    return count

# paper = [
#     [0, 0, 0, 0, 1],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [1, 0, 0, 0, 0],
# ]


# folds = [
#     ['y', 7],
#     ['x', 5]
# ]
newPaper = [*paper]

for i in range(len(folds)):
    align, section = folds[i]
    if align == 'y':
        newPaper = makeXFold(newPaper, section)
    if align == 'x':
        newPaper = makeYFold(newPaper, section)


print('Paper:')
for x in newPaper:
    row = ''
    for char in x:
        if char == 1:
            row += '#'
        else:
            row += ' '
    print(row)
print(getHoles(newPaper))
