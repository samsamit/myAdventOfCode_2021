import statistics

file1 = open("crabsData.txt", "r")
Lines = file1.readlines()
Lines[0].strip()
crabs = Lines[0].split(',')
for i in range(len(crabs)):
    crabs[i] = int(crabs[i])


# Part 1
# crabsMedian = statistics.median(crabs)
# fuel = 0
# for i in range(len(crabs)):
#     fuel += abs(crabsMedian - crabs[i])
# print(fuel)

# Part 2
crabsMedian = round(statistics.mean(crabs))-1

fuel = 0
for i in range(len(crabs)):
    total = 0
    for i in range(abs(crabsMedian - crabs[i])):
        total += i+1
    fuel += total

print(fuel)
