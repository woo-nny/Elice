
def maxSubArray(nums):
    m_start_index=0
    m_end_index= 1
    start_index=0
    end_index=0

    num_sum=nums[0] # 값을 더한 값
    num_max_sum=nums[0] #값을 더한 값중에 가장 큰 값

    for i in range(len(nums)):
        if nums[i]> nums[i]+num_sum:
            num_sum = nums[i]
            start_index=i
            end_index=i+1
        else:
            num_sum += nums[i]
            end_index = i+1
        
        if num_sum > num_max_sum:
            num_max_sum = num_sum
            m_start_index = start_index
            m_end_index = end_index
    return num_max_sum


def main():
    print(maxSubArray([-10, -7, 5, -7, 10, 5, -2, 17, -25, 1])) # 30이 리턴되어야 합니다

if __name__ == "__main__":
    main()