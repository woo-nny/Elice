
def convertTo1(num):
    num_list = [0 for _ in range(num+1)]
    #전체 숫자 횟수 리스트
    for i in range(2, num+1):
        num_list[i] = num_list[i-1] + 1  

        if i%2 == 0 and num_list[i] > num_list[i//2] + 1 :
            num_list[i] = num_list[i//2]+1
        
        if i%3 == 0 and num_list[i] > num_list[i//3] + 1 :
            num_list[i] = num_list[i//3] + 1
    return num_list[num]
def main():
    print(convertTo1(10))

if __name__ == "__main__":
    main()
