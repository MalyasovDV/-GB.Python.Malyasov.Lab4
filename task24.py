def fillList(n, some_list):
    for i in range(n):
        some_list.append(int(input()))

def findMaximumBerries(bush_list):
    max_berries = 0
    for i in range(len(bush_list) - 1):
        if (max_berries < bush_list[i - 1] + bush_list[i] + bush_list[i + 1]):
            max_berries = bush_list[i - 1] + bush_list[i] + bush_list[i + 1]
    if (max_berries < bush_list[-2] + bush_list[-1] + bush_list[0]):
        max_berries = bush_list[-1] + bush_list[-2] + bush_list[0]
    return max_berries
        
print("Type in the amount of bushes")
n = int(input())

bush_list = list()
print("Type in the amount of berries on bushes")
fillList(n, bush_list)

print(f"Maximum berries: {findMaximumBerries(bush_list)}")