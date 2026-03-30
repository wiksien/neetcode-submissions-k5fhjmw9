class Solution:
	def hasDuplicate(self, nums: List[int]) -> bool:
		numsSeen = []
		for n in nums:
			if n in numsSeen:
				return True
			else:
				numsSeen.append(n)
		return False