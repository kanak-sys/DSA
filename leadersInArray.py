class Solution:
    def leaders(self, arr):
        ans = []
        n = len(arr)
        for i in range(n):
            leader = True
            for j in range(i+1, n):
                if arr[j] > arr[i]:
                    leader = False
                    break
            if leader:
                ans.append(arr[i])
        return ans


    def leaders2(self, arr1):
        n1=len(arr1)
        maximum = arr1[-1]
        ans1 = []
        ans1.append(maximum)
        for i in range(n1-2, -1, -1):
            if arr1[i] > maximum:
                maximum = arr1[i]
                ans1.append(maximum)
        ans1.reverse()
        return ans1