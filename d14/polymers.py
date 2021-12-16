file1 = open("polyData.txt", "r")
lines = file1.readlines()
insertions = []
for line in lines:
    sline = line.strip()
    pair = sline.split(' -> ')
    insertions.append(pair)

# for x in insertions:
#     print(x)

def addPairs(newPairs, templatePairs):
    
    newTemplatePairs = [*templatePairs]
    for pair in newPairs:
        found = False
        for j in range(len(templatePairs)):
            if templatePairs[j][0] == pair:
                newTemplatePairs[j][1] += 1
                found = True
        if not found:
            newTemplatePairs.append([pair, 1])
    return newTemplatePairs

template = 'OOVSKSPKPPPNNFFBCNOV'

template = 'NNCB'

templatePairs = []
for i in range(len(template)-1):
    pair = template[i:i+2]
    templatePairs = addPairs([pair], templatePairs)



def polymerize(pair):
    for insert in insertions:
        if insert[0] == pair:
            return [pair[0] + insert[1], insert[1] + pair[1]]
    return None

def remove(pairs, templatePairs):
    newTemplatePairs = []
    for j in range(len(templatePairs)):
        for pair in pairs:
            if templatePairs[j][0] == pair:
                    newCount = templatePairs[j][1] - 1
                    if newCount > 0:
                        newTemplatePairs.append([templatePairs[j][0], newCount])

    return newTemplatePairs

def getPolymerString(templatePairs):
    polymerStr = ''
    for pair in templatePairs:
        polymerStr += pair[0][0]
    polymerStr += templatePairs[len(templatePairs)-1][0][1]
    return polymerStr

def countPolymerString(polStr):
    high, low = 0, 0
    


for i in range(1):
    allNews = []
    allDels = []
    for pair in templatePairs:
        newPairs = polymerize(pair[0])
        print(pair[0], newPairs)
        if newPairs is not None:
            allNews.extend(newPairs)
            allDels.append(pair[0])
        else:
            print('pair ' + str(pair) + ' not found in insertion table')
    print("allDels")
    for x in allDels:
        print(x)

    templatePairs = remove(allDels, templatePairs)
    templatePairs = addPairs(allNews, templatePairs)

polStr = getPolymerString(templatePairs)
print(polStr)









