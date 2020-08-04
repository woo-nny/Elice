def moveZerosToEnd(nums):
    # 내가 풀어본것
	# result=[]
    # cnt = 0
    # for i in range(len(nums)):
    #     if nums[i] ==0:
    #         cnt +=1
    #     else:
    #         result.append(nums[i])
    # return result+([0]*cnt)
	currentPosition = 0
	
	for i in range(len(nums)):
		if nums[i] != 0:
			nums[currentPosition] = nums[i]
			if i != currentPosition:
				nums[i] =0
			currentPosition += 1
	
	return nums

def main():
    print(moveZerosToEnd([0, 8, 0, 37, 4, 5, 0, 50, 0, 34, 0, 0]))

if __name__ == "__main__":
    main()
