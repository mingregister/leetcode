# -*- coding:utf-8 -*-
# author: mingregister
# date：2020-04-18,00:22 

# my answer, 超时了。
# 我这里是只考虑了*单指针*
class Solution:
    def maxArea(self, height):
        max = 0
        length = len(height)
        if length ==2:
            return min(height)

        for standard in reversed(range(length)):
            for i in range(length):
                if height[i] >= height[standard]:
                    if height[standard]*(standard-i) > max:
                        max = height[standard]*(standard-i)
                        print("first height[standard]: %d, height[i]: %d, standard: %d, i: %d" %(height[standard],height[i], standard,i))
                        continue
                else:
                    if height[i]*(standard-i) > max:
                        max = height[i]*(standard-i)
                        print("second height[standard]: %d, height[i]: %d, standard: %d, i: %d" %(height[standard],height[i], standard,i))
                        continue
        return max

// 官方双指针方案
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            ans = max(ans, area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return ans

if __name__ == '__main__':
    height = [1,2,4,3]
    # height = [1,8,6,2,5,4,8,3,7]
    s = Solution()
    a = s.maxArea(height)
    print(a)
