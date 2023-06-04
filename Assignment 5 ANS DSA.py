
                                                                                Assignment ANS 5

-------------------------------------------------------------------------------------------------------------------------------------------------------------



Question 1 ANS
def construct2DArray(original, m, n):
    if m * n != len(original):
        return []  # Return empty 2D array if it is impossible

    result = []
    for i in range(m):
        row = original[i * n : (i + 1) * n]
        result.append(row)

    return result
original = [1, 2, 3, 4]
m = 2
n = 2
output = construct2DArray(original, m, n)
print(output)
#output=[[1, 2], [3, 4]]


-------------------------------------------------------------------------------------------------------------------------------------------------------------


Question 2 ANS
def arrangeCoins(n):
    row = 1
    while n >= row:
        n -= row
        row += 1
    return row - 1
n = 5
output = arrangeCoins(n)
print(output)
#output=2


-------------------------------------------------------------------------------------------------------------------------------------------------------------


Question 3 ANS
def sortedSquares(nums):
    result = []
    for num in nums:
        result.append(num * num)
    result.sort()
    return result
nums = [-4, -1, 0, 3, 10]
output = sortedSquares(nums)
print(output)
#output=[0, 1, 9, 16, 100]


-------------------------------------------------------------------------------------------------------------------------------------------------------------

Question 4 ANS
def findDisappearedNumbers(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)

    answer = []
    answer.append(list(set1 - set2))
    answer.append(list(set2 - set1))

    return answer
nums1 = [1, 2, 3]
nums2 = [2, 4, 6]
output = findDisappearedNumbers(nums1, nums2)
print(output)
#output=[[1, 3], [4, 6]]



-------------------------------------------------------------------------------------------------------------------------------------------------------------

Question 5 ANS
def findTheDistanceValue(arr1, arr2, d):
    distance = 0
    for num1 in arr1:
        for num2 in arr2:
            if abs(num1 - num2) <= d:
                break
        else:
            distance += 1

    return distance
arr1 = [4, 5, 8]
arr2 = [10, 9, 1, 8]
d = 2
output = findTheDistanceValue(arr1, arr2, d)
print(output)
#output=2



-------------------------------------------------------------------------------------------------------------------------------------------------------------

Question 6 ANS
def findDuplicates(nums):
    duplicates = []
    for num in nums:
        index = abs(num) - 1
        if nums[index] < 0:
            duplicates.append(abs(num))
        else:
            nums[index] = -nums[index]
    return duplicates
nums = [4, 3, 2, 7, 8, 2, 3, 1]
output = findDuplicates(nums)
print(output)
#output=[2, 3]


-------------------------------------------------------------------------------------------------------------------------------------------------------------
Question 7 ANS
def findMin(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        # Check if the middle element is greater than the last element
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]
nums = [3, 4, 5, 1, 2]
output = findMin(nums)
print(output)
#output=1


-------------------------------------------------------------------------------------------------------------------------------------------------------------
Question 8 ANS
def findOriginalArray(changed):
    if len(changed) % 2 != 0:
        return []

    original = set()
    for num in changed:
        if num % 2 != 0:
            return []
        original_value = num // 2
        if original_value in original:
            original.remove(original_value)
        else:
            original.add(original_value)

    if len(original) == len(changed) // 2:
        return list(original)
    else:
        return []
changed = [1, 3, 4, 2, 6, 8]
output = findOriginalArray(changed)
print(output)
#output=[1, 3, 4]
