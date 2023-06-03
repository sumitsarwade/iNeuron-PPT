                                                                          Assignment Ans 4
------------------------------------------------------------------------------------------------------------------------------------------------------------

Question 1 Ans


def findCommonElements(arr1, arr2, arr3):
    p1, p2, p3 = 0, 0, 0
    result = []

    while p1 < len(arr1) and p2 < len(arr2) and p3 < len(arr3):
        if arr1[p1] == arr2[p2] == arr3[p3]:
            result.append(arr1[p1])
            p1 += 1
            p2 += 1
            p3 += 1
        elif arr1[p1] <= arr2[p2] and arr1[p1] <= arr3[p3]:
            p1 += 1
        elif arr2[p2] <= arr1[p1] and arr2[p2] <= arr3[p3]:
            p2 += 1
        else:
            p3 += 1

    return result
arr1 = [1,2,3,4,5]
arr2 = [1,2,5,7,9]
arr3 = [1,3,4,5,8]

result = findCommonElements(arr1, arr2, arr3)
print(result)
# Output: [1, 5]

------------------------------------------------------------------------------------------------------------------------------------------------------------

Question 2 Ans

def findDistinctIntegers(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)

    result1 = set1 - set2
    result2 = set2 - set1

    return [list(result1), list(result2)]
nums1 = [1, 2, 3]
nums2 = [2, 4, 6]

result = findDistinctIntegers(nums1, nums2)
print(result)
# Output: [[1, 3], [4, 6]]

------------------------------------------------------------------------------------------------------------------------------------------------------------

Question 3 Ans

def transposeMatrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    result = [[0] * rows for _ in range(columns)]

    for row in range(rows):
        for column in range(columns):
            result[column][row] = matrix[row][column]

    return result
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

result = transposeMatrix(matrix)
print(result)

# Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

------------------------------------------------------------------------------------------------------------------------------------------------------------

Question 4 Ans

def arrayPairSum(nums):
    nums.sort()
    max_sum = 0

    for i in range(0, len(nums), 2):
        max_sum += nums[i]

    return max_sum
nums = [1, 4, 3, 2]

result = arrayPairSum(nums)
print(result)
# Output: 4

------------------------------------------------------------------------------------------------------------------------------------------------------------

Question 5 Ans


def arrangeCoins(n):
    left = 1
    right = n

    while left <= right:
        mid = (left + right) // 2
        total_coins = (mid * (mid + 1)) // 2

        if total_coins == n:
            return mid
        elif total_coins > n:
            right = mid - 1
        else:
            left = mid + 1

    return right

n = 5

result = arrangeCoins(n)
print(result)
# Output: 2

------------------------------------------------------------------------------------------------------------------------------------------------------------

Question 6 Ans

def sortedSquares(nums):
    left = 0
    right = len(nums) - 1
    squares = []

    while left <= right:
        left_square = nums[left] * nums[left]
        right_square = nums[right] * nums[right]

        if left_square > right_square:
            squares.insert(0, left_square)
            left += 1
        else:
            squares.insert(0, right_square)
            right -= 1

    while left < len(nums):
        squares.insert(0, nums[left] * nums[left])
        left += 1

    while right >= 0:
        squares.insert(0, nums[right] * nums[right])
        right -= 1

    return squares[::-1]
nums = [-4, -1, 0, 3, 10]

result = sortedSquares(nums)
print(result)
# Output: [0, 1, 9, 16, 100]
------------------------------------------------------------------------------------------------------------------------------------------------------------

Question 7 Ans



def maxCount(m, n, ops):
    min_row = m
    min_col = n

    for operation in ops:
        min_row = min(min_row, operation[0])
        min_col = min(min_col, operation[1])

    return min_row * min_col
m = 3
n = 3
ops = [[2, 2], [3, 3]]

result = maxCount(m, n, ops)
print(result)
# Output: 4

------------------------------------------------------------------------------------------------------------------------------------------------------------


Question 8 Ans


def shuffle(nums, n):
    result = []

    for i in range(n):
        result.append(nums[i])
        result.append(nums[i + n])

    return result
nums = [2, 5, 1, 3, 4, 7]
n = 3

result = shuffle(nums, n)
print(result)
# Output: [2, 3, 5, 4, 1, 7]

