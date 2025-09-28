class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr_sum=nums[0]
        max_sum=nums[0]

        curr_min=nums[0]
        min_sum=nums[0]

        total_sum=nums[0]

        for i in range(1,len(nums)):
            x=nums[i]
            total_sum+=x
            curr_sum=max(x,x+curr_sum)
            max_sum=max(max_sum,curr_sum)

            curr_min=min(x,x+curr_min)
            min_sum=min(min_sum,curr_min)

        if max_sum<0:
            return max_sum
        return max(max_sum,total_sum-min_sum)

        