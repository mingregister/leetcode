# -*- coding:utf-8 -*-
# author: mingregister
# date：2020-04-18,10:31 

from __future__ import annotations

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        if steps == 1:
            ans = 1
            return ans
        # if steps == 2:
        #     ans = 2
        #     return 2
        # if steps == 3

if __name__ == '__main__':
    height = [1,2,4,3]
    # height = [1,8,6,2,5,4,8,3,7]
    s = Solution()
    a = s.maxArea(height)
    print(a)
