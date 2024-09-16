class Solution:
    def subArraySum(self,arr, n, s): 
        
       for i in range(n):
           for j in range(i+1,n):
               if arr[i]+arr[j]==s:
                   return i,j

a=Solution()
d=a.subArraySum([1,2,3,7,5],5,12)
print (d)