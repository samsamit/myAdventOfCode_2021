file1 = open('diveData.txt', 'r')
Lines = file1.readlines()

data = []
for d in Lines:
    data.append(str(d))

directions = []
for d in data:
    direction, length = d.split(' ')
    directions.append((direction, int(length)))

# PArt 1
# horisontal = 0
# depth = 0
# for heading in directions:
#     if heading[0] == "forward":
#         depth += heading[1]
#         pass
#     if heading[0] == "up":
#         horisontal -= heading[1]
#         pass
#     if heading[0] == "down":
#         horisontal += heading[1]
#         pass

# Part 2
aim = 0
horisontal = 0
depth = 0
for heading in directions:
    if heading[0] == "forward":
        horisontal += heading[1]
        depth += (aim * heading[1])
        pass
    if heading[0] == "up":
        aim -= heading[1]
        pass
    if heading[0] == "down":
        aim += heading[1]
        pass

print(horisontal, depth, aim)
print(horisontal * depth)
