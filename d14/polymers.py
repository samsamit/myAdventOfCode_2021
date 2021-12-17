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
            if templatePairs[j][0] == pair[0]:
                newTemplatePairs[j][1] += pair[1]
                found = True
        if not found:
            newTemplatePairs.append(pair)
    return newTemplatePairs

template = 'OOVSKSPKPPPNNFFBCNOV'

# template = 'NNCB'

templatePairs = []
for i in range(len(template)-1):
    pair = template[i:i+2]
    templatePairs = addPairs([[pair, 1]], templatePairs)



def polymerize(pair):
    for insert in insertions:
        if insert[0] == pair[0]:
            return [[pair[0][0] + insert[1], pair[1]], [insert[1] + pair[0][1], pair[1]]]
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
        for i in range(pair[1]):
            polymerStr += pair[0][0]
    polymerStr += templatePairs[len(templatePairs)-1][0][1]
    return polymerStr

def getChars(polArr):
    chars = []
    polArr.append([polArr[len(polArr)-1][0][1] + 'X', 1])
    for pair in polArr:
        found = False
        for i in range(len(chars)):
            if chars[i][0] == pair[0][0]:
                chars[i][1] += pair[1]
                found = True
                break
        if not found:
            chars.append([pair[0][0], pair[1]])
    return chars

def countPolymerString(polArr):
    high, low = 0, 0
    chars = getChars(polArr)
    for char in chars:
        if char[1] > high or high == 0:
            high = char[1]
            print('high == ' + char[0])
        if char[1] < low or low == 0:
            low = char[1]
            print('low == ' + char[0])
    return high, low

for i in range(40):
    print(i)
    allNews = []
    for pair in templatePairs:
        newPairs = polymerize(pair)
        if newPairs is not None:
            allNews = addPairs(newPairs, allNews)
        else:
            print('pair ' + str(pair) + ' not found in insertion table')
    templatePairs = allNews

print(templatePairs[len(templatePairs)-1])
high, low = countPolymerString(templatePairs)
print(f'High: {high} - Low: {low} - Total: {high-low +1}') # +1 probably because the last char in the polystring is not counted in my code...









