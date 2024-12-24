import re

def main():
    filename = 'input'

    array1, array2 = read_file_to_array(filename)
    print('Ejercicio 1: ', ej1(array1, array2))
    print('Ejercicio 2: ', ej2(array1, array2))


def ej1(array1, array2):
    array_result = []
    result = 0
    array1.sort()
    array2.sort()
    for i in range(len(array1)):
        array_result.append(abs(array1[i] - array2[i]))
    for n in array_result:
        result += n
    return result

def ej2(array1, array2):
    array_result = []
    result = 0
    for i in range(len(array1)):
        array_result.append(array1[i] * array2.count(array1[i]))
    for n in array_result:
        result += n
    return result

def read_file_to_array(filename):
    array1 = []
    array2 = []
    pattern = re.compile(r'(\d+)   (\d+)')
    with open(filename, 'r') as file:
        for line in file:
            match = pattern.match(line.strip())
            array1.append(int(match.group(1)))
            array2.append(int(match.group(2)))
    return array1, array2

if __name__ == "__main__":
    main()