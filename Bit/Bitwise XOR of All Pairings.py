from typing import List


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        '''Approach: Bit. The bitwise xor of all pairings between nums1 and nums2.
        The brute force approach for this would be generate every pairing by xoring
        two elements and then take the xor of nums3. But this approach is inefficient
        So let's take Some observation. We know that xor operation is commutative.
        which means we are xoring the first element of nums1 with every element in 
        nums2 which can be restructure as xoring the first element by itself by the
        length of nums2. So if the length of nums2 is even it would be zero otherwise
        it would be itself. In the same way for every element in nums1 I am doing the
        xor of nums2 so simply we can calculate the xor of the two arrays and based on
        their length we can return our answer accordingly.'''
        first_xor = 0
        for num in nums1:
            first_xor ^= num
        
        second_xor = 0
        for num in nums2:
            second_xor ^= num
        
        #if both of them are even everything will cancel out and we will only have 0
        if len(nums1) % 2 == 0 and len(nums2) % 2 == 0:
            return 0
        
        #if both of them are odd then we will take the xor of the two
        if len(nums1) % 2 != 0 and len(nums2) % 2 != 0:
            return first_xor ^ second_xor
        
        #if one of them are odd take the xor with odd length of nums
        if len(nums2) % 2 != 0:
            return first_xor
        
        return second_xor
        #Time Complexity: O(n+m) where n and m are length of nums1 and nums2 respectively
        #Space Complexity: O(1)