file1 = open("cavesData.txt", "r")
lines = file1.readlines()

caves = []

for line in lines:
    sline = line.strip()
    a, b = sline.split('-')
    found1, found2 =  False, False
    for i in range(len(caves)):
        if caves[i][0] == a:
            caves[i][1].append(b)
            found1 = True
    for i in range(len(caves)):
        if caves[i][0] == b:
            caves[i][1].append(a)
            found2 = True
            break
    if not found1:
        caves.append([a, [b]])
    if not found2:
        caves.append([b, [a]])

for x in caves:   
    print(x)

def isUpper(string):
    upperStr = string.upper()
    return string == upperStr

def getCaves(name):
    for cave in caves:
        if cave[0] == name:
            return cave[1]
    return None

def getPath(cavePath, paths):
    for i in range(len(paths)):
        if paths[i] == cavePath:
            return i
    return None

exploring = True
nextCaves = []
paths = []
endPaths = []
doubles = []
for cave in getCaves('start'):
    nextCaves.append(cave)
    paths.append('start,' + cave)
    doubles.append(False)
while exploring:
    newPaths = []
    newNexts = []
    newDoubles = []
    end = 0
    for path in paths:
        nextCave = path[-2:]
        newcaves = getCaves(nextCave)
        if newcaves is None:
            end += 1
        else:
            for newcave in newcaves:
                if isUpper(newcave) or path.count(newcave) == 0 or (path.count(newcave) == 1 and not doubles[i]):
                    if newcave == 'end':
                        endPaths.append(path + ',' + newcave)
                    newPaths.append(path + ',' + newcave)
                    if path.count(newcave) == 1:
                        newDoubles.append(True)
                    else:
                        newDoubles.append(doubles[i])
        if end == len(paths):
            exploring = False
    paths = newPaths
    doubles = newDoubles
    print(len(paths), len(doubles))
    if not exploring:
        break

print(len(endPaths))