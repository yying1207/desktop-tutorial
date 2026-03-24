class TestSearch:

    def __init__(self, nums=None, target=None):
        self.nums = nums
        self.target = target
        if target is not None and (not isinstance(target, int) or target < -10**4 or target > 10**4):
            raise ValueError("Target must be an integer between -10^4 and 10^4")
        if nums is not None and (not isinstance(nums, list) or len(nums) < 1 or len(nums) > 5000 or not all(isinstance(num, int) and -10**4 <= num <= 10**4 for num in nums)):
            raise ValueError("Nums must be a list of integers between -10^4 and 10^4, with length between 1 and 5000")
    
    def search_minimum_in_rotated_sorted_array(self, ) -> int:
        left, right = 0, len(self.nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if self.nums[mid] > self.nums[right]:
                left = mid + 1
            else:
                right = mid
        return self.nums.pop(left)
    
def test_search_list_and_minimum_in_rotated_sorted_array():
    test_array = [4, 5, 6, 7, 0, 1, 2]
    test_length = 4
    target = []
    init_array = TestSearch(test_array, test_length)
    for _ in range(test_length):
        target.append(init_array.search_minimum_in_rotated_sorted_array())
        #init_array.nums = init_array.nums[1:] + init_array.nums[:1]

    assert target == [0, 1, 2, 4]