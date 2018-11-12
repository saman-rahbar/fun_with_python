#! \usr\bin\env\ python3

"""
Question_1:

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

"""
 
#Solution_Question_1:

class Solution:
    def twoSum(self, nums, target):
        """
            :type nums: List[int]
            :type target: int
            :rtype: List[int]
        """
        self.nums = nums
        self.target = target
        self.final_list = []
        for i, num in enumerate(nums):
            n = abs(self.target - num)
            if n in self.nums:
                self.final_list.append((self.nums).index(num))

        print(self.final_list)


example_1 = Solution()
example_1.twoSum([1, 4, 15, 3], 7)






 
#Question_2

"""Finding the longest path in a graph assuming we know the starting point

for this purpose DFS is implemented"""

def DFS(G, v, seen = None, path = None):
	if seen is None: seen = []
	if path is None: path = [v]
	seen.append(v)
	paths = []
	for t in G[v]:
		if t not in seen:
			t_path = path + [t]
			paths.append(tuple(t_path))
			paths.extend(DFS(G,t, seen = [:], t_path))
	
	return paths


G  = defaultdict(list)
for (s, t) in edges:
	G[s].append(t)
	G[t].append(s)


