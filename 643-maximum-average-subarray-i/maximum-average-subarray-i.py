class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        win_sum=sum(nums[:k])#sum of first k elements
        maxi=win_sum/k#storing the current max avrg
        for j in range(k,len(nums)):#silding the window from index to k to end of the array
            win_sum+=nums[j] # adding the next element
            win_sum-=nums[j-k]#subtracting the past element
            avrg=win_sum/k
            maxi=max(maxi,avrg)
        return maxi        