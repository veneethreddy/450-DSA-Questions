
class Solution:
    #Function to partition the array around the range such 
    #that array is divided into three parts.
    def threeWayPartition(self, arr, a, b):
        # code here 
        n=len(arr)
        l=0
        h=n-1
        i=0
        while(i<=h):
            
            if arr[i]<a:
                arr[i],arr[l]=arr[l],arr[i]
                l+=1
                i+=1
            elif arr[i]>b:
                arr[i],arr[h]=arr[h],arr[i]
                h-=1
            else:
                i+=1
        
        '''c=[]
        d=[]
        e=[]
        for i in array:
            if i<a:
                c.append(i)
            elif(i>=a and i<=b):
                d.append(i)
            else:
                e.append(i)
        for i in d:
            c.append(i)
        for i in e:
            c.append(i)
        for i in range(len(c)-1):
            if c[i]>c[i+1]:
                t=c[i]
                c[i]=c[i+1]
                c[i+1]=t
        print(c)'''        

#{ 
#  Driver Code Starts
#Initial template for Python

from collections import Counter

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        array = list(map(int, input().strip().split()))
        original = Counter(array)
        a,b = list(map(int, input().strip().split()))
        ob = Solution()
        ob.threeWayPartition(array, a, b)

        k1 = k2 = k3 = 0
        for e in array:
            if e > a:
                k3+=1
            elif e<=a and e>=b:
                k2+=1
            elif e<a:
                k1+=1

        m1 = m2 = m3 = 0
        for e in range(k1):
            if array[e]<a:
                m1+=1
        for e in range(k1, k1+k2):
            if array[e]<=a and array[e]>=b:
                m2+=1
        for e in range(k1+k2, k1+k2+k3):
            if array[e]>=a:
                m3+=1

        flag = False
        if k1==m1 and k2==m2 and k3==m3:
            flag = True
        for e in range(len(array)):
            original[array[e]]-=1
        for e in range(len(array)):
            if original[array[e]]!=0:
                flag = False
        if flag:
            print(1)
        else:
            print(0)