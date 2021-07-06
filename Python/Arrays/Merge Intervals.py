class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    
    # sort the array
        intervals.sort(key = lambda i: i[0])
    
    # start at the 1st 
        res = [intervals[0]]
    
    # check others
        for start, end in intervals[1:]:
        
            if start <= res[-1][1]:
                res[-1][1] = max(end, res[-1][1])
            
        # if not overlap, append
            else:
                res.append([start, end]) 
        return res
        