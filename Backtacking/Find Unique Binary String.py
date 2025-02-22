from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums = set(nums)
        def backtrack(index):
            if index == len(nums):
                if "".join(result) not in nums:
                    return "".join(result)
                
                return ""
            non_pick = backtrack(index+1)
            if non_pick:
                return non_pick
            result[index] = '1'
            pick = backtrack(index+1)
            result[index] = '0'
            if pick:
                return pick
            
            return ""
        result = ['0' for _ in range(len(nums))]
        if "".join(result) not in nums:
            return "".join(result)
        for i in range(len(nums)-1,-1,-1):
            result[i] = '1'
            answer = backtrack(i+1)
            if answer:
                return answer
        