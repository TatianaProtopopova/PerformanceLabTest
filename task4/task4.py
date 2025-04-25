import os
import pathlib
import sys

numsFile = sys.argv[1]

if __name__=="__main__":
    print('TASK 4!!!!')
    nums = []
    sum = 0
    avg = -1323
    steps = 0
    with open(numsFile, "r", encoding="utf-8") as f:
        data = [line.strip() for line in f]
        for item in data:
            sum += int(item)
            nums.append(int(item))
            if (int(item) < 0):
                raise ValueError("Число не может быть отрицательным")
    avg = sum // len(data)
    for item in nums:
        steps += abs(item - avg)
    print('количество шагов: ' + str(steps))
    print('Число к которому приводим: ' + str(avg))
