# Using readlines()
file1 = open('sonarData.txt', 'r')
Lines = file1.readlines()

sonarData = []
for data in Lines:
    sonarData.append(int(data))

#sonarData = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
compareArr = []
for i in range(len(sonarData)):
    if len(sonarData) > i+2:
        arr = []
        for j in range(3):
            arr.append(sonarData[i+j])
        print(f'arr: {arr} = sum ( {sum(arr)} )')
        compareArr.append(sum(arr))
    else:
        print(i)

biggerCounter = 0
for i in range(len(compareArr)):
    if i > 0:
        if compareArr[i] > compareArr[i-1]:
            biggerCounter += 1

print(f'meas bigger than prev: {biggerCounter}')
