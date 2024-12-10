arr1 = []
arr2 = []
total = []


locationIDs = open("input.txt", "r")
line = locationIDs.readlines()

for x in line:
    split_location = x.split("   ")
    arr1.append(split_location[0])
    arr2.append(split_location[1].replace("\n", ""))


arr1.sort()
arr2.sort()
arr1 = list(map(int, arr1))
arr2 = list(map(int, arr2))
for x in arr1:
    num = arr1.index(x)
    total.append(abs(arr1[num] - arr2[num]))

print(arr1[0])
print(arr2[0])
print(total[0])
totalnum = sum(total)
print(totalnum)


# part 2 

similarity = 0
for x in arr1:
    
    count = 0
    for y in arr2:
        if x == y:
            count += 1
    similarity = similarity + (count * x)

print(similarity)
            
