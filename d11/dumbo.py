file1 = open("dumboData.txt", "r")
lines = file1.readlines()

octos =[]
for line in lines:
    sLine = line.strip()
    row = []
    for num in sLine:
        row.append(int(num))
    octos.append(row)

class Dumbos:
    def __init__(self, dumbos) -> None:
        self.dumbos = self.createDumbos(dumbos)
        self.yMax = len(self.dumbos)
        self.xMax = len(self.dumbos[0])
        pass

    def createDumbos(self, dumbos):
        newDumbos = []
        for row in dumbos:
            newRow = []
            for dumbo in row:
                newRow.append([dumbo, False])
            newDumbos.append(newRow)
        return newDumbos
    
    def charge(self):
        newDumbos = []
        for y in range(self.yMax):
            newRow = []
            for x in range(self.xMax):
                newRow.append([self.dumbos[y][x][0]+1, False])
            newDumbos.append(newRow)
        self.dumbos = newDumbos

    def deCharge(self):
        newDumbos = []
        for y in range(self.yMax):
            newRow = []
            for x in range(self.xMax):
                if self.dumbos[y][x][1]:
                    newRow.append([0, False])
                else:
                    newRow.append(self.dumbos[y][x])
            newDumbos.append(newRow)
        self.dumbos = newDumbos        

    def checkFlash(self):
        flashIndexes = []
        for y in range(self.yMax):
            for x in range(self.xMax):
                if self.dumbos[y][x][0] > 9 and not self.dumbos[y][x][1]:
                    flashIndexes.append([y, x])
        return flashIndexes

    def checkSimultaneousFlash(self):
        for y in range(self.yMax):
            for x in range(self.xMax):
                if not self.dumbos[y][x][1]:
                    return False
        return True

    def inflictFlash(self, flashIndexes):
        for point in flashIndexes:
            y, x = point
            self.dumbos[y][x][1] = True
            for tY in range(y-1, y+2):
                for tX in range(x-1, x+2):
                    if tY < 0 or tX < 0: continue
                    if tY >= self.yMax or tX >= self.xMax: continue
                    if tY == y and tX == x: continue
                    self.dumbos[tY][tX][0] += 1

# octos = [
#     [1, 1, 1, 1, 1],
#     [1, 9, 9, 9, 1],
#     [1, 9, 1, 9, 1],
#     [1, 9, 9, 9, 1],
#     [1, 1, 1, 1, 1],
# ]

dumbos = Dumbos(octos)
flashCount = 0
step = 0
doSteps = True
while doSteps:
    step += 1
    dumbos.charge()
    checkFlash = True
    while checkFlash:
        flashes = dumbos.checkFlash()
        flashCount += len(flashes)
        dumbos.inflictFlash(flashes)
        if len(flashes) == 0:
            checkFlash = False
    if dumbos.checkSimultaneousFlash():
        print(f'flashCount: {len(flashes)},  totalOctos: {dumbos.xMax * dumbos.yMax}')
        print(f'Simultaniout flash on sttep: {step}')
        doSteps = False
        checkFlash = False
    dumbos.deCharge()

