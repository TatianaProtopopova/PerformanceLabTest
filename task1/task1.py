import sys

def build_array(n):
    data = []
    for index in range(n):
        data.append(index+1)
    return  data

def get_index(cursor, lenght):
    if (cursor >= lenght):
        return cursor - lenght
    else:
        return cursor

if __name__=="__main__":
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    data = build_array(n)
    path = []
    cursor = 0
    target = data[0]
    current_value = -1;
    print("Ищем значение: " + str(target))
    print("n значение: " + str(n))
    print("m значение: " + str(m))
    while (current_value != target):
        path.append(data[cursor])
        cursor = get_index((cursor + m-1), len(data))
        current_value = data[cursor]
    print('Путь: ' + str(path))