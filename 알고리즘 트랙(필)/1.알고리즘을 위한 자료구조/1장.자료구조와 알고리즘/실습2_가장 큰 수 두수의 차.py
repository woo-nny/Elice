
def maxTwoDiff(nums):
    # 내가 푼거
    # nums.sort(reverse=True) : O(NlogN)
    # return nums[0]-nums[-1]
    # max,min ->  최댓값, 최솟값 O(N0)
    return max(nums) -min(nums)
    
def main():
    print(maxTwoDiff([2, 8, 19, 37, 4, 5, 12, 50, 1, 34, 23])) # 49가 리턴되어야 합니다.

if __name__ == "__main__":
    main()
