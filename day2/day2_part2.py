file = open("input.txt", "r")
lines = file.readlines()

safe_counter = 0

def ft_safe_checker(list1):

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
        return False;
    else:
        for count in range(len(list1) - 1):
            difference = abs(list1[count] - list1[count + 1])
            if (difference >= 1) and (difference <= 3):
                boolean = True
            else:
                boolean = False
                break

        if boolean == True:
            print("yes")
            return True
        else:
            return False

for x in lines:
    list1 = x.split(" ")
    list1 = list(map(int, list1))
    checker = ft_safe_checker(list1)
    if not checker:
        for index in range(len(list1)): 
            temp = list()
            for i in range(len(list1)):
                if (i == index):
                    continue
                else:
                    temp.append(list1[i])
            checker = ft_safe_checker(temp)
            if not checker:
                continue
            else:
                safe_counter += 1
                break
    else:
        safe_counter += 1
print(safe_counter)
