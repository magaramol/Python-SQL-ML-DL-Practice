class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        result=0
        forward=0
        current=0
        
        while forward<len(nums):
            if nums[forward]!=val:
                result+=1
                nums[current]=nums[forward]
                forward+=1
                current+=1
            else:
                forward+=1
        return result

        
