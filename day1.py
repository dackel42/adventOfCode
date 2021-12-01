def task1 ():
    input = open("day1_task1.txt", "r").readlines()
    previousNumber = 0
    n = -1
    for a in input:
        if int(a) > previousNumber: 
            n += 1
        previousNumber = int(a)
    print(n)

task1()



def task2 ():
    input = open("day1_task2.txt", "r").readlines()

    for index in range(len(input)): 
        input[index] = int(input[index])

    n = -1
    previousNumberTrioSum = 0
    for index in range(len(input)-2):
        sum = 0
        for i in range (3):
            sum += input[index + i]
        if sum > previousNumberTrioSum:
            n += 1
        previousNumberTrioSum = sum
    print(n)

task2()