class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return left


# Create an instance of the Solution class
solution = Solution()

# Call the searchInsert method
nums = [1, 3, 5, 6]
target = 5
result = solution.searchInsert(nums, target)

print(result)
