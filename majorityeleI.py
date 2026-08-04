#nums = [2,2,1,1,1,2,2,2]


class Solution:
    def majorityEle1(self, nums):
        count = {} #since dictionary stores key-value
        for n in nums:
            count[n] = count.get(n, 0) + 1  #count[2] = count.get(2, 0) + 1 since 2 doesnot occurs in list before
                                            #count.get returns 0 and count of 2 in dictionary {2:1}
        n = len(nums)       #length here is 7
        for key in count:
            if count[key] > n//2:       #n//2 = 3 if count>3 then majority  count[2] = 4
                return key              #4 >3 therefore returns 2 that is key

class Solution2:
    def majorityEle2(self, nums2):
        nums2.sort()
        return nums2[len(nums2)//2]


class Solution3:
    def majorityEle3(self, nums3):
        candidate = None
        count2 = 0
        for n in nums3:
            if count2 == 0:
                candidate = n
            if n == candidate:
                count2 += 1
            else:
                count2 -= 1
        return candidate