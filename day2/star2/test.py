def isSafeAnomaly(array):
    direction = array[1] - array[0]
    for i in range(len(array) - 1):
        diff = array[i + 1] - array[i]
        if (diff * direction) < 0 or abs(diff) < 1 or abs(diff) > 3:
            return i
    return -1


def isSafe(array):
    if len(array) == 0:
        return -1
    direction = array[1] - array[0]
    for i in range(len(array) - 1):
        diff = array[i + 1] - array[i]
        if (diff * direction) < 0 or abs(diff) < 1 or abs(diff) > 3:
            return -2
    return -1


sum = 0
with open("input.txt", "r") as file:
    lineNbr = 0
    for line in file:
        lineNbr += 1
        array = list(map(int, line.split()))
        if isSafeAnomaly(array) >= 0:
            index = isSafeAnomaly(array)
            if index == len(array) - 1:
                # print(lineNbr)
                sum += 1
            else:
                array1 = array[:index] + array[index + 1 :]
                array2 = array[: index + 1] + array[index + 2 :]
                if index > 0:
                    array3 = array[: index - 1] + array[index:]
                else:
                    array3 = []
                # print(array1, array2, array3)
                if len(array3) > 0:
                    if (
                        isSafe(array1) == -1
                        or isSafe(array2) == -1
                        or isSafe(array3) == -1
                    ):
                        # print(lineNbr)
                        sum += 1
                else:
                    if isSafe(array1) == -1 or isSafe(array2) == -1:
                        sum += 1
        else:
            # print(lineNbr)
            sum += 1

print(sum)
