def performSelectionSort(nums):
    n = len(nums)
    for i in range(n - 1, 0, -1):
        maxEle = nums[i]
        maxEleIndex = i 
        for j in range(i):
            if nums[j] > maxEle:
                maxEleIndex = j 
                maxEle = nums[j]
        if i != maxEleIndex:
            temp = nums[maxEleIndex]
            nums[maxEleIndex] = nums[i]
            nums[i] = temp
        print(nums)
nums = [12, 2, 34, 20, 56, 43, 45, 100, 89, 50]
 
print("Before sorting:")
print(nums) 
performSelectionSort(nums)
print("After sorting:")
print(nums)
