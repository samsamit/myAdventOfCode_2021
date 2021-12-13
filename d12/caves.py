file1 = open("cavesData.txt", "r")
lines = file1.readlines()

caves = []

for line in lines:
    sline = line.strip()
    a, b = sline.split('-')
    found1, found2 = False, False
    for i in range(len(caves)):
        if caves[i][0] == a:
            if b != 'start':
                caves[i][1].append(b)
            found1 = True
    for i in range(len(caves)):
        if caves[i][0] == b:
            if a != 'start':
                caves[i][1].append(a)
            found2 = True
            break
    if not found1:
        if b != 'start':
            caves.append([a, [b]])
        else:
            caves.append([a, []])
    if not found2:
        if a != 'start':
            caves.append([b, [a]])
        else:
            caves.append([b, []])

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


def explorePath(path, connections):
    if path[-1] == 'end':
        yield path
    else:
        for nextCave in connections:
            if isUpper(nextCave) or nextCave not in path:
                newPath = [*path, nextCave]
                newNeighbours = getCaves(nextCave)
                yield from explorePath(newPath, newNeighbours)


def explorePatfDoubleSingle(path, connections):
    if path[-1] == 'end':
        yield path
    else:
        for nextCave in connections:
            if isUpper(nextCave) or nextCave not in path:
                newPath = [*path, nextCave]
                newNeighbours = getCaves(nextCave)
                yield from explorePatfDoubleSingle(newPath, newNeighbours)
            elif not isUpper(nextCave) and nextCave != 'start':
                newPath = [*path, nextCave]
                newNeighbours = getCaves(nextCave)
                yield from explorePath(newPath, newNeighbours)


paths = list(explorePatfDoubleSingle(['start'], getCaves('start')))
print(type(paths))

print(len(paths))
