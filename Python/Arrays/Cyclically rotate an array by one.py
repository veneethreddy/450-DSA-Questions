def rotate(arr, n):
    '''t=arr[:n-1]
    d=[str(i) for i in t]
    res=' '.join(d)
    r=arr[-1]
    print(str(r),res)'''
    x=arr[n-1]
    arr.pop(n-1)
    return arr.insert(0,x)

  
#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        rotate(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()



