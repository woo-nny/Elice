
def twoSum(nums, target):
    # for n in nums:
    #     if (target-n) in nums:
    #         return n, (target-n)
    nums.sort() #오름 차순 정렬
    i =0
    j = len(nums) -1
    while i< j:
        sum = nums[i] + nums[j]
        if sum==target:
            return nums[i], nums[j]
        elif sum > target:
            j -=1
        else:
            i +=1
    
def main():
    print(twoSum([2, 8, 19, 37, 4, 5], 12)) # (4, 8) 혹은 (8, 4)가 리턴되어야 합니다.

if __name__ == "__main__":
    main()
