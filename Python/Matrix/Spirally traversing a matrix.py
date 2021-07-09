class Solution:
    
    #Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self,matrix, r, c): 
        # code here 
        top=0
        left=0
        down=r-1
        right=c-1
        dir=0
        ans=[]
        while(top<=down and left<=right):
            if(dir==0):
                for i in range(left,right+1):
                    ans.append(matrix[top][i])
                top+=1
            elif(dir==1):
                for i in range(top,down+1):
                    ans.append(matrix[i][right])
                right-=1
            elif(dir==2):
                for i in range(right,left-1,-1):
                    ans.append(matrix[down][i])
                down-=1
            elif(dir==3):
                for i in range(down,top-1,-1):
                    ans.append(matrix[i][left])
                left+=1
            dir=(dir+1)%4
        return ans
        
        
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(r):
            row=[]
            for j in range(c):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.spirallyTraverse(matrix,r,c)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends