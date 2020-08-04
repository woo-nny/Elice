
def josephus(num, target):
    ans_list =[]
    num_list = list(range(1,num+1))
    temp =target-1
    for _ in range(num):
        if len(num_list) > temp: # 위치가 리스트를 넘지 않은 경우
            ans_list.append(num_list.pop(temp)) # 답추가
            temp += target-1 # 다음 위치로 이동
        elif len(num_list) <= temp: #위치가 리스트를 넘는 경우
            temp = temp % len(num_list)
            ans_list.append(num_list.pop(temp))
            temp += target-1
    return ans_list

def main():
    print(josephus(7, 3)) #[3, 6, 2, 7, 5, 1, 4]이 반환되어야 합니다

if __name__ == "__main__":
    main()