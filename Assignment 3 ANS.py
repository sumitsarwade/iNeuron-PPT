                                                                                Assignment 3 ANS
-------------------------------------------------------------------------------------------------------------------------------------------------------------

#Question 1: Three Sum Closest Ans

def threeSumClosest(nums, target):
    nums.sort()
    closestSum = float('inf')
    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            currentSum = nums[i] + nums[left] + nums[right]
            if abs(currentSum - target) < abs(closestSum - target):
                closestSum = currentSum
            if currentSum < target:
                left += 1
            elif currentSum > target:
                right -= 1
            else:
                return target
    return closestSum
nums = [-1, 2, 1, -4]
target = 1
print(threeSumClosest(nums, target))

-------------------------------------------------------------------------------------------------------------------------------------------------------------
#Question 2 Ans
def fourSum(nums, target):
    nums.sort()
    n = len(nums)
    result = []
    
    for i in range(n-3):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        for j in range(i+1, n-2):
            if j > i+1 and nums[j] == nums[j-1]:
                continue
            
            left = j+1
            right = n-1
            
            while left < right:
                curr_sum = nums[i] + nums[j] + nums[left] + nums[right]
                
                if curr_sum == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif curr_sum < target:
                    left += 1
                else:
                    right -= 1
    
    return result
nums = [1, 0, -1, 0, -2, 2]
target = 0
print(fourSum(nums, target))
#OP == [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

-------------------------------------------------------------------------------------------------------------------------------------------------------------


#Question 3 ANS
def nextPermutation(nums):
    n = len(nums)
    i = n - 2
    
    # Find the first pair of adjacent elements where nums[i] < nums[i+1]
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    
    if i >= 0:
        j = n - 1
        
        # Find the smallest element to the right of nums[i] that is greater than nums[i]
        while j >= 0 and nums[j] <= nums[i]:
            j -= 1
        
        # Swap nums[i] and nums[j]
        nums[i], nums[j] = nums[j], nums[i]
    
    # Reverse the subarray starting from index i+1
    left = i + 1
    right = n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    
    return nums
nums = [1, 2, 3]
print(nextPermutation(nums))
#OP====[1, 3, 2]

-------------------------------------------------------------------------------------------------------------------------------------------------------------


#Question 4 ANS
def searchInsert(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return left
nums = [1, 3, 5, 6]
target = 5
print(searchInsert(nums, target))
#OP=2

-------------------------------------------------------------------------------------------------------------------------------------------------------------

#Question 5: Increment Large Integer ANS

def plusOne(digits):
    carry = 1
    n = len(digits)
    
    for i in range(n - 1, -1, -1):
        digit_sum = digits[i] + carry
        new_digit = digit_sum % 10
        carry = digit_sum // 10
        digits[i] = new_digit
    
    if carry == 1:
        digits.insert(0, 1)
    
    return digits
digits = [1, 2, 3]
print(plusOne(digits))
#Output:[1, 2, 4]

-------------------------------------------------------------------------------------------------------------------------------------------------------------

#Question 6: Find Single Number ANS

def singleNumber(nums):
    result = 0
    
    for num in nums:
        result ^= num
    
    return result
nums = [2, 2, 1]
print(singleNumber(nums))
#Output:1

-------------------------------------------------------------------------------------------------------------------------------------------------------------
#Question 7: Missing Ranges ANS

def findMissingRanges(nums, lower, upper):
    result = []
    start = lower
    
    for num in nums:
        if num == start:
            start += 1
        elif num > start:
            result.append(getRange(start, num - 1))
            start = num + 1
    
    if start <= upper:
        result.append(getRange(start, upper))
    
    return result

def getRange(start, end):
    if start == end:
        return str(start)
    else:
        return str(start) + "->" + str(end)

nums = [0, 1, 3, 50, 75]
lower = 0
upper = 99
print(findMissingRanges(nums, lower, upper))
##Output:['2', '4->49', '51->74', '76->99']

-------------------------------------------------------------------------------------------------------------------------------------------------------------

#Question 8: Meeting Rooms ANS

def canAttendMeetings(intervals):
    intervals.sort(key=lambda x: x[0])  # Sort intervals based on start times

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False

    return True
intervals = [[0, 30], [5, 10], [15, 20]]
print(canAttendMeetings(intervals))

##Output:False



