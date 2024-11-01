from typing import List


def nextGreaterElement(nums: List[int]) -> List[int]:
    # TC: O(n), SC: O(n)
    stack = []
    res = [-1] * len(nums)
    for i in range(len(nums)-1, -1, -1):
        while stack and nums[i] > stack[-1]:
            stack.pop()
        
        res[i] = stack[-1] if stack else -1
        stack.append(nums[i])
    
    return res


if __name__ == "__main__":
    nums = [1, 3, 4, 2]
    print(nextGreaterElement(nums))  # [3, 4, -1, -1]

    nums = [1, 5, 7, 4, 8, 9]
    print(nextGreaterElement(nums))  # [5, 7, 8, 8, 9, -1]
