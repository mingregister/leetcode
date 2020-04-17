# -*- coding:utf-8 -*-
# author: mingregister
# date：2020-04-17,23:30 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, value in enumerate(nums):
            diff = target - value
            if diff in hashmap:
                return [hashmap.get(diff), i] # i应该放在后面的位置
            hashmap[value] = i # 如果hashmap中没有diff值, 则把value作为键/位置索引作为值赋给hashmap(注意位置别颠倒)

# leetcode中不需要开始代码
if __name__ == '__main__':
    nums = [3,2,4]
    target = 6
    s = Solution()
    answer = s.twoSum(nums, target)
    print(answer)