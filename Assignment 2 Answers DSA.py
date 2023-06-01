
#Question 1 Ans
def arrayPairSum(nums):
    nums.sort()
    max_sum = 0
    for i in range(0, len(nums), 2):
        max_sum += min(nums[i], nums[i+1])
    return max_sum
nums = [1, 4, 3, 2]
result = arrayPairSum(nums)
print(result)  # Output: 4


#Question 2 Ans
def maxCandies(candyType):
    unique_candies = set()
    for candy in candyType:
        unique_candies.add(candy)
    num_unique_candies = len(unique_candies)
    max_candies = min(num_unique_candies, len(candyType) // 2)
    return max_candies
candyType = [1, 1, 2, 2, 3, 3]
result = maxCandies(candyType)
print(result)  # Output: 3


#Question 3 Ans
def findLHS(nums):
    num_counts = {}
    for num in nums:
        if num in num_counts:
            num_counts[num] += 1
        else:
            num_counts[num] = 1
    
    max_length = 0
    for num in num_counts:
        if num + 1 in num_counts:
            max_length = max(max_length, num_counts[num] + num_counts[num + 1])
    
    return max_length
nums = [1, 3, 2, 2, 5, 2, 3, 7]
result = findLHS(nums)
print(result)  # Output: 5

#Question 4 Ans
def canPlaceFlowers(flowerbed, n):
    length = len(flowerbed)
    count = 0
    i = 0
    while i < length:
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == length - 1 or flowerbed[i + 1] == 0):
            flowerbed[i] = 1
            count += 1
        i += 1
        if count >= n:
            return True
    return False
flowerbed = [1, 0, 0, 0, 1]
n = 1
result = canPlaceFlowers(flowerbed, n)
print(result)  # Output: True


#Question 5 Ans
def maximumProduct(nums):
    nums.sort()
    n = len(nums)
    return max(nums[n-1] * nums[n-2] * nums[n-3], nums[0] * nums[1] * nums[n-1])
nums = [1, 2, 3]
result = maximumProduct(nums)
print(result)  # Output: 6



#Question 6 Ans
def search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
nums = [-1, 0, 3, 5, 9, 12]
target = 9
result = search(nums, target)
print(result)  # Output: 4


#Question 7 Ans
def isMonotonic(nums):
    isIncreasing = True
    isDecreasing = True

    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            isIncreasing = False
        if nums[i] > nums[i - 1]:
            isDecreasing = False
        if not isIncreasing and not isDecreasing:
            return False

    return True
nums = [1, 2, 2, 3]
result = isMonotonic(nums)
print(result)  # Output: True



#Question 8 Ans

def minDifference(nums, k):
    if len(nums) <= 4:
        return 0
    
    nums.sort()
    min_num = min(nums)
    max_num = max(nums)

    if min_num + k >= max_num - k:
        return 0

    return max_num - k - (min_num + k)
nums = [1]
k = 0
result = minDifference(nums, k)
print(result)  # Output: 0






