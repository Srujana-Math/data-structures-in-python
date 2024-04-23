num=[10,5,85,45,64,52,48,14,78,11]
def performBubbleSort(nums):
    n = len(num)
    # n = 6
    # 5 4 3 2 1 
    for fixThisIndex in range(n - 1, 0, -1):
        for index in range(fixThisIndex):
            if num[index] > num[index + 1]:
                temp = nums[index]
                num[index] = num[index + 1]
                num[index + 1] = temp
        print(nums)
 
#nums = [12, 2, 34, 20, 56, 43, 45, 100, 89, 50]
#nums = list(map(int, input().split()))
print("Before sorting:")
print(num)
performBubbleSort(num)
print("After sorting:")
print(num)
