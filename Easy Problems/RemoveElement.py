# https://leetcode.com/problems/remove-element?envType=problem-list-v2&envId=array

nums = [0,1,2,2,3,0,4,2]
val = 2

def removeElement( nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k    

print(removeElement(nums, val))       