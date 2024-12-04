## How to run:
# python3 python/challenge01.py
## Run this command from the Day01 Directory. Failing to do so will break the open command
## as you won't be able to find the file properly

## Define the Two Lists
listOne = []
listTwo = []

## Open the input file, read it line by line, split the result
## Sort into the two lists
with open('input') as f:
    for line in f:
        temp = line.split()
        listOne.append(int(temp[0]))
        listTwo.append(int(temp[1]))

## Sort the two lists and define the result as solve
sortedListOne = sorted(listOne)
sortedListTwo= sorted(listTwo)
solve = 0

## Go through all the numbers in the list and take the difference
## Absolute value will prevent negative differences
for num in range(len(sortedListOne)):
    solve = solve + abs(sortedListOne[num] - sortedListTwo[num])

## Print Result
print(solve)