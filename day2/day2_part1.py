file = open("input.txt", "r")
lines = file.readlines()
safe_counter = 0
for x in lines:
    list1 = x.split(" ")
    list1 = list(map(int, list1))
    print(list1);
    boolean = False
    print(len(list1))
    for count in range(len(list1) - 1):
        if (list1[count] < list1[count + 1]):
            boolean = True
        else:
            boolean = False
            break
    if boolean == False:
        for count2 in range(len(list1) - 1):
            if (list1[count2] > list1[count2 + 1]):
                boolean = True
            else:
                boolean = False
                break
    if boolean == False:
        print("end")
        continue
    else:
        for count in range(len(list1) - 1):
            difference = abs(list1[count] - list1[count + 1])
            if (difference >= 1) and (difference <= 3):
                boolean = True
            else:
                boolean = False
                break
        if boolean == True:
            safe_counter += 1
            print("yes")
print(safe_counter)
