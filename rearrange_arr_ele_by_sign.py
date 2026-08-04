from typing import List
class Solution:
    def rearrange(self, nums: List[int]):
        pos = []
        neg = []
        ans = []
        for n in nums:
            if n>=0:
                pos.append(n)
            else:
                neg.append(n)
        for i in range(len(pos)):
            ans.append(pos[i])
            ans.append(neg[i])
        return ans

    def rearrange2(self, nums1: List[int]):
        n1=len(nums1)
        ans1 = [0]*n1
        pos1 = 0
        neg1 = 1
        for num in nums1:
            if num > 0:
                ans1[pos1] = num
                pos1 += 2
            else:
                ans1[neg1] = num
                neg1 += 2
        return ans1