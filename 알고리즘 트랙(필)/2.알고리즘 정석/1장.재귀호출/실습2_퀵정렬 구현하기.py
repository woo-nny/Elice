def quickSort(array):
    '''
    퀵정렬을 통해 오름차순으로 정렬된 array를반환하는 함수를 작성하세요.
    '''
    if len(array) <= 1:
        return array
    
    pivot = array[0]

    left = getSmall(array[1:],pivot)
    right = getLarge(array[1:],pivot)

    return quickSort(left) + [pivot] + quickSort(right)
def getSmall(array,pivot):
    data = []
    for a in array:
        if a<= pivot:
            data.append(a)
    return data
def getLarge(array,pivot):
    data = []
    for a in array:
        if a> pivot:
            data.append(a)
    return data
    


def main():
    line = [int(x) for x in input().split()]

    print(*quickSort(line))

if __name__ == "__main__":
    main()
