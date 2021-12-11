import math
file1 = open("syntaxData.txt", "r")
lines = file1.readlines()


def fifi(char):
    opens.append(char)


def take():
    opens.pop(len(opens)-1)


def close(char):
    opener = ""
    if char == ')':
        opener = '('
    if char == '}':
        opener = '{'
    if char == ']':
        opener = '['
    if char == '>':
        opener = '<'

    if opens[len(opens)-1] == opener:
        take()
        return True
    else:
        print('Found ' + opener + 'wanted ' + opens[len(opens)-1])
        return False


# lines = [
# '{([(<[}>{{[('
# ]
errors = []
forDel = []
openers = []
for i in range(len(lines)):
    sLine = lines[i].strip()
    opens = []
    for char in sLine:
        if char == "(":
            fifi("(")
        elif char == "[":
            fifi('[')
        elif char == "{":
            fifi('{')
        elif char == "<":
            fifi('<')
        else:
            if not close(char):
                errors.append(char)
                forDel.append(i)
                break
    openers.append(opens)

print(f'forDel: {forDel}')
newOpeners = []
for i in range(len(openers)):
    print(f'count:  {i} == {forDel.count(i)}')
    if forDel.count(i) == 0:
        newOpeners.append(openers[i])

openers = newOpeners

# part 1
# print(errors)
# score = 0
# for char in errors:
#     if char == ')':
#         score += 3
#     if char == '}':
#         score += 1197
#     if char == ']':
#         score += 57
#     if char == '>':
#         score += 25137
# print(score)

# part 2


def getCloser(char):
    if char == "(":
        return ')'
    elif char == "[":
        return ']'
    elif char == "{":
        return '}'
    elif char == "<":
        return '>'


closers = []
for opener in openers:
    opener.reverse()
    closer = []
    for char in opener:
        closer.append(getCloser(char))
    closers.append(closer)
    print(closer)

scores = []
for closer in closers:
    score2 = 0
    for char in closer:
        score2 = score2 * 5
        if char == ')':
            score2 += 1
        if char == '}':
            score2 += 3
        if char == ']':
            score2 += 2
        if char == '>':
            score2 += 4
    scores.append(score2)

scores.sort()
print(scores)
middleIdx = math.floor(len(scores) / 2)
print(f'{middleIdx} / {len(scores)}')
print(scores[middleIdx])
