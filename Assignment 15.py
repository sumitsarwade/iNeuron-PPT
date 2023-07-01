                                                                               # Assignment 15
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#Questions 1 Ans

def find_next_greater_elements(arr):
    stack = []  # Stack to store indices of elements
    result = [-1] * len(arr)  # Initialize result array with -1

    for i in range(len(arr)):
        # Process elements from right to left
        while stack and arr[i] > arr[stack[-1]]:
            
            result[stack.pop()] = arr[i]

        stack.append(i)  # Push the current element's index to the stack

    return result
arr = [4, 5, 2, 25, 10, 8]

output = find_next_greater_elements(arr)

print(output)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#Questions 2 Ans

def find_nearest_smaller_elements(arr):
    stack = []  # Stack to store elements
    result = []  # List to store the nearest smaller elements

    for i in range(len(arr)):
        # Process elements from left to right
        while stack and stack[-1] >= arr[i]:
            # Pop elements from the stack until a smaller element is found or the stack becomes empty
            stack.pop()

        if stack:
            result.append(stack[-1])  # Append the nearest smaller element found
        else:
            result.append(-1)  # No smaller element found

        stack.append(arr[i])  # Push the current element to the stack

    return result
arr = [1, 6, 2]

output = find_nearest_smaller_elements(arr)

print(output)
