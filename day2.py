def task1 ():
    input = open("day2_task1.txt", "r").readlines()
    x = 0
    y = 0#
    for i in input:
        instruction = i.split(" ")[0]
        value = int(i.split(" ")[1]) 
        if instruction == "forward":
            x += value
        if instruction == "up":
            y -= value
        if instruction == "down":
            y += value
    print(x*y)

task1()

def task2 ():
    input = open("day2_task1.txt", "r").readlines()
    x = 0
    y = 0
    aim = 0
    for i in input:
        instruction = i.split(" ")[0]
        value = int(i.split(" ")[1]) 
        if instruction == "forward":
            x += value
            y += (aim * value)
        if instruction == "up":
            aim -= value
        if instruction == "down":
            aim += value
    print(x*y)

task2()