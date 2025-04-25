import pathlib
import os

os.path.realpath(__file__)
circle_file = pathlib.Path(os.path.realpath(__file__)).parent.joinpath('circle.txt')
dots_file = pathlib.Path(os.path.realpath(__file__)).parent.joinpath('dot.txt')

def circle_params(circle_path):
    circle = {
        "center": {
            "x": 1000,
            "y": 1000
        },
        "r": -3
    }
    data = []
    with open(circle_path, "r", encoding="utf-8") as f:
        data = [line.strip() for line in f]
    item = str(data[0]).split(' ')
    circle["center"]["x"] = int(str(data[0]).split(' ')[0])
    circle["center"]["y"] = int(str(data[0]).split(' ')[1])
    circle["r"] = int(str(data[1]))
    return circle

def point_on_circle(x, y, circle):
    resolution = -3
    D = (pow((x - circle["center"]["x"]), 2) + pow((y - circle["center"]["y"]),2))
    if (D == pow(circle["r"],2)):
        resolution = 0
    else:
        if D < pow(circle["r"],2):
            resolution = 1
        else:
            resolution = 2
    return resolution


### 0 - лежит на окружности if ((x - x0)^2 + (y - y0)^2) == r^2: return true else: false
### 1 - точка внутри
### 2 - точка снаружи
if __name__=="__main__":
    circle = circle_params(circle_file)
    print("ВНИМАНИЕ! ЕСЛИ ВНУТРИ ТО 1! ЕСЛИ СНАРУЖИ ТО 2. НУ А ЕСЛИ НА ТО 0!")
    with open(dots_file, "r", encoding="utf-8") as f:
        data = [line.strip() for line in f]
        for dot in data:
            x = int(dot.split(' ')[0])
            y = int(dot.split(' ')[1])
            print('x=' + str(x) + ', y=' + str(y) + ' Результат: ' + str(point_on_circle(x,y, circle)))