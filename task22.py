def fill_set(someSet, n):
    for i in range(n):
        someSet.add(int(input()))


print("Type sizes of sets")
n = int(input())
m = int(input())


firstSet = set()
secondSet = set()
print("Type in elements of the first set")
fill_set(firstSet, n)
print("Type in elements of the second set")
fill_set(secondSet, m)

setConcatenation = firstSet | secondSet

listOfElements = list(setConcatenation)
listOfElements.sort()
print(f"Both sets sorted in ascending order without recurrences: {listOfElements}")