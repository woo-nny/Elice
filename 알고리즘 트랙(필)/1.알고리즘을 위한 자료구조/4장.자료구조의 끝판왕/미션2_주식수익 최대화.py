
def maximizeProfit(nums):
    max_profit = 0
    min_price = nums[0]
    for i in range(1,len(nums)):
        profit = nums[i] - min_price
        if profit > max_profit:
            max_profit = profit
        if nums[i] < min_price:
            min_price = nums[i]
    return max_profit

def main():
    print(maximizeProfit([1,2,3,4,5,6,7])) # 6
    print(maximizeProfit([7,6,5,4,3,2,1])) # 0
    print(maximizeProfit([1,2,3,4,3,2,1])) # 3
    print(maximizeProfit([2,8,19,37,4,5])) # 35

if __name__ == "__main__":
    main()