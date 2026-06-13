# sorted in ascending order
# first integer of every row is greaer than last integer of previous row
# maybe we can split by rows
# two binary searches?

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start_i = 0
        end_i = len(matrix) - 1



        while start_i <= end_i:
            middle = start_i + (end_i - start_i)
            mid_v = matrix[middle]

            if mid_v[0] <= target and mid_v[-1] >= target:

                start_ii = 0
                end_ii = len(mid_v) - 1

                while start_ii <= end_ii:
                    midmid = start_ii + (end_ii - start_ii)
                    midmid_v = mid_v[midmid]

                    if midmid_v == target:
                        return True
                    elif midmid_v > target:
                        end_ii = midmid - 1
                    else:
                        start_ii = midmid + 1
                
                return False
            
            elif mid_v[0] > target:
                end_i = middle - 1
            else:
                start_i = middle + 1
        return False
        