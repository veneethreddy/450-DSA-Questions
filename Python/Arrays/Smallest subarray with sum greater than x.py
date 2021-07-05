class Solution:
    def sb(self, arr, n, x):
        # Your code goes here 
        curr_sum = 0
        min_len = n + 1

    # Initialize starting and ending indexes
        start = 0
        end = 0
        while (end < n):

        # Keep adding array elements while current
        # sum is smaller than or equal to x
            while (curr_sum <= x and end < n):
                curr_sum += arr[end]
                end += 1

        # If current sum becomes greater than x.
            while (curr_sum > x and start < n):

            # Update minimum length if needed
                if (end - start < min_len):
                    min_len = end - start

            # remove starting elements
                curr_sum -= arr[start]
                start += 1

        return min_len

                


#{ 
#  Driver Code Starts
def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a = [int(x) for x in input().strip().split()]
        print(Solution().sb(a, n, m))

        T -= 1


if __name__ == "__main__":
    main()
