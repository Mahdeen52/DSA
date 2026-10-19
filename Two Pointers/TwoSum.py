class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        indexed_nums = sorted(enumerate(nums), key=lambda x:x[1])
        i,j = 0, len(nums)-1
        while i<j :
            sum=indexed_nums[i][1]+indexed_nums[j][1]
            if sum == target :
                return [indexed_nums[i][0], indexed_nums[j][0]]
            elif sum > target:
                j-=1 
            elif sum < target:
                i+=1
        return []