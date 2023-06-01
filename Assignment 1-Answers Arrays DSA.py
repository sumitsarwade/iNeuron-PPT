#Assignment 1- Answers Arrays | DSA
#Q1. ANS

def twoSum(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
    return []

# Get user input for nums array
nums = input("Enter the numbers separated by spaces: ").split()
nums = [int(num) for num in nums]

# Get user input for target value
target = int(input("Enter the target value: "))

result = twoSum(nums, target)
print(result)



Q2 Ans

def removeElement(nums, val):
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i

# Get user input for nums array
nums = input("Enter the numbers separated by spaces: ").split()
nums = [int(num) for num in nums]

# Get user input for val
val = int(input("Enter the value to remove: "))

k = removeElement(nums, val)
print("k =", k)
print("nums =", nums[:k], end="")
print("_* " * (len(nums) - k))



Q3. ANS
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

# Get user input for nums array
nums = input("Enter the numbers separated by spaces: ").split()
nums = [int(num) for num in nums]

# Get user input for target value
target = int(input("Enter the target value: "))

index = searchInsert(nums, target)
print(index)


Q4. ANS

def plusOne(digits):
    n = len(digits)
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits

# Get user input for digits array
digits = input("Enter the digits separated by spaces: ").split()
digits = [int(digit) for digit in digits]

result = plusOne(digits)
print(result)


Q5. ANS


def merge(nums1, m, nums2, n):
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] >= nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    nums1[:p2 + 1] = nums2[:p2 + 1]

# Example usage
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

merge(nums1, m, nums2, n)
print(nums1)  # Output: [1, 2, 2, 3, 5, 6]



Q6ANS


def containsDuplicate(nums):
    num_set = set()
    for num in nums:
        if num in num_set:
            return True
        num_set.add(num)
    return False

# Get user input for nums array
nums = input("Enter the numbers separated by spaces: ").split()
nums = [int(num) for num in nums]

result = containsDuplicate(nums)
print(result)


Q7. ANS

def moveZeroes(nums):
    zero_idx = 0

    # Move non-zero elements to the front of the array
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zero_idx] = nums[zero_idx], nums[i]
            zero_idx += 1

# Get user input for nums array
nums = input("Enter the numbers separated by spaces: ").split()
nums = [int(num) for num in nums]

moveZeroes(nums)
print(nums)



Q8. ANS

def findErrorNums(nums):
    n = len(nums)
    num_set = set()
    duplicate_num = -1
    missing_num = -1

    # Find the duplicate number
    for num in nums:
        if num in num_set:
            duplicate_num = num
        else:
            num_set.add(num)

    # Find the missing number
    for num in range(1, n + 1):
        if num not in num_set:
            missing_num = num
            break

    return [duplicate_num, missing_num]

# Get user input for nums array
nums = input("Enter the numbers separated by spaces: ").split()
nums = [int(num) for num in nums]

result = findErrorNums(nums)
print(result)

