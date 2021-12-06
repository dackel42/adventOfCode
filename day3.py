def task1 ():
    input = open("day3_task1.txt", "r").readlines()
    
    
    epsilon = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    gamma =  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
    
    for i in input:
        zero = 0
        one = 0
        if int(i.split(" ")[i]) == 0:   zero += 1
        if int(i.split(" ")[i]) == 1:   one += 1
    
    bin()

task1()