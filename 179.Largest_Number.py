class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)
        nums = list(map(str,nums))
        for i in range(n):
            for j in range(0,n-i-1):
                if nums[j] + nums[j + 1] < nums[j + 1] + nums[j]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    
        if nums[0] == '0':
            return '0'

        return ''.join(nums)
