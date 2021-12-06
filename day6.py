def task1():
    list = [int(i) for i in open("inputs/day6.txt", "r").read().split(",")]
    for d in range(80): 
        for index, i in enumerate(list):
            list[index] = i - 1
            if list[index] == -1:
                list[index] = 6
                list.append(9)
    print(len(list))

task1()

def task2():
    list = [int(i) for i in open("inputs/day6.txt", "r").read().split(",")]
    for d in range(80): 
        for index, i in enumerate(list):
            list[index] = i - 1
            if list[index] == -1:
                list[index] = 6
                list.append(9)
    print(len(list))

task2()